---
name: software-architect
description: Deux usages. CONSULTATION — invoquée par idea-grill pour dire
  quelle décision une idée casserait. SCAFFOLDING — met en place src/
  quand un BRIEF ready existe. Déclencher sur "scaffolde", "mets en place
  le projet", "quelle stack".
---

# Architecte logiciel

## MODE CONSULTATION
Invoquée par idea-grill G1. Répondre en ≤ 4 bullets :
- quel ADR ou contrat existant l'idée toucherait
- ce que ça coûterait structurellement (pas en jours)
- `!` si l'idée est incompatible avec une décision actée

N'écrire aucun fichier. Ne rien scaffolder. Rendre la main.

---

# MODE SCAFFOLDING

## Condition d'entrée — une seule
Il faut **un périmètre et une intention**. C'est tout.

Suffit à démarrer, dans l'ordre de préférence :
- `product/decisions/ADR-001-perimetre.md`, ou
- une liste de features v1 dans `product/grill/`, ou
- une IDEA, une SPEC ou un BRIEF, à n'importe quel status, ou
- l'utilisateur qui dit ce qu'il veut construire, dans le tour courant.

Ne JAMAIS exiger : un BRIEF `ready`, une SPEC, une preuve, un verdict de
grill, une interview. Cette chaîne de prérequis empêchait `src/` d'exister
— c'est le défaut qu'on corrige.

Si rien de tout ça n'existe : poser UNE question — `? On construit quoi,
en une phrase ?` — puis scaffolder sur la réponse.

Seul refus : `src/` existe déjà → `! Squelette déjà posé. Précise ce que
tu veux ajouter.`

## Périmètre — strictement le squelette

Autorisé :
- arborescence src/ pour la SEULE surface déclarée première en ADR-001
  (les autres attendent)
    src/
    ├── <surface>/     web | mobile | desktop | api | cli
    └── shared/        types et contrats partagés
- config de build, lint, formatage, runner de tests
- un test qui échoue, prouvant que la chaîne de test tourne
- ADR de stack

Interdit :
- toute logique métier — `feature-build` s'en charge juste après
- écrire une suite de tests de comportement
- scaffolder une surface non déclarée première

## ADR de stack
Écrire product/decisions/ADR-nnn.md : stack retenue, alternatives
écartées avec la raison, ce qui la ferait changer.
Contrainte : proposer ce que l'utilisateur maîtrise déjà, sauf raison
explicite. Signaler `!` toute techno nouvelle pour lui.

## Sortie unique — ≤ 6 bullets
## Squelette posé — <chemins créés>
## ADR-nnn — stack et alternatives écartées
## Tourne avec — `<commande>` → <ce qu'on doit voir>
## Chaîne de test — `<commande>`, échoue comme attendu
## → Suite : feature-build sur <la première feature>

Vérifier soi-même que la commande de lancement tourne avant de l'annoncer.

En phase `local`, enchaîner sur `feature-build` dans le même tour : un
squelette sans écran n'est pas un livrable. En phase `pilote`, rendre la
main à Superpowers via `/write-plan` avec le BRIEF.