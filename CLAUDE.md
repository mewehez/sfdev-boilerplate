# Règles projet

## Le contrat en une phrase
Une idée exprimée devient un produit qui tourne. La traçabilité suit,
elle ne précède jamais. Rien n'attend une preuve pour exister.

---

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

---

## Mode par défaut : `exploration`

C'est le mode unique, actif sans rien déclarer.

- **Aucun blocage, nulle part.** Ni sur une SPEC, ni sur un BRIEF, ni sur
  une TASK, ni sur le scaffolding. Aucun objet n'attend une preuve.
- Une hypothèse se trace (`SUG`), elle ne freine rien.
- Une recherche web et un raisonnement suffisent à écrire un `DOM`.
- Le hook affiche des lignes factuelles. Il ne produit aucune alerte de
  preuve, aucune injonction à interviewer.
- On construit par intuition, ou pour un portfolio. Un visuel sert
  justement à approcher les gens : il vient avant eux, pas après.

**Ce qui bloque quand même**, parce que ça relève de l'ordre et non de la
preuve — deux refus, deux seulement, tenus par `.claude/hooks/phase_guard.py` :
1. une TASK `phase: dur` tant qu'une TASK `phase: local` est ouverte ;
2. un écran sous `src/` tant que `product/assets/DESIGN.md` n'existe pas.

Un refus se lève en faisant la chose dans le bon ordre, jamais en
argumentant avec le hook.

### Activer la rigueur, plus tard
Une piste se confirme, quelqu'un d'autre commence à payer l'erreur :
écris `regime: traces` (ou `terrain`) dans le corps de
`product/decisions/ADR-002-regime-preuve.md` — mode d'emploi complet dans
`.claude/optional/RIGUEUR.md`.

---

## Phases d'exécution

Champ `phase:` obligatoire sur toute TASK. Trois valeurs, dans cet ordre :

| phase    | ce qu'elle contient |
|----------|---------------------|
| `local`  | ce qui fait tourner l'app sur la machine |
| `pilote` | ce qu'il faut pour la montrer à quelqu'un de réel |
| `dur`    | forme juridique, nom de domaine, hébergement, conformité, CGU, contrats opérateurs |

**Règle, tenue par le hook :** aucune TASK `dur` ouverte tant qu'une TASK
`local` reste ouverte.

Le juridique produit des **templates à trous** (`product/legal/`, hors
graphe, sans ID), jamais des blocages. Un template s'écrit quand on veut,
sans TASK — c'est une TASK `dur` qui est refusée, pas un fichier.

### Tests, par phase
- `local` : tester les **invariants métier** et les **erreurs qui coûtent
  cher** — une valeur qui bouge, un geste joué deux fois, une donnée
  perdue. Pas chaque fonction.
- `pilote` : le TDD complet de Superpowers démarre ici.
- `dur` : sans objet.

Écrire un test par fonction en phase `local` est une perte nette. Écrire
zéro test sur un invariant qui ne se rattrape pas est une faute.

---

## Le chemin par défaut : la feature

L'étalon est le mode non structuré : l'utilisateur dit une feature, un
écran tourne à la fin du tour. Si le processus produit moins que ça,
c'est le processus qui a tort.

Sur "je veux que…", "ajoute…", "l'écran doit…" → skill `feature-build`.
Elle construit d'abord et trace ensuite, dans le même tour.

Le circuit long (IDEA → grill → SPEC → BRIEF → TASK) existe pour ce qui
est cher à défaire : un contrat de données, un format d'échange, de
l'argent, de l'authentification. Pas pour le reste.

---

## Le web est le lieu du développement

**Une feature se développe sur le web. Toujours.** Le mobile et le
desktop ne font que **porter** ce qui existe déjà — ils n'ajoutent jamais
un comportement que le web n'a pas.

Pourquoi cette règle et pas une autre : un cycle web est de quelques
secondes — enregistrer, recharger, voir. Un cycle mobile natif est de
quelques minutes — compiler, signer, installer, relancer. Développer une
feature dans le port multiplie ce coût par le nombre d'essais, c'est-à-dire
par beaucoup. Et une feature écrite deux fois diverge toujours.

- Une feature demandée « pour le mobile » se construit **sur le web**,
  puis se porte.
- Un port ne contient que : configuration de build, coquille native,
  branchements de capacités natives (caméra, biométrie, notifications),
  icônes et signature. **Aucune règle métier, aucun écran.**
- Un correctif qui ne concerne que le port (une marge sous l'encoche, un
  clavier qui recouvre un champ) se fait dans le CSS du web, pas dans le
  port. Le web doit rester juste tout seul.

### Un seul endroit où regarder

Un serveur de développement s'ouvre pour être **regardé**. S'il y en a
deux, l'un des deux ment — et rien ne dit lequel.

