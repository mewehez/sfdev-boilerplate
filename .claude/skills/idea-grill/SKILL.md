---
name: idea-grill
description: Gère le cycle de vie d'une idée, de son apparition à son
  verdict. Deux modes. CAPTURE — déclencher dès qu'une idée surgit
  ("et si on", "idée :", "ce serait bien de", "note ça", ou toute
  proposition de feature non demandée, y compris venant de moi).
  GRILL — déclencher sur "on grille", "quelles idées restent",
  "file de grill", "dégèle les parquées".
---

# Idées

## Règle d'or
Une idée qui arrive n'est PAS une tâche. Capture ≠ décision.
Jamais d'implémentation dans le tour où une idée apparaît.

## Choix du mode
- Une idée arrive → **CAPTURE**. Toujours. Même minuscule, même évidente.
- L'utilisateur demande explicitement d'arbitrer → **GRILL**.
- En cas de doute → CAPTURE. Capturer à tort coûte trois lignes ;
  griller à tort coûte une session d'attention.

---

# MODE CAPTURE

Ne jamais interrompre ce qu'on est en train de faire.

## Procédure
1. Lire product/INDEX.md pour le prochain IDEA-nnn libre. Prendre en
   compte la section `## IDs réservés — archivés` : un ID qui y figure
   est pris, même s'il n'apparaît pas dans la liste IDEA.
2. Vérifier le doublon **dans les deux sens** : grep le sujet dans
   `product/ideas/` ET dans `backlog/tasks/`.
   - L'idée existe déjà → ajouter une ligne au fichier existant, répondre
     `IDEA-nnn enrichie. On reprend.`
   - **Une TASK ouverte la contient** → le dire avant de commencer :
     `Couverte par TASK-nnn, je l'élargis.` Ce qu'on évite n'est pas du
     travail en double, c'est deux passages sur les mêmes fichiers avec
     deux raisonnements qui divergent — et le second ignore ce que le
     premier a tranché.
3. Sinon, écrire product/ideas/IDEA-nnn.md :

---
id: IDEA-nnn
title: <l'idée en ≤ 10 mots, dans les mots de l'utilisateur>
status: raw
origine: utilisateur | agent
contexte: <où on était : fichier, écran, SPEC en cours>
links: [<SPEC-nnn ou IDEA-nnn parente si évident, sinon vide>]
updated: AAAA-MM-JJ
---

## L'idée
- <une phrase, verbatim autant que possible>

## D'où ça vient
- <ce qu'on faisait quand c'est apparu>

## ? Non tranché
- <la question évidente qu'on n'a PAS posée>

4. Répondre exactement une ligne :
   `IDEA-nnn capturée — <titre>. On reprend.`
5. Reprendre la tâche interrompue au point exact où elle en était.

## Rafale
Plusieurs idées d'un coup → un fichier par idée, puis une seule ligne
listant les IDs. Ne jamais fusionner : deux idées mêlées sont
ingrillables séparément.

## ! Capturer AVANT de proposer

Une suite entrevue ne se propose jamais à l'oral en premier. Elle
s'écrit, puis la question de fin de tour la **désigne par son ID**.

Une proposition orale n'a que deux issues — oui tout de suite, ou perdue.
Écrite d'abord, elle en a trois, et la troisième — « pas maintenant » —
est la plus fréquente. Voir `CLAUDE.md`, § Rien ne se propose qui ne soit
déjà écrit.

## Interdits du mode CAPTURE
- Reformuler l'idée pour la rendre "meilleure". Le verbatim est la donnée.
- Ajouter analyse, coût, estimation, avis.
- Demander une clarification. `? Non tranché` existe pour ça.
- Créer une SPEC ou une TASK.
- Enchaîner sur "veux-tu qu'on l'implémente ?"
- Basculer en mode GRILL sans que l'utilisateur l'ait demandé.

---

# MODE GRILL

