---
name: spec-compiler
description: Transforme une SPEC en BRIEF exécutable et le passe en ready,
  seule porte d'entrée vers Superpowers. Déclencher sur "compile SPEC-nnn",
  "prêt à coder". Aucune implémentation ne démarre sans BRIEF ready.
---

# Compilateur de spec

Le grill parle humain. L'agent de code a besoin d'autre chose : pas de
pronom sans référent, pas d'adjectif d'appréciation, pas d'implicite.

## Entrée
Une SPEC en `status: specd`, avec sa chaîne (écrite par idea-grill).

## Quand compiler — et quand ne pas compiler
Un BRIEF sert à passer la main proprement à Superpowers, en phase
`pilote`. En phase `local`, il n'en faut pas : `feature-build` construit
directement. Compiler une SPEC pour un écran de démo est du travail perdu.

`? On est en phase local. Tu veux un BRIEF, ou je construis directement ?`
— poser une fois, puis suivre la réponse.

## Passe 0 — Recevabilité
En régime `exploration` (défaut) : **aucun refus**. Une SPEC sans preuve
se compile ; ce qui est supposé est marqué `[SUPPOSÉ]` dans le corps du
BRIEF et tracé en `SUG`. La preuve ne conditionne rien.

Un seul cas de retour à `idea-grill` : la SPEC n'a pas d'IDEA parente —
et c'est un simple rattachement, pas un blocage.

En régime `traces` ou `terrain`, des refus s'ajoutent : voir
`.claude/optional/RIGUEUR.md`.

## Passe 1 — Chasse au flou
Lister ce qui ne survivra pas à la compilation :
- adjectifs non mesurables : "simple", "rapide", "intuitif", "propre"
- quantificateurs vagues : "plusieurs", "la plupart", "généralement"
- pronoms sans référent explicite
- comportements d'erreur non spécifiés
- termes métier non définis dans product/domain/

Une question à la fois. Sans réponse → dispatcher `suggester`.
Toute option retenue via suggester crée un SUG-nnn `pending` qui DOIT
apparaître dans les `links:` du BRIEF, et la ligne concernée est
marquée `[SUPPOSÉ]` dans le corps.

## Passe 2 — Écriture du BRIEF

---
id: BRIEF-nnn
title: <impératif, un résultat>
status: draft
links: [SPEC-nnn, ADR-nnn, <DOM/TRC/INT-nnn>, <SUG-nnn si applicable>]
updated: AAAA-MM-JJ
---

## Objectif
- <une phrase. Ce qui est vrai après, qui ne l'était pas avant.>

## Contexte strictement nécessaire
- <fichiers concernés, contrats existants, conventions à respecter>
- <rien d'autre — un contexte inutile dégrade le résultat>

## Comportement attendu
- Entrée <X> → sortie <Y>
- Cas limite <Z> → <comportement exact>
- Erreur <E> → <message, code, log>
(un cas par ligne, tous testables)

## Contraintes non négociables
- <issues des ADR, citées avec leur ID>

## Hors périmètre
- <minimum 2 — c'est ce qui empêche la dérive>

## Fini quand
- <critère vérifiable par exécution, pas par lecture>

## Vocabulaire
- <terme métier> = <définition> [DOM-nnn]

## [SUPPOSÉ]
- <ce qui repose sur un SUG pending, avec son ID>

## Passe 3 — Bascule en ready
Le BRIEF reste `draft` tant que l'un de ces points échoue. Ce sont des
critères de **lisibilité pour l'exécutant**, jamais des critères de preuve :
- un adjectif d'appréciation subsiste
- "Hors périmètre" a moins de 2 entrées
- un "Fini quand" n'est pas exécutable
- un terme métier n'est ni dans Vocabulaire ni dans product/domain/

Tout passe → écrire `status: ready` dans le frontmatter.
C'est cette bascule qui ouvre la frontière Superpowers. Personne d'autre
ne la fait. Un BRIEF ready est immuable : une correction crée
BRIEF-nnn+1 avec `links:` vers l'ancien, qui passe `caduc`.

## Sortie — ≤ 8 bullets
## BRIEF-nnn <ready | draft> — <chemin>
## Ce que j'ai dû trancher
- <les flous levés, et comment>
## ! Reste supposé
- <SUG-nnn en jeu, ou "rien">
## → Suite : product-owner pour la TASK (`phase:` obligatoire), puis /write-plan

## Interdits
- Compiler une SPEC `remplacée` ou `caduque`.
- Refuser de compiler faute de preuve, d'interview ou de source.
- Passer en `ready` sans avoir vérifié la Passe 3 point par point.
- Modifier un BRIEF déjà `ready`.
- Ajouter une exigence absente de la SPEC → retour à idea-grill.
- Écrire du code. Tu produis l'instruction, pas le résultat.