- **Avant d'ouvrir un port, libérer celui qui sert déjà le produit.** Pas
  « en ouvrir un autre à côté » : le port occupé est occupé par une
  version, et c'est celle-là qu'on va regarder par habitude.
- **Un serveur laissé derrière soi n'est pas neutre.** Il continue de
  servir l'état du code au moment où il a démarré. Plus le tour avance,
  plus ce qu'il montre est faux — et il ne le dit pas.
- **À la fin d'un tour, on referme ce qu'on a ouvert**, ou on écrit noir
  sur blanc ce qui reste ouvert, à quelle adresse, et de quand ça date.
- La même règle vaut pour une pile conteneurisée : une pile qui tourne
  sur d'anciennes images est un piège, pas une commodité. On la
  reconstruit, ou on l'arrête.

Le coût de l'oubli ne se paie pas sur sa propre machine : il se paie
quand quelqu'un d'autre ouvre l'adresse qu'on lui a donnée et juge le
produit sur une version morte.

**Cibles par défaut** : `PWA` sur téléphone, `Tauri v2` sur ordinateur.
On n'en change qu'en nommant la capacité qui manque.

Un port écrit dans un **autre langage** n'est pas un problème — Tauri est
en Rust, Capacitor colle du Swift et du Kotlin. Une **réécriture native**
(Flutter, Kotlin Multiplatform, React Native) n'est pas interdite non
plus : c'est une décision, qui s'écrit dans un ADR.

La seule ligne qui ne se négocie pas : **la logique qui décide de
ce qui est irréversible n'existe qu'une fois.** Un écran redessiné se
corrige ; une règle d'idempotence écrite deux fois diverge, et les deux
versions ont raison chacune de son côté. Ce qui ne se reprend pas prend
mille formes selon le produit — une valeur qui bouge, un droit accordé,
un envoi parti, un dossier détruit.

Le portage est une activité de **phase `pilote`** : on ne porte pas une
application qui n'est pas finie. Le hook `phase_guard.py` refuse d'écrire
sous `mobile/`, `desktop/`, `ios/` ou `android/` tant qu'une TASK `local`
est ouverte.

Un port se fait écran par écran, de mémoire — et **on ne voit pas ce
qu'on ne regarde pas**. Le trou ne se manifeste ni à la compilation ni à
l'ouverture des écrans portés : il se manifeste le jour où quelqu'un
cherche un réglage et ne le trouve pas. Donc **l'inventaire de ce qu'il
y a à porter se dérive de la source, jamais de tête**, et il vit dans
`product/assets/PARITE.md`, tenu par un test.

Un port n'est **jamais fini** tant que cette table n'est pas verte. Un
geste non porté n'est pas un oubli : c'est une TASK, ou une raison
écrite en toutes lettres.

Skills : `portage` choisit la cible et écrit le port ; `parite` vérifie
qu'il dit tout ce que la source dit.

---

## Conventions d'ID

Format strict : `<TYPE>-nnn` — exactement 3 chiffres, zéros inclus.
`ADR-001`, jamais `ADR-1` ni `ADR-0001`. Le hook rejette tout le reste.

IDEA-nnn    product/ideas/                idée, à n'importe quel stade
SPEC-nnn    product/specs/                comportement attendu, testable
BRIEF-nnn   product/specs/briefs/         spec compilée, prête à exécuter
ADR-nnn     product/decisions/            décision + alternatives écartées
DOM-nnn     product/domain/               fait de domaine, sourcé
TRC-nnn     product/domain/traces/        observation publique, sourcée, datée
SUG-nnn     product/domain/suggestions/   hypothèse retenue, non validée
INT-nnn     product/domain/interviews/    échange avec un expert
COPY-nnn    product/copy/                 texte destiné à l'utilisateur final
PROMPT-nnn  product/assets/prompts/       prompt de génération visuelle
TASK-nnn    backlog/tasks/                unité d'implémentation

Hors graphe — le hook les ignore (ni ID, ni frontmatter attendus) :
`product/grill/`, `product/legal/`,
`product/assets/DESIGN.md`, `product/JOURNAL.md`, `AMELIORATIONS.md`.

Avant d'attribuer un ID : lire `product/INDEX.md`, y compris la section
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

### Champs supplémentaires obligatoires
TASK    phase: local | pilote | dur
        origine: feature-build     (si la trace a été écrite après le code)
IDEA    origine: utilisateur | agent   contexte: <où l'idée est née>
DOM     source: <URL ou libellé stable>
SUG     question: <la question restée sans réponse>
        appelant: <skill ou agent>   preuve: <vide tant que pending>
