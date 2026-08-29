---
name: project-grill
description: Interrogatoire d'ouverture d'un nouveau projet. Déclencher sur
  "nouveau projet", "j'ai une idée de projet", "on démarre". Produit un
  verdict GO/NO-GO, puis le régime de preuve, le cadrage, et la
  proposition d'outillage. Aucun contenu projet n'est écrit avant le verdict.
---

# Grill de projet

## Interdits
- Proposer une solution, une feature, une techno avant l'ÉTAPE 4.
- Enchaîner plusieurs questions dans un tour.
- Traiter une réponse invérifiée comme un fait. Marquer `[SUPPOSÉ]`.
- Écrire ou écraser CLAUDE.md, les skills, les agents, le hook.
  Ils viennent du boilerplate. Ce grill remplit product/, jamais .claude/
  ni la racine.

---

## ÉTAPE 0 — Vérifier le socle
Contrôler la présence de : CLAUDE.md, .claude/hooks/graph_index.py,
.claude/skills/, product/, backlog/.
Manquant → `! Boilerplate incomplet, je m'arrête.` et lister ce qui manque.
Ne rien créer pour compenser.

---

## ÉTAPE 1 — Compréhension (avant tout verdict)

Une question par tour, dans cet ordre :

1. Le projet en une phrase : pour QUI, quel PROBLÈME, à quel MOMENT.
2. Pourquoi ce problème mérite d'être résolu ? Que coûte-t-il
   aujourd'hui à celui qui le vit ?
3. Qui le vit exactement ? (rôle, contexte, volume — pas une démographie)
4. Que font-ils aujourd'hui à la place ?
5. Qui résout déjà ça ?
   Demander d'abord : `? Je cherche les acteurs en place en ligne ? (o/n)`
   Si oui : chercher, présenter les acteurs, puis
   "pourquoi te choisirait-on ?". Refuser "je ferai mieux", exiger
   un mécanisme. Écrire ce qui est trouvé en TRC.
   Si non : demander à l'utilisateur ce qu'il connaît, marquer `[SUPPOSÉ]`.
6. Quelle contrainte externe tue le projet si elle bouge ?
   (réglementation, plateforme tierce, infra publique, échéance datée)
7. Qui paie, combien, contre quoi ?
8. Combien de personnes concernées as-tu interrogées ? (chiffre)

Consigner au fil de l'eau dans product/grill/AAAA-MM-JJ-session-NN.md
(hors graphe : pas de frontmatter, pas d'ID).

---

## ÉTAPE 2 — Verdict (≤ 15 bullets)

## Verdict : GO | GO_ÉTROIT | TERRAIN_D'ABORD | NO-GO
## Pourquoi  (3 bullets max, faits sourcés)
## ! Ce qui ne tient pas  (les objections, sans adoucissement)
## [SUPPOSÉ] à valider  (minimum 3)
## → Prochaine action non-code

Règles :
- interviews = 0 → TERRAIN_D'ABORD par défaut.
- un acteur en place fait déjà exactement ça, sans différenciateur
  mécanique → NO-GO.

Puis : "Tu peux passer outre. Si tu le fais, donne-moi ta raison —
je l'écris."
Si l'utilisateur passe outre : écrire ADR-000 avec le verdict, les
objections intactes, et sa raison. Ne jamais réécrire le verdict pour
le rendre compatible avec la décision.

STOP ici si NO-GO non levé.

---

## ÉTAPE 3 — Cadrage (après GO ou levée)

Une question par tour.

### 3.1 Régime de preuve — EN PREMIER
`? Si tu te trompes sur ce projet, qu'est-ce que ça coûte ?`
- rien, c'est pour toi et tu es l'utilisateur       → auto-usage
- du temps perdu, rattrapable                        → traces
- l'argent ou la confiance d'autrui, du réglementaire,
  de l'irréversible                                  → terrain

Écrire product/decisions/ADR-002-regime-preuve.md, contenant la ligne
exacte, dans le corps :
  regime: auto-usage | traces | terrain
Le hook lit cette ligne. Sans elle, tout le système marche à l'aveugle.

### 3.2 Périmètre v1 : qu'est-ce qui est DEHORS ? (exiger 3 exclusions)
### 3.3 Surfaces : web / mobile / desktop / API / CLI ? Laquelle en premier ?
### 3.4 Utilisateur unique ou multi-rôles ?
### 3.5 Données sensibles, conformité, hébergement contraint ?
### 3.6 Toi seul, ou d'autres contributeurs à terme ?
### 3.7 Ce qui doit tourner en 2 semaines pour que tu saches si ça marche.

→ écrire product/decisions/ADR-001-perimetre.md (3.2 à 3.7)

---

## ÉTAPE 4 — Proposition d'outillage (≤ 20 bullets)

Déjà présents dans le boilerplate, actifs sans rien faire :
project-grill, idea-grill, spec-compiler, domain-expert, graph-index,
copywriting, visual-prompt, software-architect, product-owner, suggester.
Ne pas les reproposer.

À décider ici :

| Agent à instancier | Condition |
| <role>-persona     | un par rôle de 3.4 — SAUF régime auto-usage |
| compliance-reviewer| si 3.5 signale du réglementaire |

| Stack dev | Stack prod | Justification (une ligne) |
Contrainte : proposer ce que l'utilisateur maîtrise déjà, sauf raison
explicite. Signaler `!` toute techno nouvelle pour lui.

Attendre approbation explicite avant l'ÉTAPE 5.

---

## ÉTAPE 5 — Bootstrap

Écrire UNIQUEMENT sous product/ et .claude/agents/ :
- ADR-000 (si verdict levé), ADR-001, ADR-002 — s'ils ne sont pas
  déjà écrits aux étapes 2 et 3
- les personas approuvés, à partir de persona-TEMPLATE.md, remplis avec
  les faits de l'ÉTAPE 1 uniquement — chaque ligne portant sa source,
  jamais d'invention. Aucun persona en régime auto-usage.
- chaque branche non explorée repérée pendant le grill → un IDEA-nnn
  `status: raw`, `origine: agent`, `contexte: project-grill`.
  Elles rejoignent la file de grill. Pas de fichier d'arbre séparé.

Ne PAS créer : src/, CLAUDE.md, .claude/skills/, .claude/hooks/,
.claude/settings.json.

Puis lancer le hook et rendre la main :
## Bootstrap fait — <N fichiers>
## Régime : <régime>
## → Relance une session pour que le hook prenne le graphe en compte