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

## ÉTAPE 0 bis — Le projet reprend un existant

Déclenchée dès qu'un code, une maquette ou une exploration antérieure
existe et que le nouveau projet part de là. Elle change la nature de
l'ÉTAPE 1, et elle pose une contrainte qui tient jusqu'à la fin.

### Les features ne se demandent pas, elles s'inventorient

Un utilisateur qui a déjà construit ne redit pas ce qu'il a fait : il
répond « tout », ou il cite les trois qu'il a en tête. La liste obtenue
sera **plus courte que le produit**, et le manque ne se verra pas — ni à
la compilation, ni à l'ouverture des écrans. Il se verra le jour où
quelqu'un cherche un écran qui existait.

Donc : **l'inventaire se dérive de la source, jamais de tête.** C'est le
même principe que `parite`, et il se paie de la même façon quand on
l'oublie.

Relever mécaniquement, et consigner dans
`product/grill/AAAA-MM-JJ-inventaire.md` (hors graphe) :
- les écrans — la liste des routes, pas celle dont on se souvient ;
- ce que chaque écran présente ;
- les gestes offerts à l'utilisateur, y compris les barres d'outils ;
- le modèle de données, tel que le schéma le dit ;
- tout référentiel métier codé en dur — c'est souvent l'ossature du
  produit, et c'est ce qui se perd en premier.

### La contrainte : le grill ne retire rien

**L'inventaire fixe le périmètre. Le grill ne travaille que l'UX.**

- Aucune feature inventoriée ne sort du produit. Pas par les personas,
  pas par le cadrage, pas par « ce n'est pas dans le parcours ».
- La question « ce qui n'existera PAS en v1 » cesse d'être une question
  de périmètre : elle devient une question d'**ordre**. Une feature
  repoussée reste due, et le dit.
- Les personas ne sont plus là pour trancher ce qu'on garde. Ils sont là
  pour dire **ce qui manque** à ce qui existe, et **comment le rendre
  utilisable** : ce qu'on ne trouve pas, ce qu'on n'ose pas cliquer, ce
  qu'on ne comprend pas.

Pourquoi cette contrainte et pas la liberté habituelle : un grill part du
principe qu'aucun code n'existe, donc que réduire ne coûte rien. Face à un
existant, réduire coûte **le travail déjà fait**, et l'arbitrage n'est plus
le même. Un grill qui coupe dans un produit construit ne fait pas un
choix : il fait une perte.

`! Si une feature inventoriée paraît vraiment mauvaise, elle ne se retire
pas ici. Elle devient une IDEA, et c'est idea-grill qui la tranche —
au vu de ce qu'elle coûte réellement à défaire.`

---

## ÉTAPE 1 — Vision produit  ← EN PREMIER, TOUJOURS

**Mode capture.** On écoute. On ne challenge pas, on ne réduit pas, on ne
propose pas d'alternative. Une question par tour, dans cet ordre :

1. **Le produit en une phrase** — pour QUI, quel PROBLÈME, à quel MOMENT.
2. **Les features de la v1** — « qu'est-ce que l'application sait faire ?
   Liste-les, même en vrac. » Ne pas s'arrêter à trois : relancer une fois
   avec `? Autre chose ?`
   **Si l'ÉTAPE 0 bis a eu lieu**, cette question ne se pose pas : la
   liste est l'inventaire, et elle ne se raccourcit pas. Demander à la
   place ce qui manque à ce qui existe.
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

## ÉTAPE 1 bis — Incarner les rôles

La vision vient de nommer des rôles. Un rôle nommé et jamais incarné se
fait oublier : la suite du socle le convoque — `idea-grill` le fait
parler, `copywriting` lit ce qu'il ne fera pas, `visual-prompt` s'y
accorde — et ne trouve aucun fichier. C'est ici, et nulle part ailleurs,
qu'on a la vision fraîche et que personne n'attend encore de réponse
d'eux.

**Un persona par rôle qui se sert du produit. Trois au maximum** — au-delà
ils se répondent en chœur et n'apprennent plus rien. Un rôle dont la v1
ne montre aucun écran n'a pas de persona.

Sur un existant (ÉTAPE 0 bis), ils sont convoqués **écran par écran**, et
la question posée n'est jamais « faut-il le garder » mais « qu'est-ce qui
te bloque ici, et qu'est-ce qui manque ».

Pour chacun : copier `.claude/agents/persona-TEMPLATE.md` vers
`.claude/agents/<role>-persona.md`, remplacer `<role>` dans `name:` et
`description:`, remplir les champs.

- **Chaque ligne porte sa source.** En `exploration`, ce sera `[SUPPOSÉ]`
  partout — c'est le régime qui le veut, pas une négligence. Une ligne
  sans source ne s'écrit pas.
- `## Ce qu'il fait aujourd'hui` — **le contournement en premier.** Un
  utilisateur compare toujours à ce qu'il fait déjà, jamais à rien. Un
  persona sans contournement écrit dira oui à tout, et ne servira à rien.
- `## Ce qu'il ne fera pas` — les contraintes dures. Ce champ écrira le
  design plus tard : les autres décrivent, celui-là interdit.
- `## Ce qu'on ignore encore` — les trous, nommés. Jamais vide en
  `exploration`.

**Ne pas interroger l'utilisateur champ par champ.** Il vient de donner
la vision ; il n'a pas ces réponses et les inventerait par politesse.
Les déduire de l'ÉTAPE 1, tout marquer `[SUPPOSÉ]`, et lui montrer le
résultat.

### Restitution — 3 bullets par persona, pas un de plus
## <role>
- fait déjà : <le contournement>
- ne fera pas : <la contrainte dure>
- trou : <ce qu'on ignore et qui compte>

`? Lequel est faux ?` — une question, une seule, puis on avance avec ce
qui reste debout.

! Un persona en `exploration` n'est une source de vérité pour rien. Il
fait apparaître des questions et donne un angle ; il ne tranche aucun
arbitrage et ne se cite pas comme preuve. Le jour où quelqu'un de réel
est rencontré, son `INT-nnn` prime sans discussion.

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
- les `.claude/agents/<role>-persona.md` de l'ÉTAPE 1 bis, s'ils ne sont
  pas déjà écrits.
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
## Personas — <les rôles incarnés, et sur quoi ils sont [SUPPOSÉ]>
## Périmètre — ADR-001 | Régime — exploration
## Idées en file — <les IDs>
## → J'enchaîne sur design-direction, puis le squelette, puis <feature 1>

Ne pas rendre la main ici. Le bootstrap n'est pas un livrable.