TRC     source, type, echantillon        (régime `traces` — voir RIGUEUR.md)
INT     humain: oui | non
COPY    persona: <role>-persona (sauf auto-usage)
PROMPT  outil: <modèle utilisé>

`chemin: court` reste accepté sur une TASK, mais ne sert plus à
contourner un blocage : il n'y en a plus.

---

## Règles de graphe

Ce sont des constats, pas des barrières. Le hook les liste dans
`! Incohérences` ; rien ne s'arrête.

- Une SPEC cite l'IDEA dont elle vient.
- Un BRIEF cite au moins une SPEC.
- Une TASK cite une SPEC ou un BRIEF — sauf si elle porte
  `origine: feature-build | portage | parite` (trace écrite après le
  code, ou port d'un produit déjà spécifié) ou
  `chemin: court`. Le hook lit ces deux champs et dispense ; sans eux,
  il signale.
- Un COPY cite la SPEC ou l'IDEA qu'il sert.
- Un PROMPT cite le COPY ou la SPEC qui le motive.
- Un fait sans source est `[SUPPOSÉ]`, pas un DOM.
- Un BRIEF `ready` est immuable — une correction crée BRIEF-nnn+1 qui
  référence l'ancien.

### Hypothèses
Une option choisie dans une liste proposée par `suggester` reste
`[SUPPOSÉ]`. La cocher ne la transforme pas en fait.

  pending    retenu, sans preuve — **ne freine rien**
  validé     un TRC/INT/DOM postérieur le confirme (renseigner `preuve:`)
  invalidé   une preuve postérieure le contredit
  abandonné  l'option n'est plus dans le projet

Tout objet dont une décision repose sur un SUG `pending` le déclare dans
`links:`. C'est ce lien qui rend la dette visible — visible, pas bloquante.

---

## Recherche en ligne
Chercher librement. Ce qui est trouvé est écrit en DOM (ou TRC) avant
d'être utilisé, jamais gardé en tête. Priorité de sources : régulateur,
opérateur, documentation officielle, avant blogs et comparatifs.

Demander l'autorisation seulement si la recherche va coûter plusieurs
tours, ou sortir du sujet en cours.

---

## Design

Avant le premier écran : skill `design-direction`. Elle écrit
`product/assets/DESIGN.md` (tokens, composants, ce qu'on ne fait jamais)
à partir de 3 à 5 produits réels du domaine.

Tout écran est confronté à `DESIGN.md` avant d'être écrit. Un écran qui
s'en écarte s'écarte volontairement, et le dit.

`phase_guard.py` refuse tout fichier d'écran sous `src/` tant que
`DESIGN.md` est absent. Ce n'est pas un avertissement.

---

## Archivage
Va dans `product/archive/` (sous-chemin d'origine conservé) :
IDEA killed, SPEC/BRIEF caducs, SUG abandonné, TRC dont la source a disparu.

N'y va JAMAIS : un ADR (une décision reste vraie même remplacée — marquer
`status: remplacé par ADR-nnn`), un INT, un DOM (une observation ne
devient pas fausse, elle vieillit).

On archive, on ne supprime pas. Le frontmatter reste intact.

---

## Navigation
`product/INDEX.md` est régénéré par `.claude/hooks/graph_index.py` aux
événements SessionStart et Stop. Ne jamais l'éditer à la main.
La skill `graph-index` sert à LIRE l'index et à réparer le graphe.

Ouvrir `product/` comme coffre Obsidian : les `[[ID]]` deviennent
cliquables, la vue graphe est native.

---

## Répartition avec Superpowers

Ce dépôt gère l'AMONT : quoi construire, pourquoi, dans quel ordre.
Superpowers gère l'AVAL : comment le construire correctement.

- En phase `local`, `feature-build` construit directement. Superpowers
  n'est pas convoqué pour un écran de démo.
- En phase `pilote` et au-delà, un BRIEF `ready` passe la main à
  Superpowers via `/write-plan` ou `/execute-plan`, jamais en paraphrasant
  le BRIEF dans le chat.
- Retour : TASK `done`, BRIEF `shipped`. Si l'implémentation révèle un
  manque, capturer en IDEA — ne pas patcher un BRIEF `ready`.

Ce qu'on ne réécrit jamais : TDD, débogage systématique, revue en deux
temps, sous-agents, plans d'exécution. Toute skill locale qui recouvre
ça est à supprimer — le hook le signale.

Collision de vocabulaire : `/brainstorm` de Superpowers raffine une
exigence avant code ; nos grills décident s'il faut construire.

---

## Budget de contexte au SessionStart
Superpowers et notre hook injectent tous les deux. Le nôtre tient en
4 lignes quand tout va bien, jusqu'à 8 quand plusieurs constats tombent.
Si le SessionStart devient lourd, retirer le hook `Stop` avant de
toucher au `SessionStart`.
