# sfdev-boilerplate

Un socle de développement piloté par agents pour Claude Code.

**Ce qu'il fait, en une phrase :** tu exprimes une idée, Claude construit
le produit, et la trace de ce qui a été décidé s'écrit toute seule
derrière.

Pas de validation de marché, pas de preuve à fournir, pas de verdict à
franchir. Le seul ordre imposé est celui qui évite de perdre du temps :
l'app tourne d'abord, on la montre ensuite, le juridique vient en dernier.

---

## Démarrage

```bash
./sfdev-new.sh
```

Le script demande le nom du projet et où le poser, copie le socle sans
son historique git, initialise un dépôt neuf, et affiche la phrase exacte
à dire à Claude Code pour démarrer.

Puis, dans le dossier créé :

```bash
claude
```

et tu dis : `nouveau projet` — ou directement ta première feature.

---

## Comment ça se passe, concrètement

**Session 1 — l'idée devient un écran**

1. Tu dis `nouveau projet`.
2. Claude te demande **ce que l'application fait** : les features, ce
   qu'on voit sur l'écran principal, le parcours en 5 étapes, ce qui
   n'existera pas en v1. Il écoute, il ne challenge pas.
3. Il regarde 3 à 5 produits réels du même domaine et en tire une
   direction de design (`product/assets/DESIGN.md`).
4. Il pose le squelette du projet.
5. Il construit la première feature. Ça tourne à la fin de la session.

**Ensuite — les features au fil de l'eau**

Tu dis `je veux que…`, `ajoute…`, `l'écran doit…`. Claude construit,
puis écrit la trace. Dans cet ordre, jamais l'inverse.

**Quand tu ne sais plus quoi faire**

Tu dis `des idées de features ?`. Claude lit ce qui existe déjà — les
faits de domaine, le parcours réel, les décisions prises — et propose
**trois choses au maximum**, chacune tirée du produit et non d'une liste
générique. Celles que tu ne retiens pas sont capturées, rien ne se perd.

**Une idée qui passe**

Tu dis « et si on… » au milieu d'autre chose. Elle est capturée en trois
lignes et **la tâche en cours reprend**. Elle t'attend dans la file.
Tu dis `on grille` quand tu veux la trancher.

---

## Les trois phases

Chaque tâche porte une phase. C'est la seule contrainte d'ordre du socle,
et elle est tenue par un hook, pas par une règle de bonne conduite.

| phase | ce qu'elle contient |
|---|---|
| `local` | ce qui fait tourner l'app sur ta machine |
| `pilote` | ce qu'il faut pour la montrer à quelqu'un de réel |
| `dur` | forme juridique, nom de domaine, hébergement, conformité, CGU |

**Aucune tâche `dur` ne peut s'ouvrir tant qu'une tâche `local` est
ouverte.** Un hook refuse l'écriture. Le juridique produit des templates
à trous, jamais des blocages.

C'est là pour une raison précise : sans ça, un déploiement en zone UE
sort en tâche n°2 et la conformité sature la conversation avant que quoi
que ce soit ne tourne.

---

## Le web est le lieu du développement

Une feature se développe **sur le web**. Le mobile et le desktop ne font
que le **porter** — ils n'ajoutent jamais un comportement que le web n'a
pas.

Un cycle web dure quelques secondes ; un cycle natif, quelques minutes.
Développer dans le port multiplie ce coût par le nombre d'essais. Et une
feature écrite deux fois diverge toujours.

Le portage est de phase `pilote` : la skill `portage` choisit la cible
(PWA, puis Capacitor si une capacité native manque, Tauri pour le
desktop) et emballe. Elle ne développe rien.

---

## Ce qui bloque vraiment

Trois refus, trois seulement. Ils portent sur l'**ordre**, jamais sur la
preuve. Ils sont dans `.claude/hooks/phase_guard.py` et ils refusent
l'écriture du fichier — ce ne sont pas des avertissements.

1. **Tâche `dur` avant que `local` soit fini** → refusée.
2. **Écran sous `src/` sans `product/assets/DESIGN.md`** → refusé.
   Un écran écrit sans direction de design produit une interface
   incohérente. Établir la direction prend un tour.
3. **Fichier sous `mobile/`, `desktop/`, `ios/` ou `android/` avant que
   `local` soit fini** → refusé. Porter une application inachevée, c'est
   la porter deux fois.

Un refus se lève en faisant la chose dans le bon ordre.

---

