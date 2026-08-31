---
name: feature-build
description: Le chemin par défaut. Transforme une feature exprimée en écran
  ou comportement qui tourne, dans le même tour. Déclencher sur "je veux
  que", "ajoute", "l'écran doit", "il faut pouvoir", "fais que", ou toute
  demande de fonctionnalité en phase local. Construit d'abord, trace après.
---

# Construire une feature

## Pourquoi cette skill existe
Le mode non structuré — ouvrir Claude Code et donner ses features une à
une — produit de meilleurs résultats que le circuit long. C'est l'étalon.
Cette skill rend ce mode officiel au lieu de le laisser contourner le
processus. La traçabilité s'écrit à la fin, pas au début.

## Quand NE PAS l'utiliser
Le critère est la **réversibilité dans la phase courante**, pas le sujet.
« Toucher à l'authentification » n'est pas dangereux en soi ; le devenir
quand quelqu'un d'autre en dépend, oui.

Passer par le circuit long (idea-grill → spec-compiler) si, et seulement
si, l'une de ces trois choses est vraie :
- **quelqu'un d'autre dépend déjà** de ce que tu vas changer : un
  contrat de données consommé ailleurs, un format d'échange publié, une
  API dont un tiers se sert ;
- **l'annuler coûterait plus qu'un `git revert`** : une migration, un
  avertissement à envoyer, de l'argent réel déjà déplacé ;
- la phase est `pilote` ou au-delà **et** la feature touche quelque chose
  qui ne se reprend pas : une valeur qui bouge, l'authentification, des
  données personnelles réelles.

En phase `local`, aucune de ces trois n'est vraie par construction :
personne d'autre ne dépend de rien, et rien n'est déployé. Construire.

**Contredire un ADR n'est pas un motif de circuit long** — c'est un
motif d'écrire un ADR. Voir la procédure dans `product-owner` : une
ligne pour dire lequel est contredit, un ADR nouveau qui le lève, et on
construit. Ne jamais s'arrêter pour demander l'autorisation de changer
un périmètre que l'utilisateur vient lui-même de changer en demandant.

---

## Procédure

### 1. Reformuler en une ligne d'accord — puis avancer
`Compris : <feature en une phrase, résultat observable>.`
Une seule ligne. Ne pas poser de question si la réponse ne change pas ce
qui va être écrit. Choisir un défaut raisonnable et le marquer `[SUPPOSÉ]`
dans la TASK.

### 2. Vérifier le socle avant d'écrire un écran
- `product/assets/DESIGN.md` existe ? Sinon → invoquer `design-direction`
  MAINTENANT. Le hook refusera le fichier autrement.
- `src/` existe ? Sinon → invoquer `software-architect` (mode scaffolding).
  Il ne demande ni BRIEF ni preuve.

### 3. Construire
- Le plus petit chemin qui rend la feature **visible et manipulable**.
- Chaque écran est confronté à `DESIGN.md` avant d'être écrit : tokens,
  composants existants, états d'erreur et de chargement.
- Réutiliser les composants déjà présents. En créer un nouveau est une
  décision, pas un réflexe.

### 4. Tester ce qui coûte cher — pas le reste
En phase `local`, écrire un test seulement si l'un des cas s'applique :
- un **invariant métier** (unicité, idempotence, conservation d'une
  quantité, transition d'état interdite)
- une **erreur qui ne se rattrape pas** : un geste joué deux fois, un
  enregistrement perdu, un statut faux
- un bug qu'on vient de corriger — le test empêche le retour

Ne pas tester : le rendu, le formatage, les getters, les cas que le
compilateur attrape déjà.

### 5. Montrer
Terminer par la commande exacte qui fait tourner la chose, et ce qu'on
doit voir. Vérifier soi-même que ça tourne avant de le dire.

### 6. Tracer — après, jamais avant
Écrire `backlog/tasks/TASK-nnn.md`, `status: done` :

---
id: TASK-nnn
title: <résultat observable, pas une activité>
status: done
phase: local
origine: feature-build
links: [<ADR/DOM/IDEA/SPEC qui existaient déjà, sinon vide>]
updated: AAAA-MM-JJ
---
## Fini quand
- <ce qui est vrai maintenant, vérifiable par exécution>
## Hors périmètre de cette tâche
- <ce qui n'a PAS été fait — minimum 1>
## [SUPPOSÉ]
- <les défauts choisis sans demander>

`origine: feature-build` n'est pas décoratif : c'est ce champ qui dispense
la TASK de parent SPEC/BRIEF dans le hook. Sans lui, elle est signalée
orpheline à chaque ouverture de session, et l'alerte devient du papier
peint. Le hook compte ces TASK à part — visible, jamais reproché.

Si un choix structurant a été fait en chemin (un contrat, un format, une
dépendance) → écrire aussi un ADR. Court : décision, alternatives
écartées, ce qui la ferait changer.

---

## Sortie — ≤ 8 bullets, format fixe

## Fait — <la feature, une ligne>
## Fichiers
- <chemins créés ou modifiés>
## Tourne avec
- `<commande>` → <ce qu'on doit voir>
## Testé
- <l'invariant couvert, ou "aucun test — rien de coûteux ici">
## ! Choisi sans demander
- <les [SUPPOSÉ], ou "rien">
## → Suite
- <la feature suivante la plus évidente, une seule>

---

## Interdits
- Poser plus d'une question avant d'écrire du code.
- Demander une preuve, une interview, une validation de marché.
- Attendre un BRIEF, une SPEC ou un verdict de grill.
- Écrire un test par fonction en phase `local`.
- Écrire la TASK avant le code — c'est exactement ce qu'on corrige.
- Annoncer que ça tourne sans l'avoir exécuté.
- Enchaîner sur une deuxième feature non demandée.
