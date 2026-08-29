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
IDEA-nnn  product/ideas/       une idée, à n'importe quel stade
SPEC-nnn  product/specs/       comportement attendu, testable
ADR-nnn   product/decisions/   décision structurante + alternatives écartées
DOM-nnn   product/domain/      fait de domaine, sourcé
INT-nnn   product/domain/interviews/  échange avec un expert (humain ou agent)
TASK-nnn  backlog/tasks/       unité d'implémentation
COPY-nnn    product/copy/          texte produit (landing, onboarding, erreurs)
PROMPT-nnn  product/assets/prompts/ prompt de génération visuelle + résultat
BRIEF-nnn   product/specs/briefs/   spec compilée, prête à exécuter
SUG-nnn   product/domain/suggestions/   option retenue sur proposition d'un
                                        agent, non validée par une preuve

Frontmatter obligatoire sur chaque fichier :
---
id: IDEA-007
title: ...
status: raw | grilled | parked | killed | specd | shipped
links: [DOM-002, ADR-001]
updated: AAAA-MM-JJ
---

## Règle des suggestions
Une option choisie dans une liste proposée par `suggester` reste
`[SUPPOSÉ]`. La cocher ne la transforme pas en fait.

Cycle de vie d'un SUG :
  pending    → retenu, sans preuve
  validé     → un TRC/INT/DOM postérieur le confirme (renseigner `preuve:`)
  invalidé   → une preuve postérieure le contredit
  abandonné  → l'option n'est plus dans le projet

Tout objet dont une décision repose sur un SUG `pending` le déclare
dans `links:`. C'est ce lien qui rend la dette visible.

## Règles de graphe
- Une SPEC sans lien vers une IDEA est orpheline → interdite.
- Une TASK sans lien vers une SPEC est orpheline → interdite.
- Un fait de domaine sans source datée est `[SUPPOSÉ]`, pas un DOM.
- Un COPY sans lien vers une SPEC ou un persona est orphelin → interdit.
- Un PROMPT sans lien vers le COPY ou la SPEC qui le motive est orphelin.
- Un BRIEF doit citer au moins une SPEC. Un BRIEF est immuable une fois
  `status: ready` — une correction crée BRIEF-nnn+1 qui référence l'ancien.

## Chemin court

Le processus complet existe pour ce qu'on ne peut pas défaire facilement.
Pas pour le reste.

### Éligible au chemin court
Les trois conditions, ensemble :
- < 30 min de travail
- réversible : un `git revert` suffit, rien à migrer, rien à prévenir
- n'entre en contradiction avec aucun ADR

Exemples : correction de bug local, renommage, ajustement de style,
message d'erreur, dépendance mise à jour, test ajouté, refactor interne
sans changement de contrat.

### Non éligible — processus complet obligatoire
- touche un contrat : schéma de données, API publique, format de fichier
- touche l'argent, les données personnelles, l'authentification, les droits
- ajoute une dépendance externe ou un service tiers
- change ce que l'utilisateur final voit ou peut faire
- contredit un ADR — même « juste un peu »
- tu hésites sur l'éligibilité → ce n'est pas éligible

### Procédure
1. Faire.
2. Écrire la TASK rétroactive, `status: done`, `chemin: court`.
   Le champ `## Fini quand` décrit ce qui a été fait, pas ce qui était prévu.
3. La TASK est dispensée de parent SPEC. C'est la seule exception à la
   règle d'orphelinat, et elle est visible : le hook la compte.

### Garde-fou
Le hook compte les TASK en chemin court sur les 30 derniers jours.
Au-delà de 60 % du total, il signale :
`! N% du travail passe en chemin court — soit le processus est trop lourd,
soit tu contournes.`

Ce n'est pas un reproche, c'est une mesure. Les deux causes sont
plausibles et se traitent différemment. Si le processus est trop lourd,
c'est le processus qui change — écrire un ADR pour ça.

