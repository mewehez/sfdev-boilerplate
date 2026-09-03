---
name: conception-adverse
description: Fait concevoir une forme par un agent et attaquer par un
  autre, avant d'écrire une ligne. Déclencher quand la forme n'est pas
  évidente et qu'elle sera chère à défaire — un modèle de données, une
  navigation, un geste irréversible — et sur "imagine un meilleur
  système", "comment on devrait faire", "trouve la bonne forme".
---

# Concevoir contre quelqu'un

Une conception faite seul converge vers la première idée. Non pas parce
qu'elle est bonne, mais parce que chaque minute passée dessus la rend
plus coûteuse à abandonner — et qu'à la fin on ne compare plus rien : on
justifie.

Deux agents, deux rôles opposés, **contexte vierge chacun**. Le second ne
reçoit que la proposition, jamais la conversation qui l'a produite : il
ne doit pas hériter des raisons.

---

## Quand

- La **forme** n'est pas évidente : plusieurs manières de faire tiennent
  debout, et le choix engage.
- Ce qui est choisi est **cher à défaire** — un modèle de données, une
  navigation, un geste qu'on ne peut pas reprendre.
- Une correction a déjà été reprise deux fois. Le troisième essai n'est
  pas un troisième essai : c'est le signe qu'on cherche dans le mauvais
  espace.

Ne PAS l'utiliser pour un écran de plus, une couleur, un libellé. Ça
coûte deux agents et un tour : c'est cher pour ce qui se corrige en
regardant.

---

## La procédure

### 1. Écrire le problème, pas la solution

Une phrase, et elle ne contient aucun nom de composant. « Choisir la
version qu'on regarde » est un problème ; « mettre un menu déroulant »
est déjà une réponse.

Y joindre : ce qui existe déjà, ce qui ne doit pas casser, et les
contraintes réelles du terrain. Le concepteur ne devine pas.

### 2. `concepteur` — au moins trois formes

Dispatché avec le problème et rien d'autre. Il rend **trois formes au
minimum**, dont une qu'il juge mauvaise mais défendable.

`!` Une seule proposition n'est pas un choix, c'est une décision déguisée.
Deux dont une en épouvantail non plus.

Chaque forme dit **ce qu'elle sacrifie**. Une forme sans sacrifice est
mal décrite, pas parfaite.

### 3. `contradicteur` — attaquer la plus forte

Il reçoit les formes, pas la conversation. Il attaque **celle qui semble
gagner**, pas la plus faible — démolir l'épouvantail ne fait avancer
personne.

Ce qu'il doit produire pour chaque objection :
- un **scénario d'échec concret** — des données, un geste, un moment ;
- et **ce qu'il ferait à la place**. Sans ça il ne contredit pas, il
  bloque.

`!` « C'est compliqué » n'est pas une objection. Compliqué pour qui, à
quel moment, et mesuré comment.

### 4. Trancher — un tour, deux au maximum

Au-delà de deux allers-retours, on n'affine plus : on tourne. Trancher
avec ce qu'on sait.

La sortie n'est **pas un consensus** : c'est une décision, avec ce
qu'elle sacrifie écrit en toutes lettres, et la question qui reste
ouverte s'il en reste une.

---

## La sortie

```
## Le problème        (une phrase, sans nom de composant)
## Les formes         (≥ 3, chacune avec son sacrifice)
## Ce qui a été attaqué, et ce qui a tenu
## La décision        (et ce qu'elle sacrifie)
## ? Ce qui reste ouvert
```

Elle va dans `product/grill/`, hors graphe. Ce qui en découle prend un ID
— ADR si une décision structurante est prise, SPEC si la forme est
arrêtée, IDEA si le verdict est « pas maintenant ».

---

## Interdits

- Lancer le contradicteur sur une seule forme. Il n'a rien à comparer.
- Lui donner le raisonnement du concepteur. Il doit juger la forme, pas
  l'histoire de la forme.
- Accepter une objection sans scénario d'échec, ou sans contre-proposition.
- Conclure « les deux se valent ». Si c'est vrai, prendre la moins chère
  à défaire et l'écrire.
- Faire trois tours. Le troisième n'apporte que de la fatigue.
