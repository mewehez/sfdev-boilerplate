# Journal des frictions

Une entrée par friction réellement rencontrée. Rien de spéculatif.

---

## 2026-08-30 — Le grill ne demandait jamais les features

- **Symptôme** : ouverture d'un projet, 8 questions posées, zéro portant
  sur ce que l'application fait. L'utilisateur n'a jamais pu dire ce
  qu'il voyait dans l'écran principal.
- **Cause** : `.claude/skills/project-grill/SKILL.md`, ÉTAPE 1 —
  les 8 questions étaient toutes des questions de validation (qui vit le
  problème, qui résout déjà ça, qui paie, combien d'interviews). Un
  interdit explicite en tête de fichier bloquait toute question produit
  « avant l'ÉTAPE 4 ».
- **Correction** : ÉTAPE 1 devient « Vision produit », en mode capture :
  features v1, écran principal, parcours en 5 étapes, exclusions. On
  écoute, on ne challenge pas. Les questions de validation deviennent
  l'ÉTAPE 2, sautée par défaut, et leur contenu part dans
  `.claude/optional/RIGUEUR.md`.
- **Reste ouvert** : la relance unique sur « autre chose ? » suffit-elle
  à sortir une liste de features complète ? À observer sur un vrai
  démarrage.

---

## 2026-08-30 — Un seul régime, et il bloquait

- **Symptôme** : le système exigeait une preuve avant de laisser passer
  un BRIEF, donc une TASK, donc du code. On construit souvent par
  intuition, ou pour un portfolio — et un visuel sert justement à
  approcher les gens qu'on devrait interviewer. L'ordre était inversé.
- **Cause** : plusieurs endroits, tous cohérents entre eux et tous
  bloquants — `graph_index.py` (BRIEF ready sans TRC/INT/DOM, source
  unique, régime terrain sans humain), `spec-compiler` Passe 0,
  `domain-expert` § anti-complaisance, `CLAUDE.md` § régime de preuve.
  Aucun défaut : `read_regime()` renvoyait `None` et le hook alertait.
- **Correction** : `exploration` devient le régime par défaut, renvoyé
  par `read_regime()` quand ADR-002 est absent ou illisible. Sous ce
  régime, tous les contrôles de preuve sont sautés et le hook n'affiche
  que des lignes factuelles. `traces` et `terrain` sont conservés intacts
  dans le code, mais ne s'activent que sur déclaration explicite ;
  leur mode d'emploi est isolé dans `.claude/optional/RIGUEUR.md`,
  fichier chargé par personne.
- **Reste ouvert** : rien ne rappelle qu'il faudra activer la rigueur le
  jour où de l'argent réel entre en jeu. Un rappel sans conséquence
  serait du papier peint — je n'en ai pas ajouté. Il faudrait un
  déclencheur mécanique, et je ne vois pas lequel serait fiable.

---

## 2026-08-30 — src/ n'a jamais été créé

- **Symptôme** : à la fin d'une session complète d'ouverture de projet,
  aucun fichier de code. Le graphe était riche, le produit inexistant.
- **Cause** : `software-architect` § garde-fou d'entrée exigeait un BRIEF
  `ready` ; `spec-compiler` produisait un `ready` seulement si sa Passe 0
  passait ; la Passe 0 exigeait une preuve. Chaîne de trois prérequis
  dont le dernier était inatteignable. Chaque maillon était défendable
  isolément.
- **Correction** : `software-architect` accepte désormais n'importe quoi
  qui vaut périmètre + intention — un ADR, une liste de features, une
  IDEA, ou une phrase de l'utilisateur dans le tour courant. Interdiction
  explicite d'exiger un BRIEF, une SPEC ou une preuve. Il enchaîne sur
  `feature-build` dans le même tour : un squelette sans écran n'est pas
  un livrable.
- **Reste ouvert** : rien.

---

## 2026-08-30 — Un déploiement UE en TASK 2

- **Symptôme** : le juridique et la conformité sont sortis en deuxième
  tâche du projet, ont saturé la conversation, et rien n'a avancé.
- **Cause** : aucune notion d'ordre d'exécution nulle part. `product-owner`
  arbitrait sur la valeur et la preuve, jamais sur le moment.
- **Correction** : champ `phase: local | pilote | dur` obligatoire sur
  chaque TASK. Nouveau hook `PreToolUse` `.claude/hooks/phase_guard.py`
  qui **refuse l'écriture** d'une TASK `phase: dur` tant qu'une TASK
  `phase: local` est ouverte. Le message de refus donne les trois sorties
  légitimes : fermer les tâches locales, requalifier en `pilote`, ou
  déposer en IDEA. Le juridique produit des templates à trous dans
  `product/legal/` — hors graphe, sans ID, sans TASK, donc jamais refusé.
- **Reste ouvert** : le garde ne lit que le contenu écrit, pas
  l'intention. Rien n'empêche d'écrire du travail de phase `dur` sans
  TASK du tout. C'est assumé : le garde tient l'ordre déclaré, pas la
  discipline.

---

## 2026-08-30 — Sur-testing en phase local

- **Symptôme** : chaque micro-avancement testé de fond en comble, pour du
  code jetable qui n'avait encore rencontré aucun utilisateur.
- **Cause** : `CLAUDE.md` § répartition Superpowers déléguait tout l'aval
  au TDD complet, sans distinguer le moment. Une frontière unique — le
  BRIEF `ready` — pour deux régimes de risque très différents.
- **Correction** : règle de test par phase dans `CLAUDE.md` et dans
  `feature-build`. En `local` : uniquement les invariants métier et les
  erreurs qui coûtent de l'argent ou une commande. Le TDD complet de
  Superpowers démarre en `pilote`.
- **Reste ouvert** : « invariant métier » reste un jugement. Sur Paymex
  la liste est évidente (idempotence, double débit, transition d'état) ;
  sur un domaine plus mou, moins.

---

## 2026-08-30 — Aucune skill de design

- **Symptôme** : résultat visuellement incohérent, sans direction — du
  vibe coding.
- **Cause** : rien dans le socle ne traitait l'interface.
  `product/assets/ART-DIRECTION.md` existait mais vide, et ne portait que
  sur les images générées, pas sur les écrans.
- **Correction** : skill `design-direction` en deux modes — ÉTABLIR
  (recherche de 3 à 5 produits réels du domaine, extraction de la
  navigation, densité, typo, palette, états d'erreur et de chargement,
  puis écriture de `product/assets/DESIGN.md`) et UX/UI SENIOR (chaque
  écran confronté à DESIGN.md avant d'être écrit). Agent `design-critic`
  à contexte vierge pour la confrontation après coup — il n'a pas assisté
  aux compromis, donc il ne les excuse pas.
  **Contrainte mécanique** : `phase_guard.py` refuse tout fichier d'écran
  sous `src/` tant que `DESIGN.md` est absent. Un avertissement aurait été
  ignoré ; un refus ne l'est pas.
- **Reste ouvert** : le garde reconnaît un écran à son extension
  (`.tsx`, `.vue`, `.html`…). Une UI en Python ou en Rust passe au
  travers. À étendre quand le cas se présentera, pas avant.

---

## 2026-08-30 — Le mode non structuré donnait de meilleurs résultats

- **Symptôme** : ouvrir Claude Code et donner ses features une à une
  produisait plus que le processus complet du socle. Le processus était
  net négatif.
- **Cause** : structurelle, pas locale. Toute entrée dans le système
  passait par une capture (`idea-grill`) qui interdit explicitement
  d'implémenter dans le tour courant, puis par un grill, puis par une
  SPEC, puis par un BRIEF. Le chemin court existait mais était présenté
  comme une exception à justifier, avec un garde-fou à 60 % qui le
  décourageait.
- **Correction** : skill `feature-build`, déclarée dans `CLAUDE.md` comme
  **le chemin par défaut**. Elle construit d'abord et écrit la TASK
  `done` après, dans le même tour. Le circuit long est requalifié : il ne
  sert que ce qui est cher à défaire (contrat de données, argent réel,
  authentification, contradiction d'ADR). Le hook ne signale plus une
  TASK sans parent comme une anomalie quand elle vient de `feature-build`.
- **Reste ouvert** : `feature-build` et `idea-grill` se déclenchent sur
  des formulations proches (« et si on ajoutait X » vs « ajoute X »). La
  bascule repose sur une lecture d'intention, pas sur un mécanisme. Si
  ça dérape en session réelle, il faudra trancher autrement.

---

## 2026-08-30 — Le hook signalait ce que CLAUDE.md autorise

- **Symptôme** : premier vrai projet construit avec le socle corrigé.
  Trois TASK écrites par `feature-build`, trois lignes
  `TASK-nnn orphelin — aucun parent SPEC/BRIEF` dans `! Incohérences`,
  plus deux lignes sur `product/legal/`. Cinq incohérences, cinq fausses.
  Un avertissement faux vingt fois devient du papier peint — c'est
  exactement ce qu'on cherchait à éviter.
- **Cause** : deux règles écrites en prose sans contrepartie mécanique.
  `CLAUDE.md` disait « une TASK issue de feature-build n'a pas besoin de
  parent » et « `product/legal/` est hors graphe », mais
  `graph_index.py` ne connaissait ni l'un ni l'autre : `IGNORE_DIRS` ne
  contenait que `grill`, et la dispense de parent ne testait que
  `chemin: court`.
- **Correction** : champ `origine: feature-build` obligatoire sur les TASK
  écrites après le code — c'est le champ que le hook lit pour dispenser.
  `legal` ajouté à `IGNORE_DIRS`. Le hook compte à part les TASK
  dispensées et affiche une ligne factuelle
  (« Dont N TASK écrite(s) après le code ») : la dette reste visible sans
  être reprochée. `feature-build` écrit désormais le champ, et la skill
  explique pourquoi il n'est pas décoratif.
- **Reste ouvert** : rien. La règle et le hook disent la même chose.

---

## 2026-08-30 — design-direction demandait ce que le web ne donne pas

- **Symptôme** : mode ÉTABLIR de `design-direction`, sur Paymex. La skill
  demande d'extraire de 3 à 5 produits réels leur « typographie, palette,
  densité ». Les recherches ont rendu des descriptions de fonctionnalités
  et des parts de marché — jamais une valeur de couleur ni un nom de
  police. Aucune capture d'écran n'est accessible par recherche.
- **Cause** : `.claude/skills/design-direction/SKILL.md`, MODE ÉTABLIR,
  étape 1. La liste de ce qu'il faut relever mélange ce qu'une recherche
  textuelle produit vraiment (structure de navigation, ce que le produit
  met en avant, contraintes documentées, codes USSD) et ce qu'elle ne
  produit jamais (valeurs de couleur, familles typographiques, densité
  mesurée).
- **Correction** : l'étape 1 distingue maintenant les deux, et dit à quoi
  sert chacune. Ce qui est sourçable devient `DOM` et pilote le parti ;
  la palette et la typographie sont assumées comme des **choix**, marqués
  comme tels dans `DESIGN.md`. La skill demande une capture d'écran à
  l'utilisateur quand il en a une, sans en faire une condition.
- **Reste ouvert** : rien de bloquant. Le parti tiré des contraintes de
  terrain (soleil, écran 360 px, réseau instable) s'est révélé plus utile
  que n'importe quelle palette copiée.

---

## 2026-08-30 — Le nouveau projet héritait du README du socle

- **Symptôme** : `./sfdev-new.sh` copiait tout, README compris. Le
  nouveau projet s'ouvrait sur un fichier qui explique le socle, pas le
  produit. Personne ne le remarque tant qu'on ne le montre à personne.
- **Cause** : `sfdev-new.sh`, la copie `rsync` n'excluait que `.git`,
  `.obsidian`, `AMELIORATIONS.md` et `product/INDEX.md`.
- **Correction** : le README du socle part dans `docs/LE-SOCLE.md` du
  nouveau projet, et un `README.md` minimal est écrit à sa place avec le
  nom du projet et sa phrase d'intention. Il dit explicitement qu'il est
  à réécrire quand quelque chose tournera.
- **Reste ouvert** : rien.
