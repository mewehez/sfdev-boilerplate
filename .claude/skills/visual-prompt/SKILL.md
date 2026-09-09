---
name: visual-prompt
description: Produit et trace les prompts de génération d'ASSETS —
  illustrations, images, logos, icônes, SVG, pictogrammes. Déclencher
  depuis copywriting ou depuis un designer de surface, ou sur "il faut
  une illustration pour", "génère un visuel", "il nous faut un logo".
  Le prompt est un artefact versionné, pas un jetable.
---

# Prompts visuels

## Pourquoi tracer
Un visuel régénéré six mois plus tard sans son prompt d'origine casse la
cohérence de l'app. Le prompt EST l'actif, l'image en est la sortie.

## Direction artistique — une seule fois par projet
Si product/assets/ART-DIRECTION.md n'existe pas, le créer avant tout
prompt (questions une à une) : palette, style, traitement humain,
niveau d'abstraction, ce qu'on ne veut jamais voir.
Tout PROMPT hérite de ce fichier — ne pas redéclarer le style à chaque fois.

## Les genres d'asset, et ce qui change entre eux

Le `genre` est obligatoire dans le frontmatter. Il commande le format de
sortie, l'outil, et ce qu'on vérifie à la réception.

| genre | sortie attendue | ce qu'on vérifie |
|---|---|---|
| `illustration` | image matricielle, ratio fixé | le sujet est situé, la culture est juste |
| `photo` | image matricielle | aucune personne réelle, aucune marque |
| `logo` | **SVG**, et une version monochrome | lisible à 16 px, tient en noir seul |
| `icone` | **SVG**, grille et épaisseur de trait fixées | cohérente avec les icônes déjà posées |
| `pictogramme` | SVG ou glyphe | comprise sans légende, sinon elle est décorative |
| `motif` / `texture` | SVG ou image répétable | pèse moins que ce qu'elle apporte |

`!` **Un logo et une icône ne se génèrent pas comme une image.** Les
modèles de diffusion rendent du flou vectorisable, pas du vecteur : le
prompt doit demander explicitement un SVG, ou décrire une forme
géométrique **construite** — nombre de traits, épaisseur, grille, angles
— pour qu'elle soit reproductible à la main si le rendu échoue.

`!` **Rien ne se pose sans passer par ici.** Un emoji en guise d'icône,
un carré gris en guise d'illustration, un `<svg>` improvisé dans un
composant : ce sont des décisions visuelles prises sans direction
artistique, et elles se voient toutes en même temps six écrans plus loin.

## Comment ça se fabrique aujourd'hui — et ce qui viendra

Aucune génération n'est automatisée. La skill **écrit le prompt**, le
propriétaire le colle dans l'outil de son choix, récupère le fichier et
le range. Le `PROMPT-nnn` note l'outil utilisé et le fichier obtenu.

La conséquence est une règle, pas une gêne : **le prompt doit être
copiable tel quel**, sans réécriture, sans variable à remplacer, sans
puce. Un prompt qu'il faut retoucher avant de le coller est un prompt
inachevé.

→ L'automatisation viendra quand un outil sera choisi ; le `PROMPT-nnn`
est déjà l'entrée de cette automatisation, et rien ne changera de ce qui
est écrit ici.

## Écriture

---
id: PROMPT-nnn
aliases:
  - PROMPT-nnn
title: <ce que l'image doit montrer>
status: draft | generated | retenu | rejeté
genre: illustration | photo | logo | icone | pictogramme | motif
links:
  - "[[COPY-nnn]]"
  - "[[SPEC-nnn]]"
outil: <modèle utilisé>
updated: AAAA-MM-JJ
---

## Emplacement
- <où l'asset apparaît, à quelle taille, quel ratio, sur quelle surface —
  téléphone, bureau, ou les deux>
- <la plus petite taille où il doit rester lisible>

## Rôle
- <ce que le lecteur doit comprendre ou ressentir — une ligne>

## Prompt
```
<le prompt exact, copiable tel quel, sans tiret ni puce>
```

## Négatif
```
<ce qu'on exclut>
```


## Variantes essayées
- v1 → <résultat, pourquoi écarté>
- v2 → <retenu>

## Fichier généré
- assets/<nom> — <date>

## Ce qu'on vérifie à la réception
- <selon le genre : lisibilité à la plus petite taille, tenue en
  monochrome, cohérence avec les assets déjà posés>

## Règles de contenu
- Sujets situés et concrets, jamais "business people in an office".
- Cohérence culturelle avec le persona : les lieux, les objets et les
  personnes représentés doivent correspondre à son contexte réel
  [DOM-nnn], pas à un stock photo occidental par défaut.
- Aucune personne réelle, aucune marque, aucun personnage sous licence.
- Si le visuel doit contenir du texte, l'écrire dans le prompt ET prévoir
  la retouche : les modèles ratent le texte.

## Interdits
- Générer sans PROMPT-nnn écrit d'abord.
- Réutiliser un prompt sans le lier au nouveau COPY.
- Supprimer une variante rejetée — c'est la mémoire de ce qui ne marche pas.
- Poser un emoji, un carré de couleur ou un SVG improvisé à la place d'un
  asset qui demande un métier. Écrire le PROMPT et laisser le trou en
  attendant : un trou se voit et se comble, un placeholder reste.
- Écrire un prompt qui demande une retouche avant d'être collé.