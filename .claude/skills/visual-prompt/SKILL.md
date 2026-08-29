---
name: visual-prompt
description: Produit et trace les prompts de génération d'images et
  d'illustrations. Déclencher depuis copywriting, ou sur "il faut une
  illustration pour", "génère un visuel". Le prompt est un artefact
  versionné, pas un jetable.
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

## Écriture

---
id: PROMPT-nnn
title: <ce que l'image doit montrer>
status: draft | generated | retenu | rejeté
links: [COPY-nnn, SPEC-nnn]
outil: <modèle utilisé>
updated: AAAA-MM-JJ
---

## Emplacement
- <où l'image apparaît, à quelle taille, quel ratio>

## Rôle
- <ce que le lecteur doit comprendre ou ressentir — une ligne>

## Prompt
- <le prompt exact, copiable tel quel>

## Négatif
- <ce qu'on exclut>


## Variantes essayées
- v1 → <résultat, pourquoi écarté>
- v2 → <retenu>

## Fichier généré
- assets/<nom> — <date>

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