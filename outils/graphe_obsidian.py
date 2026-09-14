#!/usr/bin/env python3
"""Mettre un graphe existant à la forme qu'Obsidian sait lire.

Un dépôt écrit avant cette convention porte un frontmatter que le hook
comprend et qu'Obsidian ignore :

    id: SPEC-002
    links: [ADR-007, INT-005]

Le fichier s'appelle `SPEC-002-un-titre-long.md`, donc `[[SPEC-002]]`
n'ouvre pas ce fichier : il crée un **fantôme**, une page vide qui porte
le bon nom. Et `links:` en texte brut ne fait aucune arête — seul un
`[[...]]` en fait une, y compris en frontmatter.

Et le lien porte le **nom de fichier**, pas l'ID seul : Obsidian résout
d'abord par nom de fichier, et l'alias — censé combler l'écart — ne le
comble pas de façon fiable. Le texte affiché après la barre reste l'ID.

Résultat : un graphe qui paraît écrit et qui n'existe que pour le hook.
Ça peut durer tout un projet sans que rien ne le signale.

Cet outil convertit :

    id: SPEC-002
    aliases:
      - SPEC-002
    links:
      - "[[ADR-007-un-titre|ADR-007]]"
      - "[[INT-005-un-autre|INT-005]]"

! L'alias en LISTE DE BLOC, jamais `aliases: [SPEC-002]`. La forme en
ligne est du YAML valide, et Obsidian ne la résout pas toujours — ça a
coûté un tour entier : le lien redevient un fantôme, et un fantôme masqué
ne laisse aucune trace à l'écran. La liste de bloc est ce qu'Obsidian
écrit lui-même quand on ajoute un alias par son interface.

    python3 outils/graphe_obsidian.py            # dit ce qui manque
    python3 outils/graphe_obsidian.py --ecrire   # convertit

Il est **idempotent** : relancé, il ne change rien. Il ne touche ni au
corps des fichiers, ni aux clés qu'il ne connaît pas, ni à leur ordre —
seuls `aliases` et `links` bougent.

! Il ne fait pas les deux autres moitiés du travail, qui ne s'automatisent
pas :

- **le coffre doit couvrir tout le dépôt.** Si les TASK vivent hors du
  dossier ouvert comme coffre, elles resteront des fantômes quoi qu'on
  écrive dans leur frontmatter.
- **`outils/liens_morts.py` doit passer.** C'est lui qui empêche la
  situation de revenir.
"""
import argparse
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

# Les dossiers qui portent le graphe. Un projet qui les nomme autrement
# les passe en argument.
DEFAUT_SCAN = ["product", "backlog"]

KINDS = ["IDEA", "SPEC", "BRIEF", "ADR", "DOM", "TRC", "SUG", "INT",
         "COPY", "PROMPT", "TASK"]
ID_RE = re.compile(r"^((?:" + "|".join(KINDS) + r")-\d{3})$")

# Hors graphe : ni ID, ni frontmatter attendus.
IGNORE_DIRS = {"grill", "legal"}


def _propre(v: str) -> str:
    """L'ID d'un lien, quelle qu'ait été sa forme d'écriture.

    ! La partie AFFICHÉE fait foi, pas la cible. `[[un-nom-invente|
    ADR-007]]` a une cible fausse et un ID juste : c'est ce qu'on écrit
    quand on tape un nom de fichier de mémoire au lieu de laisser l'outil
    le poser. En lisant l'ID, la passe suivante répare la cible toute
    seule — sinon le lien reste mort et il faut le corriger à la main,
    trois fois de suite.
    """
    v = v.strip().strip('"').strip("'").replace("[[", "").replace("]]", "").strip()
    return v.split("|", 1)[1].strip() if "|" in v else v


