---
name: project-grill
description: Interrogatoire d'ouverture d'un nouveau projet. Déclencher sur
  "nouveau projet", "j'ai une idée de projet", "grill". Produit un verdict
  GO/NO-GO, puis (si GO) le cadrage, puis la proposition d'agents, skills
  et stack. Aucune arborescence n'est créée avant le verdict.
---

# Grill de projet

## Interdits
- Proposer une solution, une feature, une techno avant l'ÉTAPE 3.
- Enchaîner plusieurs questions dans un tour.
- Traiter une réponse invérifiée comme un fait. Marquer `[SUPPOSÉ]`.

---

## ÉTAPE 1 — Compréhension (avant tout verdict)

Poser dans cet ordre, une par tour :

1. Le projet en une phrase : pour QUI, quel PROBLÈME, à quel MOMENT.
2. Pourquoi ce problème mérite d'être résolu ? Que coûte-t-il
   aujourd'hui à celui qui le vit ?
3. Qui le vit exactement ? (rôle, contexte, volume, pas une démographie)
4. Que font-ils aujourd'hui à la place ?
5. Qui résout déjà ça ? → chercher, ne pas demander à l'utilisateur.
   Présenter les acteurs trouvés, puis : "pourquoi te choisirait-on ?"
   Refuser "je ferai mieux". Exiger un mécanisme.
6. Quelle contrainte externe tue le projet si elle bouge ?
   (réglementation, plateforme tierce, infra publique, échéance datée)
7. Qui paie, combien, contre quoi ?
8. Combien de personnes concernées as-tu interrogées ? (chiffre)

Chaque réponse va dans product/grill/AAAA-MM-JJ-session-NN.md au fil de l'eau.

---

## ÉTAPE 2 — Verdict (sortie obligatoire, ≤ 15 bullets)

## Verdict : GO | GO_ÉTROIT | TERRAIN_D'ABORD | NO-GO
## Pourquoi  (3 bullets max, faits sourcés)
## ! Ce qui ne tient pas  (les objections, sans adoucissement)
## [SUPPOSÉ] à valider  (minimum 3)
## → Prochaine action non-code

Règles de verdict :
- interviews = 0  →  TERRAIN_D'ABORD par défaut.
- un acteur en place fait déjà exactement ça, sans différenciateur
  mécanique  →  NO-GO.

Puis : "Tu peux passer outre. Si tu le fais, donne-moi ta raison —
je l'écris."
Si l'utilisateur passe outre : créer ADR-000 avec le verdict, ses
objections intactes, et la raison de l'utilisateur. Ne jamais réécrire
le verdict pour le rendre compatible avec la décision.

STOP ici si NO-GO non levé.

---

### ÉTAPE 3.0 — Régime de preuve (AVANT toute autre question de cadrage)
Poser : "Si tu te trompes sur ce projet, qu'est-ce que ça coûte ?"
- rien, c'est pour toi et tu es l'utilisateur      → auto-usage
- du temps perdu, rattrapable                       → traces
- l'argent ou la confiance de quelqu'un d'autre,
  du réglementaire, de l'irréversible                → terrain

Écrire product/decisions/ADR-002-regime-preuve.md avec, en frontmatter
du corps, la ligne exacte :
  regime: auto-usage | traces | terrain
Le hook lit cette ligne. Sans elle, tout le système marche à l'aveugle.

## ÉTAPE 3 — Cadrage (uniquement après GO ou levée)

Une question par tour :
1. Périmètre v1 : qu'est-ce qui est DEHORS ? (exiger 3 exclusions)
2. Surfaces : web / mobile / desktop / API / CLI ? Laquelle en premier ?
3. Utilisateur unique ou multi-rôles ?
4. Données sensibles, conformité, hébergement contraint ?
5. Toi seul, ou d'autres contributeurs à terme ?
6. Ce qui doit tourner en 2 semaines pour que tu saches si ça marche.

→ écrire product/decisions/ADR-001-perimetre.md

---

## ÉTAPE 4 — Proposition d'outillage (≤ 20 bullets, format tableau)

Proposer, avec une justification d'une ligne chacun :

| Agent/Skill | Pourquoi ce projet en a besoin |
Toujours : domain-expert, idea-grill, software-architect, graph-index
Conditionnels : compliance-reviewer (si réglementé),
  <role>-persona (un par rôle utilisateur identifié en 3.3),
  data-modeler (si domaine métier riche), ops-reviewer (si prod critique)

| Stack dev | Stack prod | Justification |
Contrainte : proposer ce que l'utilisateur maîtrise déjà, sauf raison
explicite. Signaler `!` toute techno nouvelle pour lui.

Attendre approbation explicite avant l'étape 5.

---

## ÉTAPE 5 — Bootstrap
- créer CLAUDE.md, product/, backlog/, .claude/
- instancier les agents approuvés, remplis avec les faits de l'étape 1
  uniquement — jamais d'invention
- chaque branche non explorée repérée pendant le grill → un IDEA-nnn
  `status: raw`, `origine: agent`, `contexte: project-grill`.
  Elles rejoignent la file de grill. Pas de fichier d'arbre séparé.
- NE PAS créer src/. C'est le rôle de software-architect, plus tard.