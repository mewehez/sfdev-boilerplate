"""Les règles de style qui ne s'appliquent à rien, et l'inverse.

! Ce contrôle existe à cause d'un défaut qui s'est produit **deux fois**,
à l'identique, à six mois d'écart : une règle écrite pour un sélecteur que
le code ne produit pas. La première fois c'était une classe renommée par
une bibliothèque ; la seconde, un attribut renommé par nous-mêmes en
retirant un mode.

Dans les deux cas la règle était juste, le code était juste, et
**l'affordance avait disparu en silence** — rien ne relie une déclaration
de style à son emploi réel, donc rien ne se plaint.

Ce que le contrôle rend :

- les **règles mortes** : un sélecteur de classe ou d'attribut que
  personne ne produit. C'est le cas grave — du style écrit qui ne
  s'applique à rien, et personne pour le dire.
- les **classes orphelines** : une classe posée dans le code et qui
  n'existe dans aucune feuille de style. Souvent une faute de frappe.

Il ne comprend pas le CSS et n'essaie pas : il lit les sélecteurs, lit les
littéraux de chaîne du code, et compare. C'est grossier, et c'est
suffisant pour attraper ce qu'aucune relecture n'attrape.

    python outils/styles_morts.py [dossier]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]

CODE = {".tsx", ".jsx", ".ts", ".js", ".vue", ".svelte", ".html", ".py"}
STYLES = {".css", ".scss"}
IGNORES = {"node_modules", ".next", ".venv", "dist", "build", "__pycache__"}

# Ce qui vient des bibliothèques et des navigateurs : on ne le possède pas.
PREFIXES_ETRANGERS = ("openseadragon", "leaflet", "mapbox", "swiper", "ol-",
                      "grecaptcha", "pac-", "js-")

CLASSE = re.compile(r"\.(-?[_a-zA-Z][\w-]*)")
ATTRIBUT = re.compile(r"\[data-([\w-]+)\s*[~^|$*]?=\s*[\"']([^\"']*)[\"']\]")
MOT = re.compile(r"[\w-]+")


def _fichiers(base: Path, extensions: set[str]) -> list[Path]:
    return [c for c in base.rglob("*")
            if c.suffix in extensions and not (set(c.parts) & IGNORES)]


def controler(base: Path) -> int:
    feuilles = _fichiers(base, STYLES)
    sources = _fichiers(base, CODE)
    if not feuilles:
        print("Aucune feuille de style — rien à contrôler.")
        return 0

    texte_code = "\n".join(f.read_text(errors="ignore") for f in sources)
    mots_code = set(MOT.findall(texte_code))

    mortes: list[str] = []
    declarees: set[str] = set()

    for f in feuilles:
        for ligne_no, ligne in enumerate(f.read_text(errors="ignore").split("\n"), 1):
            if "{" not in ligne and not ligne.rstrip().endswith(","):
                continue
            selecteur = ligne.split("{")[0]

            for nom in CLASSE.findall(selecteur):
                if nom.startswith(PREFIXES_ETRANGERS):
                    continue
                declarees.add(nom)
                if nom not in mots_code:
                    mortes.append(f"{f.relative_to(base)}:{ligne_no}  .{nom}")

            for attribut, valeur in ATTRIBUT.findall(selecteur):
                # L'attribut ET sa valeur doivent exister dans le code :
                # une règle sur `data-mode="oui"` ne vaut rien si plus
                # personne ne pose `data-mode`.
                # Le nom complet, `data-machin` : c'est sous cette forme
                # qu'il apparaît dans le code, jamais amputé de `data-`.
                if (f"data-{attribut}" not in mots_code
                        or (valeur and valeur not in mots_code)):
                    mortes.append(
                        f"{f.relative_to(base)}:{ligne_no}  [data-{attribut}=\"{valeur}\"]")

    # Les classes posées dans le code et absentes de toute feuille.
    orphelines: set[str] = set()
    for f in sources:
        texte = f.read_text(errors="ignore")
        # ! `className={classe}` ne cite AUCUNE classe : il en cite une
        # dont le nom est calculé, et le contrôle ne peut pas le savoir.
        # Il le signalait comme classe jamais déclarée — un contrôle qui
        # crie sur un motif React courant finit par ne plus être lu.
        texte = re.sub(r"className=\{\s*[_a-zA-Z][\w.]*\s*\}", "", texte)
        # ! `className={x ? "a" : "b"}` cite `a` et `b`, pas `x` : dans une
        # expression, seules les chaînes entre guillemets sont des classes.
        # Le contrôle prenait la condition pour une classe orpheline.
        citations = re.findall(r"className=[\"'`]([^\"'`]+)", texte)
        for expression in re.findall(r"className=\{([^}]*)\}", texte):
            # Une chaîne comparée — `etat === "fournie"` — n'est pas une
            # classe non plus : c'est une valeur, la classe vient après.
            citations.extend(re.findall(r"(?<![=!])\s*[\"'`]([^\"'`]+)[\"'`]",
                                        re.sub(r"[=!]==?\s*[\"'`][^\"'`]*[\"'`]", "", expression)))
        for citation in citations:
            for nom in citation.split():
                # Les fragments d'expression — ternaires, gabarits — ne
                # sont pas des classes. On ne garde que ce qui en a la
                # forme, sinon le contrôle crie sur du bruit et on cesse
                # de le lire.
                # Au moins trois caractères : en dessous, c'est du bruit
                # de gabarit, jamais un nom de composant.
                if not re.fullmatch(r"-?[_a-zA-Z][\w-]{2,}", nom):
                    continue
                if (not nom.startswith(PREFIXES_ETRANGERS) and nom not in declarees):
                    orphelines.add(nom)

    if not mortes and not orphelines:
        print(f"Styles cohérents — {len(declarees)} classes déclarées, "
              f"{len(feuilles)} feuille(s).")
        return 0

    if mortes:
        print(f"! {len(mortes)} règle(s) qui ne s'appliquent à rien :\n")
        for m in sorted(set(mortes)):
            print(f"  {m}")
        print()
    if orphelines:
        print(f"! {len(orphelines)} classe(s) posées et jamais déclarées :\n")
        for o in sorted(orphelines):
            print(f"  {o}")
        print()
    print("Une règle morte n'échoue pas : elle retire une affordance en\n"
          "silence. Retirer la règle, ou corriger le sélecteur.")
    return 1


if __name__ == "__main__":
    base = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else RACINE
    raise SystemExit(controler(base))
