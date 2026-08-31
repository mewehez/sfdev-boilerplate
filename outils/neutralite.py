#!/usr/bin/env python3
"""Le socle porte-t-il encore le vocabulaire d'un projet passé ?

Un socle s'écrit PENDANT un projet. Ses règles naissent de frictions
réelles, et une friction réelle a un domaine — le premier produit finit
donc par teindre le socle : ses mots, ses exemples, son nom. Le socle
suivant hérite alors d'un vocabulaire qui n'est pas le sien.

Ce contrôle ne devine pas les fuites à venir : personne ne connaît le
domaine du prochain projet. Il garantit qu'une fuite **trouvée une fois
ne revient pas** — c'est le même pari que partout ailleurs ici : une
exemption écrite vaut mieux qu'une vigilance espérée.

    python3 outils/neutralite.py        # 0 si le socle est neutre

Quand une fuite est trouvée à la main, on ajoute son mot ici. La liste
grandit ; c'est le signe qu'elle sert.
"""
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]

# Le journal raconte des défauts réels : il a le droit d'être concret,
# mais pas de nommer un produit. Les deux règles diffèrent, donc les
# deux listes aussi.
PARTOUT = [
    # noms de produits déjà passés par ce socle
    "paymex",
    # un domaine qui s'est infiltré une fois : l'argent comme CATÉGORIE.
    # En exemple dans une liste, il reste légitime — d'où l'ancrage.
    r"règle d'argent", r"invariant d'argent", r"décide de l'argent",
    r"logique qui décide de l'argent",
    # vocabulaire d'un produit de paiement
    "mobile money", "fcfa", "t-money", "flooz", "double débit",
    "encaissement", "encaisser", "commerçant", "marchand",
]

# Hors du journal, les règles doivent viser la catégorie, pas un domaine.
REGLES_SEULEMENT = ["réconciliation", "solde d'un compte", "opérateur mobile"]

JOURNAL = "AMELIORATIONS.md"
EXAMINES = {".md", ".py", ".sh", ".json"}


def fichiers():
    for f in sorted(RACINE.rglob("*")):
        if not f.is_file() or f.suffix not in EXAMINES:
            continue
        if any(p in {".git", "__pycache__"} for p in f.parts):
            continue
        # La liste des mots interdits en contient, par construction.
        if f.name == Path(__file__).name:
            continue
        yield f


def fuites():
    trouvees = []
    for f in fichiers():
        texte = f.read_text(encoding="utf-8", errors="ignore")
        interdits = PARTOUT + ([] if f.name == JOURNAL else REGLES_SEULEMENT)
        for n, ligne in enumerate(texte.splitlines(), 1):
            for mot in interdits:
                if re.search(mot, ligne, re.IGNORECASE):
                    rel = f.relative_to(RACINE)
                    trouvees.append((f"{rel}:{n}", mot, ligne.strip()[:78]))
    return trouvees


if __name__ == "__main__":
    t = fuites()
    if not t:
        print(f"Socle neutre — {len(PARTOUT) + len(REGLES_SEULEMENT)} "
              f"termes surveillés.")
        sys.exit(0)
    print(f"! {len(t)} fuite(s) du vocabulaire d'un projet :\n")
    for ou, mot, ligne in t:
        print(f"  {ou}\n      « {mot} » — {ligne}\n")
    print("Généraliser, ou retirer le mot de la liste s'il est devenu")
    print("légitime. Un socle qui parle du domaine d'un produit le lègue.")
    sys.exit(1)
