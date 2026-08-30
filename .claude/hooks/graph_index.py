#!/usr/bin/env python3
"""
Régénère product/INDEX.md à partir du frontmatter des fichiers du graphe.
Zéro dépendance externe.

  python3 .claude/hooks/graph_index.py            # écrit + injecte le résumé
  python3 .claude/hooks/graph_index.py --quiet    # écrit seulement

Principe : ce hook CONSTATE, il ne range pas. Il ne crée aucun dossier
(sauf product/ pour écrire l'index) et ne déplace aucun fichier.

Régime par défaut : `exploration`. Aucune alerte de preuve, aucun blocage.
Les régimes `traces` et `terrain` ne s'activent que s'ils sont écrits
explicitement dans ADR-002 (voir .claude/optional/RIGUEUR.md).
"""
import re
import sys
import json
from pathlib import Path
from datetime import date, timedelta
from collections import defaultdict

# ============================================================ CONSTANTES
ROOT = Path(__file__).resolve().parents[2]
SCAN = [ROOT / "product", ROOT / "backlog"]
INDEX = ROOT / "product" / "INDEX.md"
ADR_REGIME = ROOT / "product" / "decisions" / "ADR-002-regime-preuve.md"
QUIET = "--quiet" in sys.argv

KINDS = ["IDEA", "SPEC", "BRIEF", "ADR", "DOM", "TRC", "SUG", "INT",
         "COPY", "PROMPT", "TASK"]
ID_RE = re.compile(r"\b((?:" + "|".join(KINDS) + r")-\d{3})\b")

IGNORE = {"INDEX.md", "README.md", "ART-DIRECTION.md", "JOURNAL.md",
          "DESIGN.md", "AMELIORATIONS.md"}
# hors graphe : ce sont des sources ou des brouillons, pas des nœuds
#   grill  transcripts d'ouverture de projet
#   legal  templates à trous de la phase `dur` — présents, jamais bloquants
IGNORE_DIRS = {"grill", "legal"}

# Une TASK écrite par `feature-build` est rétroactive : le code existait
# avant elle. Lui réclamer un parent, c'est réclamer le processus qu'on a
# précisément retiré du chemin par défaut. Elle est comptée, pas signalée.
DISPENSE_PARENT = {"feature-build"}

PARENT_RULES = {
    "SPEC":   ["IDEA"],
    "BRIEF":  ["SPEC"],
    "TASK":   ["SPEC", "BRIEF"],
    "COPY":   ["SPEC", "IDEA"],
    "PROMPT": ["COPY", "SPEC"],
}

# structure attendue du boilerplate (vérifiée, jamais créée)
ATTENDU = [
    "product/grill",
    "product/ideas", "product/decisions",
    "product/specs", "product/specs/briefs",
    "product/domain", "product/domain/traces", "product/domain/suggestions",
    "product/copy", "product/assets", "product/assets/prompts",
    "product/archive", "backlog/tasks",
]

# phases d'exécution (D4) — l'ordre est une contrainte, pas un conseil
PHASES = ["local", "pilote", "dur"]
OUVERT = ("todo", "doing")

# extensions qui font un écran : leur présence exige une direction de design
ECRAN_EXT = {".tsx", ".jsx", ".vue", ".svelte", ".html", ".astro"}
DESIGN_MD = ROOT / "product" / "assets" / "DESIGN.md"
SRC = ROOT / "src"

# skills locales qui empiéteraient sur l'aval (Superpowers)
AVAL = {"tdd", "test-driven", "debug", "code-review", "executing-plans",
        "subagent-driven", "writing-plans"}

# initialisés ici : lus par l'écriture de l'index quel que soit le régime
domaines, types = {}, {}


# ============================================================== HELPERS
def parse(path):
    """Retourne le frontmatter + les IDs cités dans le corps, ou None."""
    txt = path.read_text(encoding="utf-8", errors="ignore")
    if not txt.startswith("---"):
        return None
    parts = txt.split("---", 2)
    if len(parts) < 3:
        return None
    _, front, body = parts

    meta = {
        "path": path.relative_to(ROOT).as_posix(),
        "body_links": set(ID_RE.findall(body)),
    }
    for line in front.splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        meta[key.strip()] = val.strip().strip("[]").strip()
    return meta if "id" in meta else None


def read_regime():
    """Régime déclaré dans ADR-002. Absent ou illisible => exploration."""
    if not ADR_REGIME.exists():
        return "exploration"
    m = re.search(r"regime:\s*([\w-]+)", ADR_REGIME.read_text(encoding="utf-8"))
    return m.group(1) if m else "exploration"


