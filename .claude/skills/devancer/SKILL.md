---
name: devancer
description: Fait proposer ce que personne n'a demandé par un agent, et
  juger la plausibilité par un autre. Déclencher à la fin d'une tranche,
  sur "propose quelque chose qu'on n'a pas demandé", "qu'est-ce qui
  manquerait d'ambition ici", "devance", ou quand un jalon est atteint et
  que la suite est ouverte.
---

# Devancer la demande

Un produit qui ne fait que ce qu'on lui a demandé reste plat. Personne ne
demande ce qu'il ne sait pas encore nommer : on obtient des correctifs,
des commodités, et jamais la chose dont l'utilisateur dira six mois plus
tard qu'il ne s'en passerait plus.

Le risque symétrique est connu, et il ne se traite pas en s'interdisant
de proposer : il se traite en **faisant juger la proposition par
quelqu'un d'autre**, sur une échelle fermée, avec obligation de nommer
l'empêchement.

Deux agents, deux rôles opposés, **contexte vierge chacun**. Le second ne
reçoit que les propositions, jamais la conversation qui les a produites.

`!` Ce n'est pas `feature-scout`. Celle-là **déduit** du produit ce qui
lui manque — un trou dans un parcours, une conséquence non traitée. Elle
répond à « qu'est-ce qui manque ». Ici on répond à « qu'est-ce que
personne n'a imaginé », et la réponse n'est pas dans le produit.

---

## Quand

- **À la fin d'une tranche**, avant d'ouvrir la suivante. C'est le moment
  où le produit vient de changer, où la matière est fraîche, et où
  personne n'a encore d'avis.
- Quand la file de grill ne porte plus que des commodités.
- Quand l'utilisateur le demande — et quand il ne le demande pas depuis
  longtemps, ce qui est le vrai signal.

Ne PAS l'utiliser pour trancher une forme (`conception-adverse`), pour
débloquer une question posée (`suggester`), ni pour combler une file vide
avec du déductible (`feature-scout`).

---

## La procédure

### 1. Écrire le terrain, pas la question

Le devanceur ne devine pas. Lui donner, en une page :

- **ce que le produit stocke déjà** — la liste des tables ou des objets.
  C'est la liste de ce qu'il sait, et c'est la matière première ;
- **qui le touche**, tous rôles confondus, y compris ceux qui ne s'y
  connectent pas ;
- **ce qui vient d'être construit**, et ce que ça a rendu possible ;
- **les refus écrits** — les « ce que le produit ne fera pas » ;
- **les contraintes réelles** du terrain, avec leur DOM.

`!` Ne pas lui dire ce qu'on espère. Une attente transmise revient
toujours en proposition, et on croit avoir eu une idée.

### 2. `devanceur` — cinq à sept propositions

Dispatché avec le terrain et rien d'autre. Deux au moins doivent
déranger ; il le dit lui-même, à la fin.

### 3. `epreuve-du-reel` — un verdict par proposition

Dispatché avec **les propositions seules**. Il rend `déjà attendu`,
`plausible`, `risqué` ou `farfelu`, et ne peut tuer qu'en citant un
empêchement d'une liste fermée : un fait établi contredit, un ADR
contredit, une ressource que le terrain n'a pas, un tiers qui n'existe
pas, un volume qui n'arrivera pas, un risque que le produit refuse.

« Personne ne l'a demandé » et « c'est ambitieux » ne sont pas des
empêchements. C'est écrit dans son fichier, et c'est le cœur du
dispositif.

### 4. Rendre à l'humain — sa réponse l'emporte

Présenter le tableau complet : proposition, verdict, pari. **Ne pas
recommander.** Le propriétaire du produit tranche, et son avis l'emporte
sur les deux agents (`G2`).

    | # | proposition | verdict | le pari |
    |---|---|---|---|

    ! Ce que je garderais en premier — <celle du critique, pas la tienne>
    → Tu en retiens laquelle ?

### 5. Écrire — avant de proposer quoi que ce soit d'autre

Rien de tout ça n'existe tant que ce n'est pas écrit.

- **La séance** : `product/grill/AAAA-MM-JJ-devancer-<sujet>.md`. Elle
  porte les propositions **entières**, les verdicts, et les empêchements
  cités. Une proposition tuée reste lisible avec sa raison : c'est ce qui
  évite de la reproposer dans six mois.
- **Une IDEA par proposition qui n'est pas `farfelu`** —
  `origine: agent`, `contexte: devancer`, `status: raw`. Y compris celles
  que l'utilisateur ne retient pas : capturer coûte trois lignes, perdre
  coûte de retrouver.
- **Les `farfelu` ne s'écrivent pas en IDEA** — elles vivent dans la
  séance, avec leur empêchement et la version réduite qui survivrait.
- La retenue part en `feature-build` si la phase est `local`, ou en
  `idea-grill` si elle est chère à défaire.

---

## Ce qui rend la séance vérifiable plus tard

La contrepartie de la licence est fixe : **on s'autorise à devancer, à
condition de regarder ensuite ce qui est utilisé.** Un produit qui
devance sans jamais relire ce qui sert accumule de la profondeur que
personne n'ouvre. Une proposition retenue ici doit donc porter, dans sa
TASK,
une ligne « ce qu'on observera » — pas une métrique de vanité, un fait
observable : quelqu'un l'a ouvert, ou personne.

Sans ça, devancer devient une licence de construire au hasard, et la
critique n'aura servi qu'à se donner raison.

---

## Interdits

- Lancer le critique dans le même contexte que le proposeur.
- Transmettre au devanceur ce qu'on espère lire.
- Retenir une proposition sans écrire sa séance.
- Traiter `risqué` comme un refus. C'est un feu vert avec son pari écrit.
- Trancher à la place de l'humain quand il est là.
