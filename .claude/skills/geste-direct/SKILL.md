---
name: geste-direct
description: La conception d'interaction d'un écran — ce qui se manipule,
  ce qui s'explique, ce qui se retire. Déclencher avant d'écrire un écran
  qui contient un geste, et sur "l'interface n'est pas claire", "on ne
  trouve pas", "ça ne donne pas envie", "trop de boutons", "il faut
  expliquer". Complète design-direction, qui traite la forme ; celle-ci
  traite le geste.
---

# Le geste avant la commande

Un écran qui a besoin d'être expliqué est un écran raté. Ce n'est pas une
opinion : les utilisateurs **sautent le texte statique** — ils cherchent
l'objet sur lequel agir. Une phrase d'aide n'est donc pas un correctif,
c'est un pansement posé sur un défaut de forme, et le défaut reste.

D'où la règle qui commande toutes les autres :

> **Quand une interaction n'est pas évidente, on redessine la forme. On
> n'ajoute pas une phrase.**

La tentation inverse est immense, parce que la phrase coûte une minute et
la forme coûte une heure. C'est exactement pour ça qu'il faut une règle :
sans elle, on prend toujours la minute.

---

## Les sept règles

Chacune est **vérifiable par quelqu'un d'autre**. Une règle qu'on ne peut
pas mettre en défaut ne contraint personne.

### 1. On manipule l'objet, pas ses commandes

Agir sur la chose elle-même donne le sentiment d'être aux commandes ; agir
sur des boutons qui agissent sur la chose l'éloigne. Ce bénéfice l'emporte
largement sur les inconvénients de la manipulation directe.

**Le test** : lister les commandes visibles de l'écran. Pour chacune,
nommer le geste natif qu'elle double — pincer, double-taper, glisser,
maintenir, faire défiler. Toute commande qui en double un se justifie par
écrit, ou disparaît.

`!` Une commande garde sa place quand le geste natif **n'existe pas sur la
cible visée** — pas de pincement à la souris, pas de survol au doigt. La
justification écrite dit laquelle, et pour qui.

### 2. Un mode est une dette

« Appuyer sur *activer*, puis faire la chose » coûte un geste, une
découverte, et un état à sortir. Chercher la version sans mode **avant**
d'accepter celle-là.

**Le test** : compter les états dans lesquels le même toucher fait deux
choses différentes. Chacun se justifie ou se supprime.

### 3. Là où le doigt se pose, la réponse naît

Ce qui découle d'un toucher apparaît **à cet endroit**, pas ailleurs sur
la page. Un éditeur qui s'ouvre loin du point désigné oblige l'œil à
sauter, et sur un petit écran il s'ouvre hors du champ visible — donc
« il ne s'est rien passé ».

**Le test** : pour chaque toucher, mesurer la distance entre le point
touché et l'endroit où la réponse apparaît. Si elle dépasse la hauteur
visible, c'est faux.

`!` Le correctif classique — faire défiler la page jusqu'à la réponse —
traite le symptôme et confirme le défaut. Le noter comme tel.

### 4. Aucune phrase d'instruction dans un écran

Pas de « touchez X pour Y », pas de « ces boutons servent à ». Une phrase
nécessaire est **l'aveu d'une forme ratée**.

**Le test** : relever chaque phrase de l'écran qui explique comment s'en
servir. Pour chacune, écrire la forme qui la rendrait inutile. Si aucune
forme n'y arrive, garder la phrase **et l'inscrire dans la TASK comme un
défaut**, pas comme une solution.

Ne sont pas des instructions, et restent légitimes : ce qu'on **attend**
de l'utilisateur, la conséquence d'un geste irréversible, et ce que le
produit ne fait pas.

### 5. Le retour est continu, pas numérique

Un nombre qui monte dit « ça tourne ». Une forme continue dit **ce qui se
passe**. Sur une capture en cours, une onde rend le silence lisible :
rien dans l'onde, il n'y a rien à entendre — et non « c'est cassé ».

**Le test** : lister les retours de l'écran. Chacun qui est un compteur,
un pourcentage ou un texte d'état se demande s'il existe une forme
continue équivalente.

### 6. Compter les commandes visibles

Si elles sont plus nombreuses que les gestes qu'elles remplacent, l'écran
est du décor autour d'un objet.

**Le test** : le rapport commandes / gestes. Au-dessus de 1, retirer.

### 7. Nommer le geste principal, et compter ses touchers

Chaque écran a **un** geste pour lequel il existe. Si ce n'est pas le
moins cher de l'écran, l'écran est faux.

**Le test** : l'écrire noir sur blanc — « le geste principal de cet écran
est X, il coûte N touchers ». Comparer avec le geste secondaire le moins
cher.

---

## Ce qu'on regarde chez les autres, et comment

Un écran ne se conçoit pas de mémoire. Avant d'en dessiner un, passer par
la skill `references-croisees` : elle impose des exemples **hors du
domaine**, et l'écriture de ce que les concurrents directs font mal.

Le raccourci fautif est de s'aligner sur les produits les plus proches.
Quand ceux-là sont mauvais — c'est fréquent dans les métiers où le
logiciel est acheté par quelqu'un qui ne s'en sert pas — s'aligner revient
à **copier leurs défauts** en croyant faire son métier.

---

## La sortie

Avant d'écrire l'écran, rendre ceci — court, et vérifiable après coup :

```
Geste principal : <lequel>, <N> touchers
Commandes visibles : <N>, dont <N> qui doublent un geste natif
Modes : <lesquels, ou aucun>
Phrases d'instruction : <lesquelles, ou aucune>
Retours continus : <lesquels>  |  numériques : <lesquels, et pourquoi>
Références : <celles de references-croisees>
```

Après l'écran, `design-critic` reprend cette table et la vérifie contre
le code. C'est ce qui empêche la table d'être une intention.

---

## Interdits

- **Ajouter une phrase explicative pour clore un problème d'interaction.**
  C'est le défaut que cette skill existe pour empêcher.
- Justifier une commande par « c'est plus découvrable » sans nommer la
  cible qui n'a pas le geste natif.
- Rendre une sortie où « geste principal » est au pluriel. Un écran, un
  geste.
- Traiter cette skill comme un contrôle final. Elle se fait **avant**, et
  ce qu'elle produit est vérifié après.