def fichiers_src():
    """Fichiers de code sous src/, hors dépendances."""
    if not SRC.is_dir():
        return [], []
    skip = {"node_modules", ".venv", "venv", "__pycache__", "dist",
            "build", ".next", "target"}
    tous, ecrans = [], []
    for f in SRC.rglob("*"):
        if not f.is_file() or skip & set(f.relative_to(SRC).parts):
            continue
        tous.append(f)
        if f.suffix.lower() in ECRAN_EXT:
            ecrans.append(f)
    return tous, ecrans


def source_key(meta):
    """Identifie la source d'une trace : domaine web, ou libellé normalisé."""
    src = (meta.get("source") or "").strip()
    if not src:
        return None
    m = re.match(r"https?://(?:www\.)?([^/\s]+)", src, re.I)
    if m:
        return m.group(1).lower()
    return re.sub(r"\s+", " ", src.lower())[:40]


def chaine(nid):
    """Liens directs + liens des parents directs (profondeur 2)."""
    direct = outgoing.get(nid, set())
    return direct | {l for p in direct for l in outgoing.get(p, set())}


# ============================================================== COLLECTE
nodes, reserved, problems = {}, {}, []

for base in SCAN:
    if not base.exists():
        continue
    for path in sorted(base.rglob("*.md")):
        if path.name in IGNORE:
            continue
        parts = path.relative_to(base).parts[:-1]
        if IGNORE_DIRS & set(parts):
            continue

        rel = path.relative_to(ROOT)
        archived = "archive" in parts

        meta = parse(path)
        if meta is None:
            if not archived:
                problems.append(f"Sans frontmatter valide : {rel}")
            continue

        nid = meta["id"]
        if not ID_RE.fullmatch(nid):
            problems.append(
                f"ID hors convention : {nid} ({rel}) — attendu <TYPE>-nnn, 3 chiffres"
            )
            continue
        if nid in nodes or nid in reserved:
            autre = nodes[nid]["path"] if nid in nodes else reserved[nid]["path"]
            problems.append(f"ID dupliqué : {nid} — {autre} et {rel}")
            continue

        if archived:
            reserved[nid] = meta          # ID pris, hors graphe
        else:
            nodes[nid] = meta


# ================================================================ LIENS
outgoing = {}
backlinks = defaultdict(set)

for nid, meta in nodes.items():
    declared = {x.strip() for x in meta.get("links", "").split(",") if x.strip()}
    linked = (declared | meta["body_links"]) - {nid}
    outgoing[nid] = linked
    for target in linked:
        backlinks[target].add(nid)
        if target in reserved:
            problems.append(
                f"{nid} dépend de {target}, archivé — décision fondée sur du mort"
            )
        elif target not in nodes:
            problems.append(f"{nid} pointe vers {target} — inexistant")

by_kind = defaultdict(list)
for nid, meta in nodes.items():
    by_kind[nid.split("-")[0]].append((nid, meta))

ints = by_kind.get("INT", [])
humans = [nid for nid, m in ints if m.get("humain") == "oui"]
trcs = by_kind.get("TRC", [])
sugs = by_kind.get("SUG", [])


# =============================================== CONTRÔLES DE STRUCTURE
for nid in nodes:
    kind = nid.split("-")[0]
    expected = PARENT_RULES.get(kind)
    if not expected:
        continue
    if kind == "TASK" and (
        nodes[nid].get("chemin") == "court"
        or nodes[nid].get("origine") in DISPENSE_PARENT
    ):
        continue                     # dispense : chemin court, ou feature-build
    if not any(l.split("-")[0] in expected for l in outgoing[nid]):
        problems.append(f"{nid} orphelin — aucun parent {'/'.join(expected)}")

for nid, meta in nodes.items():
    if not meta.get("status"):
        problems.append(f"{nid} sans status")
    if not meta.get("updated"):
        problems.append(f"{nid} sans date updated")
    if nid.split("-")[0] in ("DOM", "TRC") and not meta.get("source"):
        problems.append(f"{nid} sans champ source — ce n'est pas une preuve")


# ==================================================== DETTE D'HYPOTHÈSES
for nid, meta in sugs:
    st = meta.get("status")
    if st not in ("pending", "validé", "invalidé", "abandonné"):
        problems.append(f"{nid} status invalide : '{st}'")
    if st == "validé" and not meta.get("preuve"):
        problems.append(f"{nid} validé sans champ preuve — qu'est-ce qui l'a confirmé ?")
    if st == "pending" and not backlinks[nid]:
        problems.append(f"{nid} pending sans backlink — quelle décision en dépend ?")
    if st == "invalidé":
        for dep in sorted(backlinks[nid]):
            problems.append(f"{dep} repose sur {nid}, invalidé — à revoir")


