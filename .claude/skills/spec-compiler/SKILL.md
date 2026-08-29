---
name: spec-compiler
description: Transforme une SPEC issue d'un grill en BRIEF exécutable par
  un agent de code. Déclencher sur "compile SPEC-nnn", "prêt à coder",
  ou avant tout passage à l'implémentation. Aucune TASK ne s'exécute sans
  BRIEF.
---

# Compilateur de spec

Le grill parle humain. L'agent de code a besoin d'autre chose : pas de
pronom sans référent, pas d'adjectif d'appréciation, pas d'implicite.

## Entrée
Une SPEC en `status: specd` + sa chaîne complète (idea-grill l'a écrite).

## Passe 1 — Chasse au flou
Scanner la SPEC et lister ce qui ne survivra pas à la compilation :
- adjectifs non mesurables : "simple", "rapide", "intuitif", "propre"
- quantificateurs vagues : "plusieurs", "la plupart", "généralement"
- pronoms sans référent explicite
- comportements d'erreur non spécifiés
- termes métier non définis dans product/domain/

Pour chaque trouvaille, une question à l'utilisateur, une à la fois.
Sans réponse → convoquer `suggester`.

## Passe 2 — Écriture du BRIEF

---
id: BRIEF-nnn
title: <impératif, un résultat>
status: draft
links: [SPEC-nnn, ADR-nnn, DOM-nnn]
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

## Passe 3 — Autocontrôle avant `status: ready`
Refuser de passer en ready si :
- un adjectif d'appréciation subsiste
- "Hors périmètre" a moins de 2 entrées
- un "Fini quand" n'est pas exécutable
- un terme métier n'est pas dans Vocabulaire ou dans product/domain/

## Sortie à l'écran — ≤ 8 bullets
## BRIEF-nnn écrit — <chemin>
## Ce que j'ai dû trancher
- <les flous levés, et comment>
## ! Reste supposé
- <ce qui n'a pas pu être levé>

## Interdits
- Compiler une SPEC en status `raw` ou `parked`.
- Ajouter une exigence absente de la SPEC. Si elle manque → retour à
  idea-grill, pas d'ajout silencieux.
- Écrire du code. Tu produis l'instruction, pas le résultat.