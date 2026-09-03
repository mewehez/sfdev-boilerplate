---
name: page-produit
description: Écrit ou resserre la page qui présente le produit à quelqu'un
  qui ne le connaît pas. Déclencher sur "la landing", "la page d'accueil",
  "la page de présentation", "c'est trop long", "personne ne lit".
  Ne vend que ce qui tourne.
---

# La page qui présente le produit

Le défaut par défaut n'est pas d'en dire trop peu. C'est d'en dire trop.

Une page produit écrite par quelqu'un qui connaît son produit contient
tout ce qu'il aimerait qu'on sache. Une page produit lue par quelqu'un
qui ne le connaît pas contient ce qu'il a le temps de lire. Ce n'est pas
la même page, et c'est la seconde qu'il faut écrire.

---

## Le chiffre qui commande

**Le temps médian passé sur une page de ce genre est d'environ une demi-
minute.** Ce qui est au-dessus de la ligne de flottaison reçoit la
grande majorité de l'attention ; ce qui est en dessous, presque rien.

Écrire trois mille mots ne fait pas lire trois mille mots. Ça fait partir
plus tôt : chaque écran de texte supplémentaire est un écran où
quelqu'un décide qu'il n'a pas le temps.

Si le projet a mesuré ces chiffres pour son domaine, ils sont en `DOM`.
Sinon, chercher une fois, écrire le `DOM`, et s'en servir.

---

## La règle, et elle est unique

> **Une idée = un titre + une phrase.**

Ce qui ne tient pas dans cette forme n'est pas un argument : c'est une
note interne. Elle a sa place dans `product/`, pas sur la page.

Conséquences directes, et elles surprennent :

- **Pas de citations de recherche.** Les paroles d'utilisateurs, réels ou
  simulés, sont de la matière de conception. Le visiteur ne sait pas ce
  qu'est un persona et n'a pas à l'apprendre. Elles pèsent lourd et ne
  lui disent rien.
- **Pas d'explication du raisonnement.** *Pourquoi* on a fait ce choix
  intéresse l'équipe. Le visiteur veut savoir ce que ça change pour lui.
- **Pas de liste de dix.** Trois. Au-delà, on ne lit plus, on survole —
  et survoler dix items donne moins qu'en lire trois.

---

## Ce qu'on écrit, dans l'ordre

1. **L'en-tête** — ce que le produit fait, en une phrase qui pourrait
   être dite à voix haute. Un appel à l'action **visible sans défiler**.
   Et une **preuve visuelle** : le produit lui-même, montré. Pas une
   métaphore, pas une illustration abstraite — l'écran réel.
2. **Trois choses que ça fait.** Titre + une phrase.
3. **Trois choses par public supplémentaire**, s'il y en a un. Chaque
   section dit **à qui elle parle**, sinon les deux publics lisent la
   moitié qui n'est pas la leur et repartent.
4. **Ce que le produit ne fait pas** — une phrase, pas un bloc. En bloc,
   ça se lit comme une clause juridique et personne ne la lit.
5. **Le dernier appel.** Rien autour.

---

## La preuve visuelle

L'en-tête montre le produit. Deux façons, et la première est meilleure :

- **Une réplique en HTML**, faite avec les vrais composants. Elle ne
  vieillit pas — quand le produit change, elle change avec — et elle ne
  coûte aucune image à charger.
- Une image, si le sujet ne se compose pas en HTML.

! **Ne jamais dessiner soi-même ce qui demande un métier.** Un plan
d'architecte, un schéma d'installation, un tracé technique : quatre
rectangles ne font pas un plan, et un visiteur du métier le voit en une
seconde. Ce faux ne coûte pas rien : il dit que le produit n'a pas été
fait par quelqu'un qui connaît le sujet.

Dans ce cas : écrire un `PROMPT-nnn` avec la skill `visual-prompt`, et le
**demander**. Un blanc assumé vaut mieux qu'un faux.

---

## On ne vend que ce qui tourne

Une feature annoncée et absente se paie deux fois : à l'essai, et dans ce
que le visiteur croira des autres annonces.

Avant d'écrire une ligne : lire `src/`. Ce qui n'y est pas ne s'écrit pas,
même au futur, même « bientôt ».

Si le produit exclut délibérément quelque chose que ses utilisateurs
craignent qu'il fasse, **le dire**. C'est souvent la phrase qui rassure le
plus, et elle ne coûte qu'une ligne.

---

## Mesurer avant de rendre la main

Compter, ne pas estimer :

- **le nombre de mots visibles** de la page ;
- **le nombre d'écrans à défiler** — `scrollHeight / innerHeight` ;
- que le **titre, l'appel et la preuve** sont au-dessus du pli, sur un
  écran de bureau **et** sur un téléphone.

Deux écrans, c'est bien. Au-delà de trois, quelque chose est une note
interne déguisée.

## Sortie — ≤ 5 bullets
## Page — <N mots, N sections, N écrans à défiler>
## Au-dessus du pli — <ce qui y est>
## Ce qu'on ne vend pas — <ce qui est exclu, et qui est dit>
## ? Visuels demandés — <les PROMPT-nnn écrits, s'il y en a>

---

## Interdits
- Écrire plus de trois items dans une liste.
- Citer un utilisateur, réel ou simulé.
- Expliquer un choix de conception.
- Annoncer ce qui n'est pas dans `src/`.
- Dessiner soi-même un visuel qui demande un métier.
- Rendre la main sans avoir compté les mots et les écrans.