# ====================================================== RÉGIME DE PREUVE
regime = read_regime()
if regime not in ("exploration", "auto-usage", "traces", "terrain"):
    problems.append(f"ADR-002 : régime inconnu '{regime}' — voir .claude/optional/RIGUEUR.md")
    regime = "exploration"

vieilles = 0

if regime == "auto-usage":
    agents_dir = ROOT / ".claude" / "agents"
    if agents_dir.exists():
        for p in agents_dir.glob("*-persona.md"):
            if p.name != "persona-TEMPLATE.md":
                problems.append(
                    f"{p.name} présent en régime auto-usage — tu es l'utilisateur"
                )

elif regime == "traces":
    perime = (date.today() - timedelta(days=180)).isoformat()
    fraiches = [(nid, m) for nid, m in trcs if str(m.get("updated", "")) >= perime]
    vieilles = len(trcs) - len(fraiches)

    domaines, types = defaultdict(list), defaultdict(list)
    for nid, m in fraiches:
        k = source_key(m)
        if k is None:
            problems.append(f"{nid} sans source exploitable — non compté")
            continue
        domaines[k].append(nid)
        t = m.get("type")
        if not t:
            problems.append(f"{nid} sans champ type")
        else:
            types[t].append(nid)

    total = sum(len(v) for v in domaines.values())
    if total >= 3:
        top, items = max(domaines.items(), key=lambda kv: len(kv[1]))
        part = round(100 * len(items) / total)
        if part > 60:
            problems.append(
                f"Traces concentrées : {part}% viennent de {top} — "
                f"une seule source ne fait pas un échantillon"
            )
    if total and len(types) == 1:
        problems.append(
            f"Toutes les traces sont de type '{next(iter(types))}' — "
            f"croiser avec un autre type"
        )

    for nid, meta in by_kind.get("BRIEF", []):
        if meta.get("status") != "ready":
            continue
        if not any(x.startswith(("TRC", "INT", "DOM")) for x in chaine(nid)):
            problems.append(
                f"{nid} ready sans aucune observation dans sa chaîne — "
                f"collecter un TRC ou écrire un ADR de dérogation"
            )
        elif len(domaines) < 2:
            problems.append(
                f"{nid} ready sur une seule source distincte — croiser avant de coder"
            )

elif regime == "terrain":
    if not humans:
        for nid, meta in by_kind.get("BRIEF", []):
            if meta.get("status") == "ready":
                problems.append(
                    f"{nid} ready en régime terrain sans interview humaine — "
                    f"écrire un ADR de dérogation ou repasser en draft"
                )


# ================================================ FRONTIÈRE SUPERPOWERS
if regime != "exploration":
    for nid, meta in by_kind.get("BRIEF", []):
        if meta.get("status") == "ready" and not any(
            b.startswith("TASK") for b in backlinks[nid]
        ):
            problems.append(f"{nid} ready sans TASK — relais Superpowers non amorcé")


# ================================================== PHASES D'EXÉCUTION (D4)
tasks = by_kind.get("TASK", [])
par_phase = defaultdict(list)
for nid, m in tasks:
    ph = m.get("phase")
    if ph is None:
        problems.append(f"{nid} sans champ phase — attendu local | pilote | dur")
        continue
    if ph not in PHASES:
        problems.append(f"{nid} phase invalide : '{ph}' — attendu local | pilote | dur")
        continue
    par_phase[ph].append((nid, m))

locales_ouvertes = sorted(
    nid for nid, m in par_phase["local"] if m.get("status") in OUVERT
)
dures_ouvertes = sorted(
    nid for nid, m in par_phase["dur"] if m.get("status") in OUVERT
)
if locales_ouvertes and dures_ouvertes:
    problems.append(
        "Ordre rompu : " + ", ".join(dures_ouvertes) + " (dur) ouverte(s) alors que "
        + ", ".join(locales_ouvertes) + " (local) ne l'est pas encore — "
        "l'app doit tourner avant le juridique"
    )


# ======================================================== CODE ET DESIGN
src_files, src_ecrans = fichiers_src()
design_ok = DESIGN_MD.exists()
if src_ecrans and not design_ok:
    problems.append(
        f"{len(src_ecrans)} écran(s) sous src/ sans product/assets/DESIGN.md — "
        "invoquer la skill design-direction"
    )

