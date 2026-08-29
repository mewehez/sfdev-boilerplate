---
name: graph-index
description: Lecture et réparation du graphe product/. Déclencher sur
  "où on en est", "montre-moi le graphe", "qu'est-ce qui est orphelin",
  "d'où vient SPEC-nnn", "quelles incohérences". Ne produit pas l'index.
---

# Graphe

## Qui écrit quoi
product/INDEX.md est généré par .claude/hooks/graph_index.py aux
événements SessionStart et Stop. Cette skill le LIT et aide à réparer
ce qu'il signale. Elle ne l'écrit jamais.

## Lecture
Toujours lire product/INDEX.md AVANT de répondre. Ne jamais
reconstruire le graphe de mémoire, ni deviner un compteur.

Sections à connaître :
- `! Incohérences` — la première à lire, toujours
- `File de grill` — IDEA raw en attente
- `Parquées` — gelées, avec leur question décisive
- `Dette d'hypothèses` — SUG pending et ce qui en dépend
- `Diversité des traces` — régime traces uniquement
- `IDs réservés — archivés` — IDs pris, jamais réattribuables

## Remontée de chaîne ("d'où vient X ?")
Sortie ≤ 8 bullets, une chaîne par ligne :
  TASK-012 ← BRIEF-006 ← SPEC-004 ← IDEA-007 ← INT-002 [humain]
Types de preuve terminaux : INT, TRC, DOM.
Marquer `!` :
- toute chaîne dont la racine est un `[SUPPOSÉ]` sans DOM, TRC ni INT
- toute chaîne traversant un SUG `pending`
- toute chaîne dont une preuve est un TRC de plus de 6 mois

## Réparation d'orphelin
Pour chaque orphelin signalé, une question à la fois :
  `? SPEC-004 n'a pas d'IDEA parente. Elle vient de quelle idée —
   ou je crée IDEA-nnn rétroactivement ?`
Jamais de rattachement deviné, jamais de rattachement en lot.

Cas particuliers :
- TASK orpheline sans `chemin: court` → demander si c'était un chemin
  court non déclaré, ou une TASK qui a perdu son BRIEF.
- Lien vers un ID archivé → la décision repose sur du mort.
  Proposer : dégeler l'archivé, ou retirer le lien. Ne pas trancher.
- `Dossier manquant` → ne pas créer. Le signaler et rappeler que la
  structure vient du boilerplate.

## Attribution d'un ID
Sur demande du prochain ID libre : lire la section du type concerné
ET `IDs réservés — archivés`. Le prochain libre est le successeur du
plus grand des deux. Un ID archivé n'est jamais réutilisé.

## Interdits
- Éditer INDEX.md.
- Créer un lien que l'utilisateur n'a pas confirmé.
- Répondre "tout est cohérent" sans avoir lu `! Incohérences`.
- Créer un dossier manquant pour faire taire un avertissement.