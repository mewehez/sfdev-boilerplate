#!/usr/bin/env python3
"""Un `[[ID]]` pointe-t-il vers quelque chose ?

Un lien qui pointe vers rien est **pire qu'un lien absent** : il
s'affiche, il se clique, il ouvre une page vide — et rien ne dit si c'est
l'objet qui manque ou l'outillage qui a raté. On a tenu tout un projet
avec un graphe fait de fantômes sans le savoir (TASK-035).

    python3 outils/liens_morts.py       # 0 si tout lien a sa cible

Deux vérifications, et la seconde est celle qui manquait :

1. **Chaque `[[...]]` désigne un fichier existant.** Une cible sans
   fichier est soit une faute de frappe, soit un objet jamais écrit — les
   deux se corrigent, aucun ne se tolère.
2. **Un lien vers un objet nomme son FICHIER**, pas son ID seul.
   `[[SPEC-002]]` compte sur l'alias pour résoudre, et l'alias ne résout
   pas de façon fiable : le lien devient un fantôme, sans un mot. La
   forme sûre est `[[SPEC-002-un-titre-long|SPEC-002]]` —
   le nom de fichier ne dépend d'aucune résolution, et le texte affiché
   reste l'ID.
3. **Une séance mène quelque part.** Un transcript de `grill/` sans
   aucune arête entrante est une trace perdue : le fichier existe, il est
   lisible, et il est introuvable. `ADR-008`, `ADR-009` et `ADR-010`
   sortent tous d'une même séance — un ADR dit ce qui a été décidé, pas
   comment on y est arrivé.
4. **Il n'y a qu'un seul coffre.** Un `.obsidian/` dans un sous-dossier
   fait un second coffre qui ne voit qu'une partie du dépôt — et rien ne
   dit lequel des deux on a ouvert. Obsidian le recrée tout seul dès
   qu'on rouvre l'ancien : il faut le fermer, pas seulement l'effacer.
"""
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SCAN = [RACINE / "product", RACINE / "backlog"]

KINDS = ["IDEA", "SPEC", "BRIEF", "ADR", "DOM", "TRC", "SUG", "INT",
         "COPY", "PROMPT", "TASK"]
ID_RE = re.compile(r"^((?:" + "|".join(KINDS) + r")-\d{3})$")
LIEN_RE = re.compile(r"\[\[([^\]|#]+)")
# Obsidian ne fait pas de lien dans du code — ni entre backticks, ni dans
# un bloc clôturé. Un contrôle qui l'ignore signale les exemples qu'on
# écrit pour EXPLIQUER les liens, et devient du bruit là où il devrait
# être rare.
BLOC_RE = re.compile(r"^```.*?^```", re.S | re.M)
CODE_RE = re.compile(r"`[^`\n]*`")
# Un bloc indenté de quatre espaces est du code aussi — c'est la forme
# qu'on utilise pour montrer une commande ou un frontmatter. Elle avait
# été oubliée, et le contrôle signalait un exemple tronqué comme un lien
# mort. Il faut du temps pour comprendre qu'un contrôle a tort, et ce
# temps se paie chaque fois qu'il crie pour rien.
INDENTE_RE = re.compile(r"^(?: {4}|\t).*$", re.M)


def hors_code(txt: str) -> str:
    return CODE_RE.sub("", INDENTE_RE.sub("", BLOC_RE.sub("", txt)))

# Les listes FERMÉES de `CLAUDE.md`. Un statut hors liste ne casse rien :
# il ment doucement, et le prochain qui filtre ne voit pas l'objet.
STATUTS = {
    "IDEA": ("raw", "parked", "specd", "killed"),
    "SPEC": ("specd", "remplacée", "caduque"),
    "BRIEF": ("draft", "ready", "shipped", "caduc"),
    "DOM": ("raw", "hypothèse", "confirmé"),
    "TRC": ("raw", "confirmé"),
    "SUG": ("pending", "validée", "invalidée"),
}

# Hors graphe : ni ID, ni frontmatter attendus (CLAUDE.md).
IGNORE_DIRS = {"grill", "legal"}


def objets() -> tuple[dict[str, Path], list[str]]:
    """Les objets du graphe par ID, et ceux à qui l'alias manque."""
    par_id: dict[str, Path] = {}
    sans_alias: list[str] = []
    hors_liste: list[str] = []

    for base in SCAN:
        for f in sorted(base.rglob("*.md")):
            if any(p in IGNORE_DIRS for p in f.parts):
                continue
            txt = f.read_text(encoding="utf-8", errors="ignore")
            if not txt.startswith("---"):
                continue
            front = txt.split("---", 2)[1]

            ident, alias, dans_alias, statut = None, set(), False, None
            for ligne in front.splitlines():
                nu = ligne.strip()
                # Une liste de bloc : c'est la forme qu'Obsidian écrit
                # lui-même, et la seule qu'il résout à coup sûr.
                if dans_alias and nu.startswith("- "):
                    alias.add(nu[2:].strip().strip('"').strip("'"))
                    continue
                dans_alias = False
                if ligne.startswith("id:"):
                    ident = ligne.split(":", 1)[1].strip()
                elif ligne.startswith("status:"):
                    statut = ligne.split(":", 1)[1].strip()
                elif ligne.startswith("aliases:"):
                    val = ligne.split(":", 1)[1].strip()
                    if val:
                        alias |= {a.strip().strip('"').strip("'")
                                  for a in val.strip("[]").split(",") if a.strip()}
                    else:
                        dans_alias = True
            if not ident or not ID_RE.match(ident):
                continue

            par_id[ident] = f
            if ident not in alias:
                sans_alias.append(f"{ident} — {f.relative_to(RACINE)}")

            # ! Le statut, confronté à sa liste FERMÉE.
            #
            # Rien ne le vérifiait, et six objets ont porté `done` — un
            # mot qui n'existe dans aucune liste. Il ne casse rien : il
            # ment doucement, et le prochain qui filtre sur `specd` ne
            # les voit pas. Un statut hors liste est le même défaut qu'un
            # lien vers rien, en plus discret.
            genre = ident.split("-")[0]
            permis = STATUTS.get(genre)
            if permis and statut is not None and statut not in permis:
                hors_liste.append(
                    f"{ident} — `{statut}`, attendu : {' | '.join(permis)}")
    return par_id, sans_alias, hors_liste


