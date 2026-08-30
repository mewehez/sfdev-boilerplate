---
name: project-grill
description: Ouverture d'un nouveau projet. Commence par capturer la VISION
  PRODUIT — features, écran principal, parcours — puis cadre le périmètre.
  Déclencher sur "nouveau projet", "j'ai une idée de projet", "on démarre".
  Ne rend aucun verdict et ne bloque rien.
---

# Ouverture de projet

Ce grill sert à savoir **quoi construire**, pas à décider s'il faut le
construire. La décision est déjà prise : l'utilisateur est là.

## Interdits
- Poser une question de validation (marché, concurrence, interviews,
  business model) avant l'ÉTAPE 2. Elles n'arrivent qu'en mode rigueur.
- Enchaîner plusieurs questions dans un tour.
- Écrire ou écraser CLAUDE.md, les skills, les agents, les hooks.
- Rendre un verdict GO/NO-GO. Il n'y en a plus en `exploration`.

---

## ÉTAPE 0 — Vérifier le socle
Contrôler : `CLAUDE.md`, `.claude/hooks/graph_index.py`,
`.claude/hooks/phase_guard.py`, `.claude/skills/`, `product/`, `backlog/`.
Manquant → `! Boilerplate incomplet` + la liste. Ne rien créer pour
compenser.

---

## ÉTAPE 1 — Vision produit  ← EN PREMIER, TOUJOURS

**Mode capture.** On écoute. On ne challenge pas, on ne réduit pas, on ne
propose pas d'alternative. Une question par tour, dans cet ordre :

1. **Le produit en une phrase** — pour QUI, quel PROBLÈME, à quel MOMENT.
2. **Les features de la v1** — « qu'est-ce que l'application sait faire ?
   Liste-les, même en vrac. » Ne pas s'arrêter à trois : relancer une fois
   avec `? Autre chose ?`
3. **L'écran principal** — « quand tu l'ouvres, tu vois quoi ? Qu'est-ce
   qui est en haut, qu'est-ce qui domine, quelle est l'action évidente ? »
4. **Le parcours en 5 étapes** — du premier contact au résultat.
   Faire écrire les 5, numérotées. S'il en manque, demander laquelle.
5. **Ce qui doit exister en v1** — la liste minimale sans laquelle on ne
   peut pas montrer le produit.
6. **Ce qui n'existera PAS en v1** — exiger 3 exclusions. C'est la seule
   question de cadrage de cette étape, et elle protège la suite.

Si l'utilisateur sèche sur une question → dispatcher `suggester`.
S'il répond partiellement → prendre ce qu'il donne, marquer le reste
`[SUPPOSÉ]`, avancer. Ne pas insister deux fois.

Consigner au fil de l'eau dans `product/grill/AAAA-MM-JJ-vision.md`
(hors graphe : pas de frontmatter, pas d'ID).

### Restitution — ≤ 12 bullets
## Produit — <une phrase>
## Features v1 — <la liste, verbatim>
## Écran principal — <ce qu'on voit, dans l'ordre de lecture>
## Parcours — <les 5 étapes>
## Dehors — <les 3 exclusions>
## ! Ce que j'ai supposé — <ce qu'il n'a pas dit>

`? C'est bien ça ? Corrige ce qui est faux.`

---

## ÉTAPE 2 — Questions de validation

**Sautée en `exploration`** — c'est-à-dire par défaut, et c'est voulu.
On construit d'abord ; un visuel sert justement à approcher les gens.

Elles ne s'appliquent que si `ADR-002` déclare `traces` ou `terrain`.
La liste et le format de verdict sont dans `.claude/optional/RIGUEUR.md`.

En `exploration`, une seule ligne, sans y revenir :
`Hypothèses non vérifiées — tracées, pas bloquantes. On construit.`

---

## ÉTAPE 3 — Cadrage technique

Une question par tour.

3.1 **Surfaces** : web / mobile / desktop / API / CLI ? Laquelle en premier ?
3.2 **Utilisateur unique ou multi-rôles ?**
3.3 **Contraintes matérielles du terrain** — appareil, connexion, langue,
    luminosité. C'est ce qui écrit le design, pas une démographie.
3.4 **Stack** — proposer ce que l'utilisateur maîtrise déjà, sauf raison
    explicite. Signaler `!` toute techno nouvelle pour lui.
3.5 **Ce qui doit tourner d'ici la fin de la session** pour qu'on ait
    quelque chose à montrer.

→ écrire `product/decisions/ADR-001-perimetre.md` (features v1, exclusions,
surface première, rôles, contraintes de terrain, cible de session).

---

## ÉTAPE 4 — Bootstrap, puis construire

Écrire, sans demander d'approbation :
- `ADR-001-perimetre.md` (ÉTAPE 3)
- `ADR-002-regime-preuve.md` avec la ligne exacte, dans le corps :
      regime: exploration
  et une phrase : « ce que ça coûte de se tromper, aujourd'hui ».
- une `IDEA-nnn` `status: raw`, `origine: agent`, `contexte: project-grill`
  par branche non explorée repérée pendant l'ÉTAPE 1. Elles rejoignent la
  file de grill, elles n'attendent personne.

Ne PAS créer : `src/`, `CLAUDE.md`, `.claude/skills/`, `.claude/hooks/`,
`.claude/settings.json`.

Puis **enchaîner immédiatement**, dans le même tour :
1. `design-direction` (mode ÉTABLIR) → `product/assets/DESIGN.md`
2. `software-architect` (mode SCAFFOLDING) → `src/`
3. `feature-build` sur la première feature de la liste v1

## Sortie — ≤ 6 bullets
## Vision capturée — <N features, parcours en 5 étapes>
## Périmètre — ADR-001 | Régime — exploration
## Idées en file — <les IDs>
## → J'enchaîne sur design-direction, puis le squelette, puis <feature 1>

Ne pas rendre la main ici. Le bootstrap n'est pas un livrable.
