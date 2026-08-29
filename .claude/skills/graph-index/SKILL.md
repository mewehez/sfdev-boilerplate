---
name: graph-index
description: Navigation et réparation du graphe product/. Déclencher sur
  "où on en est", "montre-moi le graphe", "qu'est-ce qui est orphelin",
  "d'où vient SPEC-nnn". Ne jamais éditer INDEX.md à la main.
---

# Graphe

## Lecture
Toujours lire product/INDEX.md AVANT de répondre à une question de
navigation. Ne jamais reconstruire le graphe de mémoire.

## Remontée de chaîne ("d'où vient X ?")
Sortie ≤ 8 bullets, une chaîne par ligne :
  TASK-012 ← SPEC-004 ← IDEA-007 ← INT-002 (humain)
Marquer `!` toute chaîne qui remonte à un `[SUPPOSÉ]` sans DOM ni INT.

## Réparation d'orphelin
Pour chaque orphelin signalé par le hook, une question à la fois :
  "? SPEC-004 n'a pas d'IDEA parente. Elle vient de quelle idée —
   ou je crée IDEA-nnn rétroactivement ?"
Jamais de rattachement deviné.

## Interdits
- Éditer INDEX.md (généré).
- Créer un lien que l'utilisateur n'a pas confirmé.
- Répondre "tout est cohérent" sans avoir lu la section `! Incohérences`.