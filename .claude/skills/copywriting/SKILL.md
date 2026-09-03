---
name: copywriting
description: Produit les textes destinés à l'utilisateur final — landing,
  onboarding, messages d'erreur, emails, app store. Déclencher sur
  "écris la landing", "le texte de", "copy".
---

# Copywriting

! **Ce n'est PAS la skill de la page qui présente le produit.** Celle-ci
écrit pour quelqu'un qui **se sert déjà** du produit : messages, libellés,
courriels. Là, la précision paie. La page qui s'adresse à quelqu'un qui ne
connaît rien et n'a pas le temps obéit à la contrainte inverse — c'est
`page-produit`, et elle interdit ce qu'on encourage ici.

## Entrée — aucun refus

En régime `exploration` (défaut) : **écrire**. Aucun persona requis,
aucune SPEC requise, aucune interview requise.

- Sans persona : estampiller `confiance: miroir` et le dire en une ligne.
  Un texte écrit sans avoir parlé à personne n'est pas interdit, il est
  déclaré. La première chose à faire vérifier par un vrai utilisateur se
  note en tête du COPY.
- Les autres régimes ajoutent des exigences de persona :
  `.claude/optional/RIGUEUR.md`.

## La seule règle qui ne cède pas : ne rien promettre qui n'existe

Le copy promet un comportement, il ne l'invente pas. Mais la référence
n'est pas une SPEC — la plupart des projets n'en ont pas, et refuser
pour ça bloquerait un texte sur un produit qui tourne déjà.

Vérifier contre ce qui existe **vraiment**, dans cet ordre :
`src/` (le code), les TASK `done`, les ADR, product/domain/.

Ce que le produit ne sait pas encore faire ne se cache pas : ça devient
une section **« où en est le produit »**, en clair, dans la page. Sur une
page de vente, c'est ce qui rend le reste croyable.

## Procédure
1. Lire le persona : `Ce qu'il ne fera pas` et `Ce qui lui coûte` sont
   les deux sections qui écrivent le texte.
2. Partir de son vocabulaire, pas du tien. Les termes du domaine
   viennent de product/domain/, pas d'un registre marketing générique.
3. Produire 2 angles différents, jamais un seul :
   - un qui nomme la douleur
   - un qui nomme le résultat

   **En phase `local`** : ne pas s'arrêter pour faire choisir. Monter un
   angle, écrire l'autre dans le COPY marqué `<!-- écarté -->` avec la
   raison, et le dire en une ligne :
   `Angle <douleur|résultat> monté. L'autre est dans COPY-nnn, il se
   remonte en un tour.` Attendre un choix avant d'écrire l'écran, c'est
   le détour qu'on a retiré du chemin par défaut.

   **En phase `pilote`** : les deux angles, l'utilisateur choisit, aucune
   recommandation.

## Écriture
product/copy/COPY-nnn.md :

---
id: COPY-nnn
title: <emplacement — ex. "landing v1">
status: draft
persona: <role>-persona     # nom de fichier, PAS un ID du graphe
confiance: traces | miroir | auto-usage
links: [SPEC-nnn, IDEA-nnn]
updated: AAAA-MM-JJ
---

Une section par emplacement : `## hero`, `## sous-titre`, `## CTA`.
Chaque bloc porte sa longueur cible en caractères.
Les deux angles cohabitent dans le fichier jusqu'au choix ; l'angle
écarté reste, marqué `<!-- écarté -->`.

`links:` ne contient que des IDs du graphe. Le persona a son propre
champ — le hook rejetterait un lien vers un nom de fichier.

## Interdits
- Superlatifs : "révolutionnaire", "seamless", "unlock", "empower".
- Promettre une capacité absente des SPEC. Vérifier avant d'écrire.
- Écrire en français métropolitain pour un persona qui ne l'est pas.
- Livrer un mur de texte : bullets et blocs courts, toujours.
- Recommander un des deux angles en phase `pilote`.
- Refuser d'écrire faute de SPEC, de persona ou d'interview.
- Supprimer l'angle écarté. C'est la mémoire de ce qui n'a pas été choisi.

## Enchaînement visuel
Quand un bloc appelle une illustration, ne pas la décrire dans le COPY.
Invoquer `visual-prompt` avec l'intention, puis référencer le PROMPT-nnn
obtenu dans le bloc concerné.