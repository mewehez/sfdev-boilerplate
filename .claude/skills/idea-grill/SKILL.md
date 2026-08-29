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
- Une idée arrive → **CAPTURE**. Toujours. Même si elle semble évidente,
  même si elle est minuscule, même si on vient d'en parler.
- L'utilisateur demande explicitement d'arbitrer → **GRILL**.
- En cas de doute → CAPTURE. Capturer à tort coûte trois lignes ;
  griller à tort coûte une session d'attention.

---

# MODE CAPTURE

Ne jamais interrompre ce qu'on est en train de faire.

## Procédure
1. Lire `product/INDEX.md` pour le prochain IDEA-nnn libre.
2. Vérifier le doublon : grep le titre dans `product/ideas/`.
   Si l'idée existe déjà → ajouter une ligne au fichier existant et
   répondre `IDEA-nnn enrichie. On reprend.`
3. Sinon, écrire `product/ideas/IDEA-nnn.md` :

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

## Interdits du mode CAPTURE
- Reformuler l'idée pour la rendre "meilleure". Le verbatim est la donnée.
- Ajouter analyse, coût, estimation, avis.
- Demander une clarification. Si c'est flou, c'est flou —
  `? Non tranché` existe pour ça.
- Créer une SPEC ou une TASK.
- Enchaîner sur "veux-tu qu'on l'implémente ?"
- Basculer en mode GRILL sans que l'utilisateur l'ait demandé.

---

# MODE GRILL

## G0 — Vider la file
1. Lire `product/INDEX.md` § File de grill.
2. Afficher ≤ 8 bullets, la plus ancienne en premier :
   `IDEA-nnn — <titre> (capturée le JJ/MM, contexte : <...>)`
3. `? On commence par laquelle, ou dans l'ordre ?`
4. Griller UNE idée, rendre le verdict, puis s'arrêter :
   `IDEA-nnn → <verdict>. Reste N dans la file. On continue ? (o/n)`

Ne jamais enchaîner sans redemander. Le grill consomme de l'attention,
et l'attention est la ressource rare.

## G1 — Grill d'une idée
Convoquer par sous-agents, selon le régime de preuve d'ADR-002 :
- `domain-expert` — ce problème existe-t-il vraiment dans le domaine ?
- `<role>-persona` — sauf en régime auto-usage : le vivrais-tu ?
  que fais-tu aujourd'hui à la place ?
- `product-owner` — qu'est-ce que ça déclasse dans le backlog ?
- `software-architect` — ça casse quelle décision existante ?

En régime auto-usage, tu remplaces le persona par une question directe :
`? Tu l'as vécu combien de fois cette semaine ?`

Si une question reste sans réponse → convoquer `suggester`.

## G2 — Verdict (≤ 12 bullets)

## IDEA-nnn — <titre>
## Ce que ça résout        (1 bullet ; si vide → killed)
## Preuve                  (DOM-nnn / TRC-nnn / INT-nnn, ou `[SUPPOSÉ]`)
## ! Coût réel             (ce que ça complexifie durablement)
## Ce que ça déclasse
## Verdict : specd | parked | killed
## ? La question qui décide  (une seule, obligatoire si parked)

`parked` est le verdict par défaut.
Une idée parquée garde sa raison de parcage — c'est elle qu'on relit
pour la dégeler, pas l'idée.

Mettre à jour le `status:` du fichier IDEA. Un `killed` part dans
`product/archive/` — le hook l'exclut du graphe et garde l'ID réservé.

## G3 — Si specd
- créer SPEC-nnn, `links: [IDEA-nnn, DOM-nnn | TRC-nnn | INT-nnn]`
- ne pas créer de TASK : c'est `product-owner` qui décide du moment
- ne pas compiler : c'est `spec-compiler` qui produit le BRIEF

## G4 — Dégel d'une parquée
Une idée `parked` ne revient pas parce qu'elle est vieille. Elle revient
quand sa `? La question qui décide` a trouvé sa réponse.
Sur "dégèle les idées parquées" : lister uniquement celles dont la
question décisive est désormais couverte par un DOM, TRC ou INT récent.
Si aucune → le dire en une ligne, ne pas proposer de dégeler quand même.

## Interdits du mode GRILL
- Griller une idée qui n'a pas été capturée d'abord.
- Griller plusieurs idées sans redemander entre chaque.
- Transformer un `[SUPPOSÉ]` en preuve parce que l'idée plaît.
- Rendre un verdict `specd` sans au moins une ligne dans "Preuve".