## G0 — Vider la file
1. Lire product/INDEX.md § File de grill.
2. Afficher ≤ 8 bullets, la plus ancienne en premier :
   `IDEA-nnn — <titre> (capturée le JJ/MM, contexte : <...>)`
3. `? On commence par laquelle, ou dans l'ordre ?`
4. Griller UNE idée, rendre le verdict, puis s'arrêter :
   `IDEA-nnn → <verdict>. Reste N dans la file. On continue ? (o/n)`

Ne jamais enchaîner sans redemander. Le grill consomme de l'attention,
et l'attention est la ressource rare.

## G1 — Grill d'une idée

Deux mécanismes distincts, ne pas les confondre :

**Skills, invoquées en séquence dans cette session :**
- `domain-expert` — ce problème existe-t-il vraiment dans le domaine ?
- `software-architect` — ça casse quelle décision existante ?
  (consultation seule : il ne scaffolde rien ici)

**Agents, dispatchés en sous-agents :**
- `<role>-persona` — le vivrais-tu ? que fais-tu aujourd'hui à la place ?
  SAUTÉ en régime auto-usage : poser à la place
  `? Tu l'as vécu combien de fois cette semaine ?`
- `product-owner` — qu'est-ce que ça déclasse ?

Si une question reste sans réponse → dispatcher `suggester`.
L'option retenue crée un SUG-nnn `pending` que je dois inscrire dans
les `links:` de la SPEC si l'idée passe en specd. Un SUG `pending` ne
freine rien : il rend la dette visible, c'est tout.

## G2 — Verdict (≤ 12 bullets)

## IDEA-nnn — <titre>
## Ce que ça résout        (1 bullet ; si vide → killed)
## Sur quoi ça repose      (DOM-nnn / TRC-nnn / INT-nnn, ou `[SUPPOSÉ]`)
## ! Coût réel             (ce que ça complexifie durablement)
## Ce que ça déclasse
## Verdict : specd | parked | killed
## ? La question qui décide  (une seule, obligatoire si parked)

`parked` est le verdict par défaut. Une idée parquée garde sa raison de
parcage — c'est elle qu'on relit pour la dégeler, pas l'idée.

Mettre à jour le `status:` du fichier IDEA.
Un `killed` est déplacé dans product/archive/ideas/ — frontmatter intact.
Le hook l'exclut du graphe et réserve l'ID définitivement.

## G3 — Si specd

En phase `local`, ne pas enchaîner sur `spec-compiler` : proposer
`feature-build` directement. Le BRIEF sert la phase `pilote`.

Écrire product/specs/SPEC-nnn.md :

---
id: SPEC-nnn
title: ...
status: specd
links: [IDEA-nnn, <DOM/TRC/INT-nnn>, <SUG-nnn si applicable>]
updated: AAAA-MM-JJ
---

Contraintes vérifiées par le hook (constats, pas blocages) :
- `links:` contient l'IDEA parente, sinon la SPEC est signalée orpheline
- tout SUG pending ayant servi au verdict y figure

Aucune preuve n'est requise en régime `exploration`. Une SPEC adossée à
du `[SUPPOSÉ]` se compile et se construit.

Puis s'arrêter :
- ne pas créer de TASK — c'est `product-owner` qui décide du moment
- ne pas compiler — c'est `spec-compiler` qui produit le BRIEF

## G4 — Dégel d'une parquée
Une idée `parked` ne revient pas parce qu'elle est vieille, mais quand
sa `? La question qui décide` a trouvé sa réponse.
Sur "dégèle les idées parquées" : lister uniquement celles dont la
question décisive est couverte par un DOM, TRC ou INT récent.
Si aucune → le dire en une ligne, ne pas proposer de dégeler quand même.

## Interdits du mode GRILL
- Griller une idée qui n'a pas été capturée d'abord.
- Griller plusieurs idées sans redemander entre chaque.
- Transformer un `[SUPPOSÉ]` en preuve parce que l'idée plaît.
- Refuser un `specd` faute de preuve. Marquer `[SUPPOSÉ]` et avancer.