skills_dir = ROOT / ".claude" / "skills"
if skills_dir.exists():
    for d in skills_dir.iterdir():
        if d.is_dir() and any(k in d.name.lower() for k in AVAL):
            problems.append(f"skill locale '{d.name}' recouvre Superpowers — supprimer")


# ============================================== STRUCTURE DE RÉPERTOIRES
attendu = list(ATTENDU)
if regime == "terrain":
    attendu.append("product/domain/interviews")

for d in attendu:
    if not (ROOT / d).is_dir():
        problems.append(f"Dossier manquant : {d}/ — structure du boilerplate incomplète")

autorises = set(ATTENDU) | {"product", "backlog", "product/domain/interviews"}
for base in SCAN:
    if not base.exists():
        continue
    for path in base.rglob("*.md"):
        if path.name in IGNORE:
            continue
        parts = path.relative_to(base).parts[:-1]
        if IGNORE_DIRS & set(parts) or "archive" in parts:
            continue
        parent = path.parent.relative_to(ROOT).as_posix()
        if parent not in autorises:
            problems.append(f"{path.relative_to(ROOT)} hors structure attendue")

problems = sorted(set(problems))


# ============================================================= AGRÉGATS
by_status = defaultdict(list)
for nid, meta in nodes.items():
    by_status[meta.get("status", "?")].append(nid)

raw = sorted(n for n in by_status["raw"] if n.startswith("IDEA"))
parked = sorted(n for n in by_status["parked"] if n.startswith("IDEA"))
specd = sorted(by_status["specd"])
ready = sorted(by_status["ready"])

pending = sorted(nid for nid, m in sugs if m.get("status") == "pending")
porteurs = set()
for nid in pending:
    porteurs |= {b for b in backlinks[nid] if not b.startswith("SUG")}
briefs_dette = sorted(
    nid for nid, m in by_kind.get("BRIEF", [])
    if m.get("status") == "ready" and chaine(nid) & set(pending)
)

cutoff = (date.today() - timedelta(days=30)).isoformat()
recent = [(nid, m) for nid, m in by_kind.get("TASK", [])
          if str(m.get("updated", "")) >= cutoff]
courts = [nid for nid, m in recent if m.get("chemin") == "court"]
directes = [nid for nid, m in by_kind.get("TASK", [])
            if m.get("origine") in DISPENSE_PARENT]
part_courte = round(100 * len(courts) / len(recent)) if recent else 0


# ============================================================= ÉCRITURE
lines = [
    "---", "id: INDEX-000", "title: Index du graphe",
    "status: generated", "updated: auto", "---", "",
    "> Régénéré automatiquement par .claude/hooks/graph_index.py.",
    "> Ne pas éditer à la main.", "",
    f"Régime : **{regime}**"
    + ("  (mode unique par défaut — aucun blocage)" if regime == "exploration" else ""),
    "",
    f"Code : **{len(src_files)}** fichier(s) sous src/, dont {len(src_ecrans)} écran(s)."
    + ("  DESIGN.md présent." if design_ok else "  Pas de DESIGN.md."),
    "",
]

if problems:
    lines += ["## ! Incohérences", ""] + [f"- {p}" for p in problems] + [""]

if directes:
    lines += [f"Dont **{len(directes)}** TASK écrite(s) après le code "
              f"(`origine: feature-build`) — sans parent, par construction.", ""]

if tasks:
    lines += ["## Phases", ""]
    for ph in PHASES:
        items = par_phase.get(ph, [])
        if not items:
            continue
        ouv = [n for n, m in items if m.get("status") in OUVERT]
        lines.append(
            f"- `{ph}` — {len(items)} TASK, {len(ouv)} ouverte(s)"
            + (f" : {', '.join(sorted(ouv))}" if ouv else "")
        )
    lines += [""]

if raw:
    lines += ["## File de grill", ""]
    for nid in raw:
        m = nodes[nid]
        ctx = m.get("contexte", "")
        ctx = f" — {ctx}" if ctx else ""
        lines.append(
            f"- [[{nid}]] {m.get('title','')} — capturée {m.get('updated','?')}{ctx}"
        )
    lines += [""]

if parked:
    lines += ["## Parquées (dégeler seulement si la question décisive est levée)", ""]
    lines += [f"- [[{nid}]] {nodes[nid].get('title','')}" for nid in parked]
    lines += [""]

if pending:
    lines += ["## Dette d'hypothèses (SUG pending)", ""]
    for nid in pending:
        m = nodes[nid]
        dep = sorted(b for b in backlinks[nid] if not b.startswith("SUG"))
        lines.append(
            f"- [[{nid}]] {m.get('title','')} ← {', '.join(dep) if dep else 'rien'}"
        )
        lines.append(f"    ? {m.get('question','')}")
    lines += [""]

