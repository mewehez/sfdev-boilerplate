---
name: concevoir-une-page
description: Conçoit une page comme ce qu'elle est — des fonctionnalités
  ET une présentation. Fait proposer les fonctions par un agent, puis
  composer les DEUX surfaces par deux designers spécialisés, en
  parallèle. Déclencher sur "refais cette page", "conçois l'écran de…",
  "cette page mérite mieux", ou avant d'écrire une page qui compte.
---

# Concevoir une page

> Une page, c'est des **fonctionnalités** et une **présentation**.

Les deux se traitent séparément, et dans cet ordre. Mélanger les deux
produit le défaut le plus courant : on discute d'une couleur avant de
savoir ce que la page doit permettre, et on découvre la fonction
manquante une fois la maquette faite.

`!` Et la présentation se conçoit **deux fois**, pas une. Le téléphone et
le grand écran ne sont pas deux tailles : ce sont deux paradigmes — une
main contre un clavier, une interruption contre une session. Une seule
composition « adaptée » donne un produit plat des deux côtés.

---

## Quand

- Une page que l'utilisateur voit **avant de faire confiance** : entrée,
  inscription, accueil, page publique.
- Une page qu'on reprend parce qu'elle « fonctionne mais ne vaut rien ».
- Une page neuve qui portera plus de trois gestes.

Ne PAS l'utiliser pour un écran de plus dans un parcours établi
(`feature-build` suffit), ni pour trancher une forme unique
(`conception-adverse`).

---

## 1. Les fonctionnalités — ce que la page doit permettre

Avant toute forme, la liste de ce qui doit être **possible ici**. Deux
sources, dans cet ordre :

1. **Ce qui est déjà là** — lire le fichier de la page. Ce qu'elle
   permet aujourd'hui est le plancher, pas le plafond.
2. **Ce qui manque** — dispatcher `suggester` avec la question exacte :
   « que doit permettre cette page, au-delà de ce qu'elle permet
   aujourd'hui ? » Il rend trois à cinq options **matériellement
   différentes**, sans recommander.

`!` À ce stade, aucune forme. « Un lien vers l'aide » est une fonction ;
« un lien discret en bas à droite » est déjà une réponse de design.

Le propriétaire tranche la liste. Sa réponse l'emporte (`G2`).

---

## 2. La présentation — deux surfaces, deux agents, en parallèle

Dispatcher **ensemble** :

- `designer-telephone` — une main, un pouce, une interruption ;
- `designer-bureau` — pointeur, clavier, session, densité assumée.

Chacun reçoit **la même chose** : la liste des fonctions retenues, le
`DESIGN.md` du produit, et le contexte d'usage. Aucun ne reçoit la
composition de l'autre : deux compositions du même objet, pas une
composition et sa réduction.

Les deux lisent
`.claude/skills/design-direction/references/paradigmes-de-surface.md` —
les constantes physiques, les familles de motifs éprouvés, et la table
« quel design pour quel type d'application ».

---

## 3. Les assets — écrire les prompts, pas dessiner

Si une composition demande un logo, une icône, une illustration ou un
pictogramme, le designer **ne le dessine pas** et ne pose ni emoji ni
carré gris. Il écrit un `PROMPT-nnn` par la skill `visual-prompt`, avec
son `genre`, et le nomme dans sa sortie.

Aujourd'hui la génération est manuelle : le propriétaire colle le prompt
dans l'outil de son choix et range le fichier. D'où la règle : **le
prompt est copiable tel quel**.

---

## 4. La critique — après, jamais avant

Une fois une composition retenue et écrite :

- `design-critic` la confronte au `DESIGN.md` — contexte vierge ;
- `directeur-artistique` refuse le tiède, et doit citer un produit précis
  qui fait mieux.

`!` Ne pas les convoquer sur une proposition. Ils jugent ce qui existe.

---

## 5. Écrire — sinon rien de tout ça n'a eu lieu

- Les **fonctions non retenues** partent en `IDEA` — `origine: agent`,
  `contexte: concevoir-une-page`.
- Les **deux compositions** entrent dans le journal de `DESIGN.md`, avec
  ce que chaque surface porte et ce qu'elle ne porte pas.
- Les composants introduits entrent dans le **registre** de `DESIGN.md`,
  avec leur ligne « ce qu'il ne doit jamais porter ».
- Les `PROMPT-nnn` sont écrits, même si aucun asset n'est encore généré.

---

## Mesurer avant de regarder

La règle du socle vaut ici plus qu'ailleurs : une capture se mesure avant
de se regarder. Aux **deux largeurs**, et sur la page réelle :

- aucun débordement horizontal à 375 px ;
- un seul bouton principal visible par largeur ;
- la hauteur de page, et ce qui tient au-dessus du pli ;
- la plus petite taille de texte réellement rendue.

Une composition qu'on n'a pas mesurée n'est pas livrée.

---

## Interdits

- Traiter la forme avant les fonctions.
- Donner à un designer la composition de l'autre surface.
- Concevoir une seule surface et « adapter » l'autre.
- Laisser un designer dessiner un asset qui demande un métier.
- Convoquer les critiques sur une proposition plutôt que sur un écran.
