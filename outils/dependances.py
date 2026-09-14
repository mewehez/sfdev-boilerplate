#!/usr/bin/env python3
"""Les failles connues des dépendances — celles qu'on installe.

Il existe parce qu'il a manqué. Le 2026-09-08, une instance mise en ligne
a été sondée avec succès **dans les vingt minutes** par une faille
publiée neuf mois plus tôt, dans une dépendance, à distance de tout ce
que le dépôt savait vérifier : deux cent vingt-cinq tests verts, quatre
contrôles mécaniques verts, et personne ne regardait ça.

! Le défaut n'était pas dans le code écrit ici. C'est précisément ce qui
le rendait invisible : rien de ce qu'on relit ne le contenait.

! Et il ne coûtait rien tant que la pile tournait sur une machine
d'atelier. Un contrôle qui ne sert qu'au moment de la mise en ligne doit
donc tourner **avant**, pas ce jour-là.

    python3 outils/dependances.py

! Il rend **trois** codes, et la distinction n'est pas cosmétique :

    0   rien à signaler — **et des verrous ont bien été ouverts**
    1   des failles connues — ça bloque
    3   **pas pu auditer** : les outils manquent, ou il n'y avait aucun
        verrou à ouvrir

Confondre 1 et 3 est ce qui a arrêté un déploiement pour rien : sur le
serveur, ni `pnpm` ni `uv` n'existent — tout s'y construit dans Docker —
et le contrôle criait « failles connues » alors qu'il n'avait rien
regardé. Un contrôle qui crie pour rien cesse d'être lu.

L'audit a sa place **là où vivent les verrous** : sur la machine où l'on
modifie les dépendances, avant l'envoi. `envoyer.sh` le lance et refuse
de partir s'il est rouge.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent


def _lancer(cmd: list[str], cwd: Path) -> tuple[int, str]:
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                           timeout=600)
        return r.returncode, (r.stdout or "") + (r.stderr or "")
    except FileNotFoundError:
        return 127, ""
    except subprocess.TimeoutExpired:
        return 124, "délai dépassé"


def web(dossier: Path) -> tuple[str | None, list[str]]:
    """`pnpm audit` sur les dépendances de production seulement.

    ! `--prod` et non l'ensemble : une faille dans un outil de
    construction ne s'expose à personne, et un contrôle qui crie pour
    rien cesse d'être lu.

    Rend `(ce qui a été ouvert, les lignes)`. Le premier membre est
    `None` quand il n'y avait rien à ouvrir — et c'est lui qui empêche
    un « rien à signaler » de vouloir dire « je n'ai rien regardé ».
    """
    if not (dossier / "package.json").exists():
        return None, []
    ouvert = f"{dossier.name}/package.json"
    if shutil.which("pnpm") is None:
        return ouvert, ["pnpm introuvable — dépendances web non auditées"]
    code, sortie = _lancer(["pnpm", "audit", "--prod", "--json"], dossier)
    if code == 127:
        return ouvert, ["pnpm introuvable — dépendances web non auditées"]
    trouvees: list[str] = []
    for ligne in sortie.splitlines():
        ligne = ligne.strip()
        if not ligne.startswith("{"):
            continue
        try:
            d = json.loads(ligne)
        except json.JSONDecodeError:
            continue
        for a in (d.get("advisories") or {}).values():
            trouvees.append(
                f"{a.get('severity', '?'):8s} {a.get('module_name', '?')} "
                f"{a.get('vulnerable_versions', '')} → "
                f"{a.get('patched_versions', '')}\n"
                f"           {(a.get('title') or '')[:96]}")
    if not trouvees and code not in (0, 1):
        return ouvert, [f"pnpm audit a échoué (code {code})"]
    return ouvert, trouvees


def api(dossier: Path) -> tuple[str | None, list[str]]:
    """Les dépendances Python, par `pip-audit` s'il est là.

    ! On ne l'installe pas d'autorité : un contrôle qui modifie
    l'environnement pour pouvoir s'exécuter n'est plus un contrôle. On
    dit ce qui manque, et comment l'avoir.
    """
    # ! `requirements.txt` compte autant que `pyproject.toml`. Ne
    # reconnaître qu'une forme de projet Python, c'est rendre « rien à
    # signaler » sur l'autre — sans l'avoir ouverte.
    verrou = next((n for n in ("pyproject.toml", "requirements.txt")
                   if (dossier / n).exists()), None)
    if verrou is None:
        return None, []
    ouvert = f"{dossier.name}/{verrou}"
    code, sortie = _lancer(
        ["uv", "run", "--with", "pip-audit", "pip-audit", "--strict",
         "--progress-spinner", "off"], dossier)
    if code == 127:
        return ouvert, ["uv introuvable — dépendances Python non auditées"]
    if code == 0:
        return ouvert, []
    lignes = [l for l in sortie.splitlines()
              if l.strip() and not l.startswith(("Resolved", "Audited",
                                                 "Installed", "Prepared"))]
    return ouvert, (lignes[-30:] if lignes
                    else [f"pip-audit a échoué (code {code})"])


# ! Ce qui distingue « pas pu regarder » de « j'ai vu quelque chose ».
# La phrase est produite par les deux fonctions ci-dessus ; on la
# reconnaît ici plutôt que de rendre deux listes séparées partout.
def _est_une_absence(ligne: str) -> bool:
    return "introuvable" in ligne or "non audité" in ligne


def main() -> int:
    failles: dict[str, list[str]] = {}
    absences: list[str] = []
    ouverts: list[str] = []
    for nom, fn, chemin in (("web", web, RACINE / "src" / "web"),
                            ("api", api, RACINE / "src" / "api")):
        if not chemin.exists():
            continue
        ouvert, lignes = fn(chemin)
        if ouvert is not None:
            ouverts.append(ouvert)
        for ligne in lignes:
            (absences if _est_une_absence(ligne) else
             failles.setdefault(nom, [])).append(ligne)

    # ! Le troisième code, pris un cran plus haut qu'il ne l'était.
    #
    # Il ne couvrait que « l'auditeur manque ». Il manquait « il n'y
    # avait rien à auditer » : sur un dépôt sans `src/web` ni `src/api`
    # — le socle lui-même, ou un produit rangé autrement — les deux
    # boucles ne produisaient rien et le contrôle annonçait
    # « Dépendances sans faille connue ».
    #
    # C'est la forme la plus chère de ce défaut : il ne crie pas, il
    # RASSURE. Un projet neuf serait parti avec un audit vert qui
    # n'avait ouvert aucun fichier.
    if not ouverts:
        print("! Aucun verrou de dépendances trouvé :\n")
        print(f"  ni src/web/package.json ni src/api/pyproject.toml "
              f"(ou requirements.txt) sous {RACINE}")
        print()
        print("Ce n'est PAS « aucune faille » : c'est « il n'y avait rien à")
        print("ouvrir ». Si ce dépôt a des dépendances rangées ailleurs, le")
        print("contrôle ne les voit pas — et il ne le dira jamais tout seul.")
        return 3

    if failles:
        total = sum(len(v) for v in failles.values())
        print(f"! {total} ligne(s) sur les dépendances installées :\n")
        for nom, lignes in failles.items():
            print(f"  — {nom} —")
            for l in lignes:
                print(f"  {l}")
            print()
        print("Une faille de dépendance ne se voit dans aucun test : elle n'est")
        print("pas dans le code qu'on relit. Elle se corrige en montant la")
        print("version, ou en l'imposant si elle vient d'une dépendance de")
        print("dépendance (pnpm-workspace.yaml → overrides).")
        return 1

    if absences:
        print("! Rien n'a pu être audité :\n")
        for l in absences:
            print(f"  {l}")
        print()
        print("Ce n'est PAS « aucune faille » : c'est « je n'ai pas regardé ».")
        print("L'audit se fait là où vivent les verrous — sur la machine de")
        print("travail, avant l'envoi — pas sur le serveur, qui construit")
        print("tout dans Docker et n'a aucune raison d'avoir ces outils.")
        return 3

    print("Dépendances sans faille connue.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