if regime == "traces" and trcs:
    lines += ["## Diversité des traces (fraîches)", ""]
    for k in sorted(domaines, key=lambda x: -len(domaines[x])):
        lines.append(f"- `{k}` — {len(domaines[k])} : {', '.join(sorted(domaines[k]))}")
    for t in sorted(types, key=lambda x: -len(types[x])):
        lines.append(f"- type `{t}` — {len(types[t])}")
    lines += [""]

if reserved:
    lines += [f"## IDs réservés — archivés ({len(reserved)})", ""]
    for nid in sorted(reserved):
        m = reserved[nid]
        lines.append(f"- `{nid}` {m.get('title','')} — {m.get('status','?')}")
    lines += ["", "> Ne jamais réattribuer ces IDs.", ""]

for kind in KINDS:
    items = sorted(by_kind.get(kind, []))
    if not items:
        continue
    lines.append(f"## {kind} ({len(items)})")
    for nid, m in items:
        refs = f" ←{len(backlinks[nid])}" if backlinks[nid] else ""
        extra = ""
        if kind == "INT":
            extra = " [humain]" if m.get("humain") == "oui" else " [simulé]"
        elif kind == "TASK" and m.get("chemin") == "court":
            extra = " [court]"
        lines.append(
            f"- [[{nid}]] `{m.get('status','?')}`{extra} {m.get('title','')}{refs}"
        )
    lines.append("")

INDEX.parent.mkdir(parents=True, exist_ok=True)
INDEX.write_text("\n".join(lines), encoding="utf-8")

if QUIET:
    sys.exit(0)


# ==================================================== INJECTION CONTEXTE
tete = f"Graphe : {len(nodes)} objets. product/INDEX.md à jour."
if reserved:
    tete += f" {len(reserved)} ID(s) archivé(s), réservés."

summary = [
    tete,
    f"Code : {len(src_files)} fichier(s) sous src/, {len(src_ecrans)} écran(s)"
    + ("" if design_ok else " | pas de DESIGN.md"),
    f"À GRILLER : {len(raw)}" + (f" — {', '.join(raw[:6])}" if raw else " — file vide"),
]

if tasks:
    detail = " | ".join(
        f"{ph} {len([1 for n, m in par_phase.get(ph, []) if m.get('status') in OUVERT])}"
        f"/{len(par_phase.get(ph, []))}"
        for ph in PHASES if par_phase.get(ph)
    )
    summary.append(f"TASK ouvertes/total par phase : {detail}")

if regime == "exploration":
    pass                     # mode par défaut : rien à annoncer, rien à bloquer
elif regime == "auto-usage":
    summary.append("Régime auto-usage — tu es l'utilisateur.")
elif regime == "traces":
    total = sum(len(v) for v in domaines.values())
    ligne = (f"Régime traces — {total} obs. fraîche(s), "
             f"{len(domaines)} source(s) distincte(s), {len(types)} type(s)")
    if vieilles:
        ligne += f" | {vieilles} périmée(s)"
    if not trcs:
        ligne += "  ! aucune trace — tout BRIEF sera bloqué"
    elif len(domaines) < 2:
        ligne += "  ! source unique — BRIEF bloqués"
    summary.append(ligne)
elif regime == "terrain":
    summary.append(
        f"Régime terrain — {len(ints)} interviews dont {len(humans)} humaines"
        + ("  ! BRIEF bloqués tant que 0 humaine" if not humans else "")
    )


if sugs:
    # en exploration, une hypothèse est tracée, pas reprochée
    summary.append(
        f"Hypothèses : {len(pending)} pending, {len(sugs) - len(pending)} tranchée(s)"
    )

if regime != "exploration" and briefs_dette:
    summary.append(
        f"! {len(briefs_dette)} BRIEF ready reposent sur du [SUPPOSÉ] : "
        + ", ".join(briefs_dette[:4])
    )

if locales_ouvertes and dures_ouvertes:
    summary.append(
        f"! {len(dures_ouvertes)} TASK `dur` ouverte(s) alors que "
        f"{len(locales_ouvertes)} `local` reste(nt) — le hook de garde les refusera"
    )

if src_ecrans and not design_ok:
    summary.append("! écrans sans DESIGN.md — invoquer design-direction")

if problems:
    summary.append(f"! {len(problems)} incohérence(s) — voir product/INDEX.md")

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": "\n".join(summary),
    }
}))