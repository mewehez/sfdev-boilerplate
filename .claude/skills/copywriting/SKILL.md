---
name: copywriting
description: Produit les textes destinés à l'utilisateur final — landing,
  onboarding, messages d'erreur, emails, app store. Déclencher sur
  "écris la landing", "le texte de", "copy".
---

# Copywriting

## Garde-fou d'entrée — selon ADR-002
- **auto-usage** : pas de persona. Écrire pour soi, en s'appuyant sur
  product/JOURNAL.md. `! Tu écris pour toi : le texte te paraîtra
  évident. Fais-le relire.`
- **traces** : persona requis. S'il est absent → `! Aucun persona.
  Pour qui j'écris ?` Sinon, estampiller le COPY `confiance: traces`.
- **terrain** : persona requis. Si 0 INT `humain: oui` → écrire quand
  même, estampiller `confiance: miroir`, et le dire à l'utilisateur en
  une ligne.

Refuser dans tous les cas s'il n'existe aucune SPEC : le copy promet
un comportement, il ne l'invente pas.

## Procédure
1. Lire le persona : `Ce qu'il ne fera pas` et `Ce qui lui coûte` sont
   les deux sections qui écrivent le texte.
2. Partir de son vocabulaire, pas du tien. Les termes du domaine
   viennent de product/domain/, pas d'un registre marketing générique.
3. Produire 2 angles différents, jamais un seul :
   - un qui nomme la douleur
   - un qui nomme le résultat
   Laisser l'utilisateur choisir. Ne pas recommander.

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
- Recommander un des deux angles.

## Enchaînement visuel
Quand un bloc appelle une illustration, ne pas la décrire dans le COPY.
Invoquer `visual-prompt` avec l'intention, puis référencer le PROMPT-nnn
obtenu dans le bloc concerné.