def seances_perdues(liens_vers: set[str]) -> list[str]:
    """Les séances que rien ne cite.

    Elles sont hors graphe — ce sont des sources, pas des objets — mais
    hors graphe ne veut pas dire hors d'atteinte.
    """
    return [f.stem for f in sorted((RACINE / "product" / "grill").glob("*.md"))
            if f.stem not in liens_vers]


def coffres() -> list[Path]:
    """Les `.obsidian/` du dépôt. Il n'en faut qu'un, à la racine."""
    return sorted(p for p in RACINE.rglob(".obsidian")
                  if p.is_dir()
                  and not any(x in p.parts for x in
                              ("node_modules", ".venv", ".git")))


def main() -> int:
    par_id, sans_alias, hors_liste = objets()

    # ! Un second coffre ne se voit pas : il s'ouvre, il affiche un
    # graphe, et ce graphe est faux d'un tiers sans le dire.
    en_trop = [c for c in coffres() if c.parent != RACINE]

    # Les cibles valides incluent l'INDEX et tout fichier nommé par son
    # titre : on ne vérifie que les liens qui PRÉTENDENT désigner un ID.
    # Les noms de fichiers du coffre : c'est ce qu'un lien doit nommer.
    stems = {p.stem for base in (RACINE,) for p in base.rglob("*.md")
             if not any(x in p.parts for x in
                        ("node_modules", ".venv", ".git", "src"))}

    morts: list[str] = []
    fragiles: list[str] = []
    vises: set[str] = set()
    for base in SCAN:
        for f in sorted(base.rglob("*.md")):
            if any(p in IGNORE_DIRS for p in f.parts):
                continue
            txt = hors_code(f.read_text(encoding="utf-8", errors="ignore"))
            for cible in LIEN_RE.findall(txt):
                cible = cible.strip()
                vises.add(cible)
                if cible in stems:
                    continue
                # ! Un `[[ID]]` nu : il ne résoudra que si l'alias le
                # veut bien, et l'alias ne le veut pas toujours.
                if ID_RE.match(cible):
                    fragiles.append(f"{f.relative_to(RACINE)} → [[{cible}]]")
                else:
                    # ! Toute cible inconnue, pas seulement celles qui
                    # RESSEMBLENT à un ID. Le contrôle ne regardait que
                    # les cibles en forme de `TYPE-nnn` : il a déclaré
                    # « cohérent » un lien vers un nom inventé, ce qui est
                    # précisément ce qu'il existe pour trouver.
                    morts.append(f"{f.relative_to(RACINE)} → [[{cible}]]")

    perdues = seances_perdues(vises)

    if not (morts or sans_alias or en_trop or fragiles or perdues or hors_liste):
        print(f"Liens cohérents — {len(par_id)} objets, toutes les cibles existent,\n"
              "toutes les séances mènent quelque part.")
        return 0

    if en_trop:
        print(f"! {len(en_trop)} coffre(s) Obsidian en trop — le coffre est la RACINE :\n")
        for c in en_trop:
            print(f"  {c.relative_to(RACINE)}")
        print("\n  Le fermer DANS Obsidian avant de l’effacer : sinon il le recrée.\n")

    if hors_liste:
        print(f"! {len(hors_liste)} statut(s) hors de leur liste fermée :\n")
        for h in sorted(hors_liste):
            print(f"  {h}")
        print()
        print("Un statut hors liste ne casse rien : il ment doucement, et le")
        print("prochain qui filtre ne voit pas l'objet.")
        print()
    if sans_alias:
        print(f"! {len(sans_alias)} objet(s) sans alias — `[[ID]]` ouvrira un fantôme :\n")
        for l in sans_alias:
            print(f"  {l}")
        print()
    if fragiles:
        print(f"! {len(fragiles)} lien(s) qui comptent sur l’alias — nommer le fichier :\n")
        for l in sorted(set(fragiles))[:20]:
            print(f"  {l}")
        print("\n  python3 outils/graphe_obsidian.py --ecrire\n")
    if perdues:
        print(f"! {len(perdues)} séance(s) que rien ne cite :\n")
        for s in perdues:
            print(f"  product/grill/{s}.md")
        print("\n  La citer depuis ce qu’elle a produit : [[" + perdues[0] + "]]\n")
    if morts:
        print(f"! {len(morts)} lien(s) sans cible :\n")
        for l in sorted(set(morts)):
            print(f"  {l}")
        print()
    print("Un lien vers rien s’affiche et se clique. Écrire l’objet, ou\n"
          "corriger l’ID — jamais laisser le lien pendre.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