def convertir(txt: str, noms: dict[str, str] | None = None) -> tuple[str | None, str | None]:
    """(texte converti, ID) — ou (None, None) si le fichier n'est pas un objet.

    Rend le texte inchangé quand il est déjà à la bonne forme : c'est ce
    qui rend l'outil rejouable sans rien casser.
    """
    if not txt.startswith("---"):
        return None, None
    parts = txt.split("---", 2)
    if len(parts) < 3:
        return None, None
    _, front, corps = parts
    lignes = front.strip("\n").split("\n")

    ident = next((l.split(":", 1)[1].strip() for l in lignes if l.startswith("id:")), None)
    if not ident or not ID_RE.match(ident):
        return None, None

    liens: list[str] = []
    alias: list[str] = []
    gardees: list[str] = []
    collecte = None          # "links" | "aliases" | None

    for l in lignes:
        nu = l.strip()
        if collecte and nu.startswith("- "):
            if v := _propre(nu[2:]):
                (liens if collecte == "links" else alias).append(v)
            continue
        collecte = None

        for cle, panier in (("links:", liens), ("aliases:", alias)):
            if l.startswith(cle):
                val = l.split(":", 1)[1].strip()
                if val:
                    panier += [v for v in (_propre(x) for x in val.strip("[]").split(","))
                               if v]
                else:
                    # Une clé sans valeur ouvre une liste : les tirets suivent.
                    collecte = cle.rstrip(":")
                break
        else:
            gardees.append(l)

    # ! L'alias s'écrit en LISTE DE BLOC, pas en `aliases: [X]`. La forme
    # en ligne est du YAML valide et Obsidian ne la résout pas toujours —
    # un alias non résolu ne laisse aucune trace : le lien devient un
    # fantôme, et avec les fantômes masqués, l'arête disparaît sans un
    # mot. La liste de bloc est ce qu'Obsidian écrit lui-même.
    neuves: list[str] = []
    for l in gardees:
        neuves.append(l)
        if l.startswith("id:"):
            neuves.append("aliases:")
            neuves += [f"  - {a}" for a in dict.fromkeys([ident, *alias])]

    # Les liens en fin de bloc : une liste multi-lignes se lit mal au
    # milieu d'autres clés.
    # ! Le lien porte le NOM DE FICHIER, pas l'ID seul. Obsidian résout
    # d'abord par nom de fichier ; l'alias était censé combler l'écart et
    # ne le comble pas de façon fiable. Un lien non résolu ne proteste
    # pas — il ouvre une page vide, et le graphe se remplit de fantômes
    # qui ressemblent à des objets. Le texte affiché reste l'ID.
    noms = noms or {}
    if liens:
        neuves.append("links:")
        neuves += [f'  - "[[{noms[v]}|{v}]]"' if v in noms else f'  - "[[{v}]]"'
                   for v in dict.fromkeys(liens)]
    else:
        neuves.append("links: []")

    return "---\n" + "\n".join(neuves) + "\n---" + corps, ident


def parcourir(dossiers: list[str]):
    for nom in dossiers:
        base = RACINE / nom
        if not base.exists():
            continue
        for f in sorted(base.rglob("*.md")):
            if any(p in IGNORE_DIRS for p in f.parts):
                continue
            yield f


def main() -> int:
    a = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    a.add_argument("--ecrire", action="store_true",
                   help="convertir (sans lui, l'outil ne fait que dire)")
    a.add_argument("dossiers", nargs="*", default=DEFAUT_SCAN,
                   help=f"où chercher (défaut : {' '.join(DEFAUT_SCAN)})")
    args = a.parse_args()

    dossiers = args.dossiers or DEFAUT_SCAN

    # Première passe : qui est où. Un lien ne peut nommer un fichier
    # qu'une fois qu'on les connaît tous.
    noms: dict[str, str] = {}
    for f in parcourir(dossiers):
        _, ident = convertir(f.read_text(encoding="utf-8"))
        if ident:
            noms[ident] = f.stem

    a_changer: list[tuple[Path, str]] = []
    total, doublons, vus = 0, [], {}

    for f in parcourir(dossiers):
        txt = f.read_text(encoding="utf-8")
        neuf, ident = convertir(txt, noms)
        if ident is None:
            continue
        total += 1
        if ident in vus:
            doublons.append(f"{ident} — {vus[ident]} et {f.relative_to(RACINE)}")
        vus[ident] = f.relative_to(RACINE)
        if neuf != txt:
            a_changer.append((f, neuf))

    # ! Un ID en double casse l'alias : deux fichiers revendiquent la même
    # cible, et Obsidian en choisit un — silencieusement. Ça se règle à la
    # main, avant la conversion.
    if doublons:
        print(f"! {len(doublons)} ID(s) en double — à régler AVANT de convertir :\n")
        for d in doublons:
            print(f"  {d}")
        return 2

    if not a_changer:
        print(f"Graphe déjà à la forme Obsidian — {total} objet(s).")
        return 0

    if not args.ecrire:
        print(f"! {len(a_changer)} objet(s) sur {total} à convertir :\n")
        for f, _ in a_changer:
            print(f"  {f.relative_to(RACINE)}")
        print("\n  python3 outils/graphe_obsidian.py --ecrire")
        return 1

    for f, neuf in a_changer:
        f.write_text(neuf, encoding="utf-8")
    print(f"{len(a_changer)} objet(s) converti(s) sur {total}.\n"
          "\nIl reste deux choses qui ne s'automatisent pas :\n"
          "  → ouvrir le coffre sur la RACINE du dépôt, pas sur un sous-dossier\n"
          "  → python3 outils/liens_morts.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