### Escalade
Si pendant un chemin court tu découvres que ça touche un contrat ou un
ADR : arrêter, `git stash`, capturer en IDEA, sortir du chemin court.
Ne jamais finir « puisqu'on y est ».

## Navigation
Ouvrir product/ comme coffre Obsidian. Vue graphe = carte du projet.
product/INDEX.md est régénéré par la skill `graph-index`.

## Régime de preuve
Déclaré dans ADR-002 à l'ouverture du projet : auto-usage | traces | terrain

- auto-usage : je suis l'utilisateur. Preuve = usage documenté (JOURNAL.md).
  Aucun persona n'est instancié. Pas d'avertissement interview.
- traces   : preuve = TRC-nnn (observations publiques sourcées et datées).
  Les personas sont construits à partir des TRC, jamais d'imagination.
- terrain  : INT humain obligatoire avant tout BRIEF ready.

Nouveaux IDs :
TRC-nnn   product/domain/traces/   observation publique, sourcée, datée

Frontmatter TRC obligatoire :
---
id: TRC-nnn
title: ...
source: <URL, ou description stable si hors web>
type: avis | support | forum | emploi | reglementaire | presse | produit
echantillon: <nombre d'items observés>
status: raw | confirmé
updated: AAAA-MM-JJ   # date de consultation, pas date de création
---

Deux traces du même `type` ET du même domaine ne comptent que comme
une source. La diversité des sources vaut plus que leur nombre.

## Répartition avec Superpowers

Ce dépôt gère l'AMONT : quoi construire, pourquoi, dans quel ordre.
Superpowers gère l'AVAL : comment le construire correctement.

Frontière : le BRIEF en status `ready`.
  amont  → IDEA → SPEC → BRIEF        (nos skills)
  aval   → plan → TDD → revue → merge (Superpowers)

Nos skills n'écrivent JAMAIS de code applicatif.
Superpowers ne décide JAMAIS du quoi ni du pourquoi.

### Passage de relais
Un BRIEF `ready` est l'unique entrée de Superpowers.
Le passer via /write-plan ou /execute-plan, jamais en paraphrasant
le BRIEF dans le chat — le BRIEF a été compilé pour ça.

### Retour de relais
Superpowers finit → mettre à jour la TASK et le BRIEF en `shipped`.
Si l'implémentation a révélé un manque dans le BRIEF : capturer en IDEA
(mode capture), ne pas patcher le BRIEF a posteriori. Un BRIEF `ready`
est immuable — c'est ce qui rend la trace lisible.

### Budget de contexte au SessionStart
Superpowers et notre hook injectent tous les deux.
Le nôtre reste plafonné à 7 lignes. Si le SessionStart devient lourd,
retirer le hook `Stop` avant de toucher au `SessionStart`.

### Ce qu'on ne réécrit pas
TDD, débogage systématique, revue en deux temps, sous-agents, plans
d'exécution : c'est Superpowers. Toute skill locale qui recouvre ça
est à supprimer.

### Collision de vocabulaire
Superpowers a son propre /brainstorm, orienté raffinement d'une exigence
avant code. Le nôtre (project-grill, idea-grill) décide s'il faut
construire. Ne pas les confondre : /brainstorm arrive APRÈS le verdict.

## Archivage
Va dans product/archive/ (en conservant le sous-chemin d'origine) :
- IDEA killed
- SPEC/BRIEF rendus caducs par un ADR postérieur
- SUG abandonné
- TRC périmé dont la source a disparu

Ne va JAMAIS dans l'archive :
- un ADR — une décision reste vraie même quand elle est remplacée.
  Marquer `status: remplacé par ADR-nnn` et laisser en place.
- un INT ou un DOM — une observation ne devient pas fausse.
  Elle vieillit, c'est différent.

Règle absolue : un ID archivé n'est jamais réattribué.
Le fichier garde son frontmatter intact. On archive, on ne supprime pas.
