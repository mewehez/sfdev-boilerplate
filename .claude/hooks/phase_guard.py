#!/usr/bin/env python3
"""
Garde mécanique PreToolUse. Deux refus, deux seulement.

  G1 — ordonnancement : on n'ouvre pas une TASK `dur` (juridique, domaine,
       hébergement, conformité) tant qu'une TASK `local` reste ouverte.
  G2 — design : on n'écrit pas un écran tant que product/assets/DESIGN.md
       n'existe pas.

Ces deux refus ne portent JAMAIS sur la preuve. Ils portent sur l'ordre.
Un refus est levé en faisant la chose dans le bon ordre, pas en argumentant.

Tout imprévu => on laisse passer. Un garde qui casse la session est pire
que pas de garde.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TASKS = ROOT / "backlog" / "tasks"
DESIGN = ROOT / "product" / "assets" / "DESIGN.md"
ECRAN_EXT = {".tsx", ".jsx", ".vue", ".svelte", ".astro", ".html"}
OUVERT = ("todo", "doing")


def deny(reason):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


def allow():
    sys.exit(0)


def front(text):
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    out = {}
    for line in parts[1].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def locales_ouvertes():
    out = []
    if not TASKS.is_dir():
        return out
    for f in TASKS.glob("TASK-*.md"):
        m = front(f.read_text(encoding="utf-8", errors="ignore"))
        if m.get("phase") == "local" and m.get("status") in OUVERT:
            out.append(m.get("id", f.stem))
    return sorted(out)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        allow()

    tool = data.get("tool_name", "")
    if tool not in ("Write", "Edit", "MultiEdit"):
        allow()

    ti = data.get("tool_input") or {}
    path = ti.get("file_path") or ""
    if not path:
        allow()
    p = Path(path)

    payload = " ".join(
        str(ti.get(k, "")) for k in ("content", "new_string", "new_str")
    )
    if not payload and isinstance(ti.get("edits"), list):
        payload = " ".join(str(e.get("new_string", "")) for e in ti["edits"])

    # ---------------------------------------------------------------- G1
    if p.name.startswith("TASK-") and p.suffix == ".md":
        if re.search(r"^\s*phase:\s*dur\s*$", payload, re.M):
            statut = re.search(r"^\s*status:\s*(\w+)\s*$", payload, re.M)
            if not statut or statut.group(1) in OUVERT:
                bloq = locales_ouvertes()
                if bloq:
                    deny(
                        "TASK `phase: dur` refusée : "
                        + ", ".join(bloq)
                        + " (phase local) sont encore ouvertes.\n"
                        "Le juridique, l'hébergement et la conformité viennent "
                        "APRÈS que l'app tourne.\n"
                        "→ soit tu fermes les TASK local, soit tu écris cette "
                        "tâche en `phase: pilote`, soit tu la déposes en "
                        "product/ideas/ comme IDEA à griller plus tard.\n"
                        "Un template juridique à trous n'est pas une TASK `dur` : "
                        "écris-le directement, sans TASK."
                    )

    # ---------------------------------------------------------------- G2
    if p.suffix.lower() in ECRAN_EXT and not DESIGN.exists():
        try:
            rel = p.resolve().relative_to(ROOT).as_posix()
        except Exception:
            rel = p.as_posix()
        if rel.startswith("src/"):
            deny(
                f"Écran refusé ({rel}) : product/assets/DESIGN.md n'existe pas.\n"
                "Un écran écrit sans direction de design produit du vibe coding "
                "— c'est constaté, pas supposé.\n"
                "→ invoque la skill `design-direction` d'abord. Elle prend "
                "un tour, pas une session."
            )

    allow()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        allow()
