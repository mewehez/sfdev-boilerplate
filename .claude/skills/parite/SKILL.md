---
name: parite
description: Vérifie qu'un port dit tout ce que la source dit — inventaire
  mécanique des écrans et des gestes, puis table de parité tenue par un
  test. Déclencher sur "il manque des features dans l'app", "est-ce que
  tout est porté", "vérifie la parité", avant de déclarer un port fini.
---

# Parité du port

## Le défaut que cette skill existe pour empêcher
Un port se fait écran par écran, de mémoire. On porte ce qu'on a sous les
yeux, et **on ne voit pas ce qu'on ne regarde pas**. Le trou ne se
manifeste ni à la compilation, ni à l'ouverture des écrans portés : il se
manifeste le jour où quelqu'un cherche un réglage et ne le trouve pas.

La mémoire est exactement l'outil qui a échoué. Donc :

> **L'inventaire se dérive de la source. Jamais de tête.**

## 1. Dériver la surface, mécaniquement

La source de vérité expose une surface énumérable. Selon la pile :

- application web : les **routes** déclarées, et les **gabarits**
- API : les chemins du routeur
- application native : les écrans enregistrés dans la navigation

L'énumérer avec un script — `grep`, un parcours d'AST, ce qui marche.
Pas à la main : une liste écrite à la main a les mêmes trous que la
mémoire qui l'a écrite.

Pour chaque écran, extraire **ce qu'on peut y faire**, pas ce qu'il
montre : les formulaires et leur cible, les boutons, les liens vers un
autre écran. Un geste est ce qui se perd ; un pixel se rattrape.

Coller le script dans la TASK. Il resservira au port suivant.

## 2. Écrire la table de parité

Dans `product/assets/PARITE.md`. Une ligne par écran ou par geste de la
source, trois colonnes :

| source | port | état |
|---|---|---|
| `/profil` · changer d'avatar | `EcranProfil` | porté |
| `/reconciliation` · simulateur | — | hors périmètre — outil de démonstration, le web le garde |

Deux états, pas trois :
- **porté** — et on dit où
- **hors périmètre — <la raison, en toutes lettres>**

Il n'y a pas d'état « à faire » : un geste non porté sans raison écrite
est un **oubli**, et un oubli n'a pas sa place dans un document. S'il
doit être porté, il devient une TASK ; s'il ne doit pas l'être, la
raison s'écrit.

## 3. Rendre l'oubli impossible

Une prose se relit ; un test se heurte. Écrire un test qui :

1. réénumère la surface de la source, avec le même script ;
2. lit `PARITE.md` ;
3. **échoue** si une entrée de la source n'y figure pas ;
4. **échoue** si un « hors périmètre » n'a pas de raison.

C'est la seule partie qui survit à l'oubli de cette skill. Un nouvel
écran ajouté à la source fera tomber le test le jour même, avant que
personne n'ait à s'en souvenir.

## 4. Combler

Ce qui reste sans ligne devient des TASK, dans l'ordre où un utilisateur
s'en sert — pas dans l'ordre du fichier. Un réglage que personne
n'ouvre passe après un geste du parcours principal.

---

## Interdits
- Dresser l'inventaire de mémoire, ou en relisant le port. On part de la
  **source**, sinon on retrouve exactement ce qu'on a déjà porté.
- Un « à faire » dans la table. C'est une TASK ou une raison écrite.
- Déclarer un port fini sans table de parité verte.
- Inventer une divergence sans l'écrire. Si le port range un geste
  ailleurs que la source, la ligne le dit — sinon la relecture suivante
  le comptera comme manquant.

## Sortie — ≤ 8 bullets
## Surface — <n> écrans, <n> gestes, dérivés par <le script>
## Portés — <n>
## Hors périmètre — <n>, chacun avec sa raison
## Trous — <la liste, devenue des TASK>
## Le test — <chemin> : il échoue si la source grandit sans la table