## Ce qu'il y a dans le dossier

```
CLAUDE.md                    les règles, chargées à chaque session
sfdev-new.sh                 le script de démarrage
AMELIORATIONS.md             journal des frictions rencontrées

.claude/
  skills/                    instructions chargées dans ta session
    project-grill            ouverture d'un projet — vision produit d'abord
    feature-build            LE chemin par défaut : feature → écran qui tourne
    design-direction         direction de design, puis rôle d'UX/UI senior
    portage                  emballe le web en PWA, app mobile ou desktop
    software-architect       pose src/, choisit la stack
    feature-scout            propose des features quand tu es à court d'idées
    idea-grill               capture une idée sans casser ce qu'on fait
    spec-compiler            compile une SPEC en brief exécutable (phase pilote)
    domain-expert            cherche et écrit les faits du domaine
    copywriting              les textes vus par l'utilisateur final
    visual-prompt            les prompts d'images, versionnés
    graph-index              lire et réparer le graphe

  agents/                    instances séparées, contexte vierge
    design-critic            confronte un écran au DESIGN.md, sans indulgence
    product-owner            décide de l'ordre, crée les tâches
    suggester                débloque une question sans réponse
    persona-TEMPLATE         gabarit d'un utilisateur simulé

  hooks/
    graph_index.py           régénère product/INDEX.md — constate, ne range pas
    phase_guard.py           les deux refus ci-dessus

  optional/
    RIGUEUR.md               la couche exigeante, DÉSACTIVÉE par défaut

product/                     tout le travail amont, versionné
  ideas/  specs/  decisions/  domain/  copy/  assets/  grill/  archive/
backlog/tasks/               les tâches
src/                         le code (créé au premier scaffolding)
```

---

## Le graphe

Chaque fichier de `product/` porte un ID (`IDEA-001`, `SPEC-004`,
`ADR-002`…) et des liens vers ceux dont il dépend. Un hook régénère
`product/INDEX.md` à chaque session et à chaque fin de tour : ce qui
existe, ce qui est ouvert, ce qui est incohérent.

Le hook **constate**. Il ne crée aucun dossier, ne déplace aucun fichier,
et ne bloque rien — le blocage, c'est l'autre hook, et il ne fait que deux
choses.

Pour voir le graphe : ouvre `product/` comme un coffre Obsidian. Les
`[[ID]]` deviennent cliquables et la vue graphe est native.

Questions utiles à Claude : `où on en est`, `qu'est-ce qui est orphelin`,
`d'où vient SPEC-004`.

---

## Passer en mode exigeant

Par défaut, le socle tourne en `exploration` : on construit sur
l'intuition et la recherche en ligne, les hypothèses sont tracées mais ne
freinent rien.

Le jour où une piste se confirme — de l'argent réel, du réglementaire, la
confiance de quelqu'un d'autre — une ligne suffit, dans le corps de
`product/decisions/ADR-002-regime-preuve.md` :

```
regime: traces
```

Ça réactive les exigences de preuve, les personas adossés à des
observations, et le blocage des briefs mal sourcés. Le mode d'emploi
complet est dans `.claude/optional/RIGUEUR.md`. Pour revenir :
`regime: exploration`.

---

## Superpowers

Le socle gère l'**amont** — quoi construire, pourquoi, dans quel ordre.
Le plugin Superpowers gère l'**aval** — TDD, revue, exécution.

Installation :

```
/plugin install superpowers@claude-plugins-official
```

En phase `local`, Superpowers n'est pas convoqué : `feature-build`
construit directement et ne teste que les invariants qui coûtent cher.
Le TDD complet démarre en phase `pilote`, à partir d'un brief `ready`.

! Superpowers charge par défaut un logo distant qui transmet sa version.
`SUPERPOWERS_DISABLE_TELEMETRY` le désactive — à poser dans
l'environnement du projet.

! Superpowers et notre hook injectent tous les deux du contexte au
démarrage de session. Le nôtre tient en 4 à 8 lignes. Si le démarrage
devient lourd, retirer le hook `Stop` de `.claude/settings.json` avant de
toucher au `SessionStart`.

---

## Performance

Le hook `Stop` régénère l'index après chaque tour. Sur un graphe de
quelques centaines de fichiers c'est imperceptible ; au-delà du millier,
retire-le et garde `SessionStart` seul.

---

## Prérequis

- Claude Code
- Python 3 (les hooks n'ont aucune dépendance externe)
- git
