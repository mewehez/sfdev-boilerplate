# Règles projet

## Concision (s'applique à TOUS les agents et skills)
- Bullet points. Jamais de paragraphes.
- Aucun préambule, aucun récapitulatif de ce que tu viens de faire.
- Aucune reformulation de ma question.
- Marquage obligatoire :
  `→` action que je dois faire   `?` question   `!` risque/blocage
- Une seule question par tour. Attendre la réponse.
- Écran maximum. Si ça dépasse, écris dans un fichier et donne-moi
  le chemin + 3 bullets de synthèse.
- Jamais de validation gratuite ("bonne idée", "excellent point").

## Conventions d'ID

Format strict : `<TYPE>-nnn` — exactement 3 chiffres, zéros inclus.
`ADR-001`, jamais `ADR-1` ni `ADR-0001`. Le hook rejette tout le reste.

IDEA-nnn    product/ideas/                idée, à n'importe quel stade
SPEC-nnn    product/specs/                comportement attendu, testable
BRIEF-nnn   product/specs/briefs/         spec compilée, prête à exécuter
ADR-nnn     product/decisions/            décision + alternatives écartées
DOM-nnn     product/domain/               fait de domaine, sourcé
TRC-nnn     product/domain/traces/        observation publique, sourcée, datée
SUG-nnn     product/domain/suggestions/   option retenue sur proposition
                                          d'un agent, non validée
INT-nnn     product/domain/interviews/    échange avec un expert
COPY-nnn    product/copy/                 texte destiné à l'utilisateur final
PROMPT-nnn  product/assets/prompts/       prompt de génération visuelle
TASK-nnn    backlog/tasks/                unité d'implémentation

Avant d'attribuer un ID : lire product/INDEX.md, y compris la section
`## IDs réservés — archivés`. Un ID archivé n'est JAMAIS réattribué.

### Frontmatter — commun à tous
---
id: <TYPE>-nnn
title: ...
status: <voir ci-dessous>
links: [ID, ID]
updated: AAAA-MM-JJ
---

### Status valides, par type
IDEA    raw | parked | specd | killed
SPEC    specd | remplacée | caduque
BRIEF   draft | ready | shipped | caduc
ADR     actif | remplacé par ADR-nnn
DOM     raw | confirmé
TRC     raw | confirmé
SUG     pending | validé | invalidé | abandonné
INT     raw | confirmé
COPY    draft | retenu | rejeté
PROMPT  draft | generated | retenu | rejeté
TASK    todo | doing | done

Aucun autre status. Le hook n'en vérifie qu'une partie — la liste fait foi.

### Champs supplémentaires obligatoires
IDEA    origine: utilisateur | agent   contexte: <où l'idée est née>
TRC     source: <URL ou libellé stable>
        type: avis | support | forum | emploi | reglementaire | presse | produit
        echantillon: <nombre d'items observés>
DOM     source: <URL ou libellé stable>
SUG     question: <la question restée sans réponse>
        appelant: <skill ou agent>   recherche: oui | non
        preuve: <vide tant que pending>
INT     humain: oui | non
TASK    chemin: normal | court
COPY    persona: <role>-persona (sauf auto-usage)
        confiance: traces | miroir | auto-usage
PROMPT  outil: <modèle utilisé>

## Règles de graphe
- Une SPEC sans lien vers une IDEA est orpheline → interdite.
- Un BRIEF doit citer au moins une SPEC.
- Une TASK sans lien vers une SPEC ou un BRIEF est orpheline → interdite.
  Seule exception : `chemin: court`.
- Un COPY sans lien vers une SPEC ou une IDEA est orphelin.
- Un PROMPT sans lien vers le COPY ou la SPEC qui le motive est orphelin.
- Un fait de domaine sans source datée est `[SUPPOSÉ]`, pas un DOM.
- Un BRIEF est immuable une fois `ready` — une correction crée
  BRIEF-nnn+1 qui référence l'ancien.

## Règle des suggestions
Une option choisie dans une liste proposée par `suggester` reste
`[SUPPOSÉ]`. La cocher ne la transforme pas en fait.

  pending    retenu, sans preuve
  validé     un TRC/INT/DOM postérieur le confirme (renseigner `preuve:`)
  invalidé   une preuve postérieure le contredit
  abandonné  l'option n'est plus dans le projet

Tout objet dont une décision repose sur un SUG `pending` le déclare
dans `links:`. C'est ce lien qui rend la dette visible.

## Régime de preuve
Déclaré dans ADR-002 à l'ouverture du projet, ligne exacte lue par
le hook : `regime: auto-usage | traces | terrain`

- auto-usage : je suis l'utilisateur. Preuve = usage documenté
  (product/JOURNAL.md). Aucun persona n'est instancié.
