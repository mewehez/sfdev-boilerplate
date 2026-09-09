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

! Il ne regarde que le SOCLE — `CLAUDE.md`, `.claude/`, `outils/`. Pas
`product/`, pas `backlog/`, pas `src/`.

La raison est celle qui l'a fait crier : le jour où le produit est
légitimement entré dans un domaine voisin d'un projet passé, il a
signalé « FCFA », « mobile money » et « encaissement » dans un fait de
domaine sourcé — des mots que le produit a le DROIT d'employer, puisque
c'est le sien. Un produit nomme son domaine ; c'est le socle qui n'a pas
à le porter. Élargir la portée revenait à demander au produit de parler
de son métier sans ses mots.
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

# ! Le produit EN COURS, déclaré par lui-même.
#
# La liste ci-dessus ne grandit qu'après coup : elle porte les mots d'un
# projet fini, jamais ceux du projet qu'on écrit. Or c'est pendant qu'un
# projet se construit que son vocabulaire s'installe dans le socle — et à
# ce moment-là le contrôle est aveugle, par construction.
#
# Le socle ne peut pas deviner ces mots. Le projet, lui, les connaît :
# il les écrit dans `outils/vocabulaire-produit.txt`, un mot par ligne.
# Le jour où le projet se termine, ce fichier EST la rallonge à coller
# dans la liste ci-dessus, et le suivant repart d'un fichier vide.
VOCABULAIRE_PRODUIT = Path(__file__).resolve().parent / "vocabulaire-produit.txt"


def mots_du_produit() -> list[str]:
    if not VOCABULAIRE_PRODUIT.exists():
        return []
    return [l.strip().lower() for l in VOCABULAIRE_PRODUIT.read_text().splitlines()
            if l.strip() and not l.startswith("#")]

JOURNAL = "AMELIORATIONS.md"
EXAMINES = {".md", ".py", ".sh", ".json"}


# ! Ce qu'on n'a PAS écrit. Le contrôle porte sur le socle et sur le
# produit, pas sur les dépendances : une table Unicode d'`idna` contient
# `0xFCFA`, et le contrôle remontait « fcfa » depuis un fichier que
# personne ici n'a tapé. Un faux positif dans un contrôle de neutralité
# est plus grave qu'ailleurs — il est fait pour être lu rarement, donc
# chaque ligne qu'il sort doit valoir une lecture.
NON_ECRIT = {".git", "__pycache__", ".venv", "node_modules", ".next",
             "dist", "build", ".mypy_cache", ".pytest_cache", "site-packages"}


# Le socle, et rien d'autre. Le produit nomme son domaine ; c'est ici que
# ce vocabulaire ne doit pas s'installer.
SOCLE = ["CLAUDE.md", ".claude", "outils", "AMELIORATIONS.md"]

# ! Ce qui vit dans le socle sans en faire partie. Un persona EST le
# vocabulaire du produit — c'est sa raison d'être ; le signaler
# reviendrait à interdire au produit d'avoir des utilisateurs. Même chose
# pour la configuration de lancement, et pour `outils/produit/`.
HORS_SOCLE = ["persona", "launch.json", "produit"]


def fichiers():
    racines = [RACINE / n for n in SOCLE]
    for f in sorted(x for r in racines if r.exists()
                    for x in ([r] if r.is_file() else r.rglob("*"))):
        if any(h in f.as_posix() for h in HORS_SOCLE):
            continue
        if not f.is_file() or f.suffix not in EXAMINES:
            continue
        if any(p in NON_ECRIT for p in f.parts):
            continue
        # La liste des mots interdits en contient, par construction.
        if f.name == Path(__file__).name:
            continue
        yield f


def fuites():
    trouvees = []
    for f in fichiers():
        texte = f.read_text(encoding="utf-8", errors="ignore")
        interdits = (PARTOUT + mots_du_produit()
                     + ([] if f.name == JOURNAL else REGLES_SEULEMENT))
        for n, ligne in enumerate(texte.splitlines(), 1):
            for mot in interdits:
                # ! Frontières de mot, sinon « plancher » déclenche sur
                # « planche ». Un contrôle qui crie sur un mot légitime
                # finit par ne plus être lu — même défaut que
                # `styles_morts.py` sur les ternaires.
                #
                # ! Le pluriel reste attrapé (`s` ou `x` seuls) : la
                # première version bornait strictement et laissait passer
                # « planches », ce qui est PIRE que le faux positif
                # qu'elle corrigeait. Une correction se vérifie sur les
                # deux sens.
                if re.search(rf"(?<![\w-]){mot}(?:s|x)?(?![\w-])", ligne,
                             re.IGNORECASE | re.UNICODE):
                    rel = f.relative_to(RACINE)
                    trouvees.append((f"{rel}:{n}", mot, ligne.strip()[:78]))
    return trouvees


if __name__ == "__main__":
    t = fuites()
    if not t:
        # ! Le décompte dit ce qui est surveillé, mots du produit
        # compris : annoncer 17 alors qu'on en surveille 30 laisserait
        # croire que le fichier de vocabulaire n'est pas lu.
        print(f"Socle neutre — {len(PARTOUT) + len(REGLES_SEULEMENT) + len(mots_du_produit())} "
              f"termes surveillés.")
        sys.exit(0)
    print(f"! {len(t)} fuite(s) du vocabulaire d'un projet :\n")
    for ou, mot, ligne in t:
        print(f"  {ou}\n      « {mot} » — {ligne}\n")
    print("Généraliser, ou retirer le mot de la liste s'il est devenu")
    print("légitime. Un socle qui parle du domaine d'un produit le lègue.")
    sys.exit(1)
