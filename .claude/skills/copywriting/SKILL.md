---
name: copywriting
description: Produit les textes destinés à l'utilisateur final — landing,
  onboarding, messages d'erreur, emails, app store. Déclencher sur
  "écris la landing", "le texte de", "copy". Ne jamais écrire de copy
  sans persona ni SPEC.
---

# Copywriting

## Garde-fou d'entrée
Refuser si :
- aucun persona dans .claude/agents/ → `! Pour qui j'écris ?`
- le persona a 0 interview humaine → écrire quand même, mais estampiller
  le COPY `confiance: miroir` et le dire à l'utilisateur.

## Procédure
1. Lire le persona concerné : "Ce qu'il ne fera pas" et "Ce qui lui coûte"
   sont les deux sections qui écrivent le texte.
2. Partir de son vocabulaire à lui, pas du tien. Les termes du domaine
   viennent de product/domain/, pas d'un registre marketing générique.
3. Produire 2 angles différents, jamais un seul :
   - un qui nomme la douleur
   - un qui nomme le résultat
   Laisser l'utilisateur choisir.

## Écriture
- product/copy/COPY-nnn.md, links: [SPEC-nnn, <role>-persona]
- Une section par emplacement : `## hero`, `## sous-titre`, `## CTA`, etc.
- Chaque bloc porte sa longueur cible en caractères.

## Interdits
- Superlatifs, "révolutionnaire", "seamless", "unlock", "empower".
- Promettre une capacité absente des SPEC. Vérifier avant d'écrire.
- Écrire en français métropolitain pour un persona qui ne l'est pas.
- Livrer un mur de texte : bullets et blocs courts, toujours.

## Enchaînement visuel
Quand un bloc appelle une illustration, ne pas la décrire dans le COPY.
Appeler `visual-prompt` avec l'intention, et référencer PROMPT-nnn.