- traces : preuve = TRC. Les personas sont construits à partir des TRC,
  jamais d'imagination. Deux traces du même `type` ET du même domaine
  ne comptent que comme une source — la diversité vaut plus que le nombre.
- terrain : INT humain obligatoire avant tout BRIEF `ready`.

## Recherche en ligne
Toute recherche web demande l'autorisation, une fois par sujet :
`? Il me manque X. Je cherche en ligne ? (o/n)`
Sans exception, y compris pendant un grill. Ce qui est trouvé est
écrit en DOM ou TRC, jamais gardé en tête.

## Chemin court

Le processus complet existe pour ce qu'on ne peut pas défaire facilement.
Pas pour le reste.

### Éligible — les trois conditions ensemble
- < 30 min de travail
- réversible : un `git revert` suffit, rien à migrer, rien à prévenir
- n'entre en contradiction avec aucun ADR

Exemples : bug local, renommage, style, message d'erreur, dépendance
mise à jour, test ajouté, refactor sans changement de contrat.

### Non éligible — processus complet obligatoire
- touche un contrat : schéma de données, API publique, format de fichier
- touche l'argent, les données personnelles, l'authentification, les droits
- ajoute une dépendance externe ou un service tiers
- change ce que l'utilisateur final voit ou peut faire
- contredit un ADR — même « juste un peu »
- tu hésites → ce n'est pas éligible

### Procédure
1. Faire.
2. Écrire la TASK rétroactive, `status: done`, `chemin: court`.
   `## Fini quand` décrit ce qui a été fait, pas ce qui était prévu.
3. Dispensée de parent SPEC — seule exception à la règle d'orphelinat,
   et elle est visible : le hook la compte.

### Garde-fou
Au-delà de 60 % de chemin court sur 30 jours, le hook signale.
Ce n'est pas un reproche, c'est une mesure : soit le processus est trop
lourd, soit tu contournes. Les deux se traitent différemment. Si c'est
le processus, c'est le processus qui change — écrire un ADR pour ça.

### Escalade
Si pendant un chemin court ça touche un contrat ou un ADR : arrêter,
`git stash`, capturer en IDEA, sortir. Ne jamais finir « puisqu'on y est ».

## Archivage
Va dans product/archive/ (sous-chemin d'origine conservé) :
- IDEA killed
- SPEC/BRIEF caducs
- SUG abandonné
- TRC dont la source a disparu

Ne va JAMAIS dans l'archive :
- un ADR — une décision reste vraie même remplacée.
  Marquer `status: remplacé par ADR-nnn` et laisser en place.
- un INT ou un DOM — une observation ne devient pas fausse. Elle vieillit.

On archive, on ne supprime pas. Le frontmatter reste intact.

## Navigation
product/INDEX.md est régénéré automatiquement par
.claude/hooks/graph_index.py aux événements SessionStart et Stop.
Ne jamais l'éditer à la main — toute modification sera écrasée.
La skill `graph-index` sert à LIRE l'index et à réparer le graphe,
pas à produire l'index.

Ouvrir product/ comme coffre Obsidian : les [[ID]] deviennent
cliquables, la vue graphe est native.

## Répartition avec Superpowers

Ce dépôt gère l'AMONT : quoi construire, pourquoi, dans quel ordre.
Superpowers gère l'AVAL : comment le construire correctement.

Frontière : le BRIEF en `ready`.
  amont  IDEA → SPEC → BRIEF          (nos skills)
  aval   plan → TDD → revue → merge   (Superpowers)

Nos skills n'écrivent JAMAIS de code applicatif.
Superpowers ne décide JAMAIS du quoi ni du pourquoi.

### Passage de relais
Un BRIEF `ready` est l'unique entrée de Superpowers, via /write-plan ou
/execute-plan. Jamais en paraphrasant le BRIEF dans le chat : il a été
compilé pour ça.

### Retour de relais
Superpowers finit → TASK `done`, BRIEF `shipped`.
Si l'implémentation révèle un manque : capturer en IDEA, ne pas patcher
le BRIEF. Un BRIEF `ready` est immuable — c'est ce qui rend la trace lisible.

### Ce qu'on ne réécrit pas
TDD, débogage systématique, revue en deux temps, sous-agents, plans
d'exécution. Toute skill locale qui recouvre ça est à supprimer.

### Collision de vocabulaire
Le /brainstorm de Superpowers raffine une exigence avant code.
Nos grills décident s'il faut construire. /brainstorm arrive APRÈS
le verdict.

### Budget de contexte au SessionStart
Superpowers et notre hook injectent tous les deux. Le nôtre tient en
4 lignes quand tout va bien, jusqu'à 9 quand plusieurs alertes tombent.
Si le SessionStart devient lourd, retirer le hook `Stop` avant de
toucher au `SessionStart`.