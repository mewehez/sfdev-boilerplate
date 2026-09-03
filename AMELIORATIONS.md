# Journal des frictions

Une entrée par friction réellement rencontrée. Rien de spéculatif.

---

## 2026-09-03 — La page produit disait tout, donc n'était pas lue

- **Symptôme** : l'utilisateur relève que la page qui présente le produit
  « étouffe le visiteur ». Mesuré : **1 509 mots, 12 sections**, environ
  huit écrans à défiler. Une page comparable, prise en exemple, tenait
  chaque idée en un titre et une phrase.
- **Cause** : aucune skill ne couvrait cet artefact. `copywriting` traite
  les textes vus par l'utilisateur **d'un produit** — messages d'erreur,
  libellés, courriels — c'est-à-dire quelqu'un qui s'en sert déjà. La
  page qui s'adresse à quelqu'un **qui ne connaît pas** le produit
  obéit à des contraintes opposées : là où l'un veut de la précision,
  l'autre n'a pas le temps de la lire. Faute de règle, la page a été
  écrite comme le reste du projet : en expliquant les raisons, en citant
  la recherche, en listant tout ce qui existe.
- **Cause seconde** : le socle valorise, à juste titre, d'écrire pourquoi
  une décision a été prise. Cette qualité se retourne sur une page
  produit — le raisonnement intéresse l'équipe, pas le visiteur.
- **Correction** : une skill `page-produit`, tenue par une seule règle —
  **une idée = un titre + une phrase** — et par une mesure avant de rendre
  la main : mots, écrans à défiler, et ce qui tient au-dessus du pli. Les
  citations de recherche et les explications de choix y sont **interdites**,
  nommément, parce que c'est exactement ce que le reste du socle
  encourage. Elle porte aussi le refus de dessiner soi-même un visuel qui
  demande un métier.
- **Ce qui vaut d'être retenu** : une règle juste pour un artefact peut
  être fausse pour un autre. Le socle n'avait pas de mot pour « ce texte
  s'adresse à quelqu'un qui ne connaît rien et n'a pas le temps » — et
  sans ce mot, il a appliqué la règle du dessus.
- **Reste ouvert** : `copywriting` et `page-produit` se contredisent sur
  la citation d'utilisateur. La frontière est claire — dans le produit
  contre autour du produit — mais elle n'est écrite que d'un côté.

---

## 2026-08-31 — Le grill coupait dans un produit déjà construit

- **Symptôme** : un projet démarre en reprenant une exploration
  antérieure, déjà substantielle. À la question « qu'est-ce que
  l'application sait faire ? », l'utilisateur répond « tout », puis
  valide une liste de neuf features **écrite par l'agent de mémoire**.
  La question de cadrage suivante en sort quatre. Deux tours plus tard,
  le produit construit a deux écrans là où l'existant en avait onze — et
  l'écart n'apparaît qu'à la relecture du code, une fois la feature
  livrée.
- **Cause** : `project-grill` suppose qu'aucun code n'existe. Sur cette
  hypothèse, deux de ses mécanismes se retournent. **La liste des
  features vient de la mémoire de l'utilisateur** — plus courte que son
  produit, et le manque est invisible. Et **les exclusions coupent dans
  du périmètre** : la question « ce qui n'existera PAS en v1 » est saine
  quand rien n'est écrit, elle détruit du travail fait quand quelque
  chose l'est. Les personas, convoqués pour arbitrer, ont argumenté
  contre des features déjà codées — ils faisaient leur travail, on leur
  avait posé la mauvaise question.
- **Correction** : une ÉTAPE 0 bis, déclenchée dès qu'un existant est
  repris. L'inventaire se **dérive de la source** — routes, écrans,
  gestes, schéma, référentiels codés en dur — jamais de tête. Il fixe le
  périmètre, et **le grill ne travaille plus que l'UX** : les exclusions
  deviennent une question d'ordre, pas de contenu, et les personas sont
  convoqués écran par écran pour dire ce qui manque et ce qui bloque, non
  ce qu'on garde. Retirer une feature inventoriée redevient possible,
  mais par `idea-grill`, qui la juge au vu de ce qu'elle coûte à défaire.
- **Ce qui vaut d'être retenu** : c'est la troisième fois que le même
  défaut se paie — après `parite` et `DISPENSE_PARENT`. **Un inventaire
  pris de mémoire est toujours plus court que la source**, et rien dans
  la session ne signale l'écart. Partout où le socle doit énumérer un
  existant, il doit le dériver, jamais le demander.
- **Reste ouvert** : la détection de l'ÉTAPE 0 bis repose sur l'utilisateur
  qui mentionne un existant. Rien ne la déclenche si le code est là et que
  personne n'en parle.

---

## 2026-08-31 — Un ADR ne pouvait pas citer ce qu'il avait écarté

- **Symptôme** : une idée est tranchée puis archivée `killed`, et l'ADR qui
  consigne la décision la cite comme alternative écartée. Le hook signale
  aussitôt « ADR-nnn dépend de IDEA-nnn, archivé — décision fondée sur du
  mort ».
- **Cause** : `graph_index.py` applique la règle du lien-vers-archivé à
  **tous** les types d'objets. Elle est juste pour une SPEC, un BRIEF ou une
  TASK — bâtir dessus, c'est bâtir sur du mort. Elle est fausse pour un ADR,
  et pour lui seul : le socle le définit comme « décision **+ alternatives
  écartées** ». Citer l'idée tuée n'est pas en dépendre, c'est la
  documenter. Le contournement n'existait pas non plus : le corps est lu au
  même titre que le frontmatter, donc retirer le lien du frontmatter ne
  suffisait pas. **Il n'y avait aucune façon d'écrire un ADR conforme à sa
  propre définition sans déclencher l'alerte.**
- **Correction** : la règle saute les nœuds `ADR-`. Trois lignes, un seul
  endroit. Le hook ne bloquant rien, le changement ne peut que retirer des
  alertes fausses — jamais en ajouter, jamais empêcher une écriture.
- **Ce qui vaut d'être retenu** : c'est la deuxième fois que le même défaut
  se paie — après `DISPENSE_PARENT`. Une règle de graphe vraie pour la
  majorité des types est appliquée à tous, et le type dont le métier est
  précisément l'exception se fait signaler à chaque session. Une règle de
  graphe se pose **par type**, ou elle criera à tort quelque part.
- **Reste ouvert** : les autres règles de lien ont-elles la même faiblesse ?
  Aucune revue systématique n'a été faite, type par type.

---

## 2026-08-31 — Les personas étaient convoqués, jamais écrits

- **Symptôme** : à l'ouverture d'un projet, l'utilisateur laisse la main
  sur une question produit et demande qu'on travaille avec les personas.
  Il n'y en a aucun. `.claude/agents/` ne contient que le gabarit.
- **Cause** : le maillon manque au milieu d'une chaîne branchée des deux
  côtés. `persona-TEMPLATE.md` porte en commentaire « CHAMPS À REMPLIR
  PAR project-grill » — et `project-grill/SKILL.md` ne prononçait pas le
  mot une seule fois. En aval, trois consommateurs supposaient le fichier
  présent : `idea-grill` dispatche `<role>-persona` en sous-agent,
  `copywriting` lit « ce qu'il ne fera pas », `visual-prompt` demande la
  cohérence avec lui. Chacun échouait en silence, sur un fichier que
  personne n'avait la charge de créer.
- **Cause seconde** : la déclaration d'ouverture obligatoire du gabarit
  couvrait `auto-usage`, `traces` et `terrain` — pas `exploration`, qui
  est le régime **par défaut**. Le seul régime où le persona est une pure
  invention était le seul à n'avoir aucune phrase pour le dire. Un
  persona muet sur sa provenance finit cité comme une source.
- **Correction** : `project-grill` gagne une ÉTAPE 1 bis — les rôles
  nommés par la vision sont incarnés tout de suite, trois au maximum,
  déduits de l'ÉTAPE 1 et non demandés champ par champ à un utilisateur
  qui n'a pas ces réponses. Le gabarit gagne sa ligne `exploration` :
  « Persona inventé — zéro observation. » L'ÉTAPE 4 les compte parmi ce
  qu'elle écrit.
- **Ce qui vaut d'être retenu** : le socle a une seconde couture, jumelle
  de celle des hooks — celle entre ce qu'une skill **consomme** et ce
  qu'une autre a la charge de **produire**. Un consommateur qui suppose
  un fichier sans que personne ne soit nommé pour l'écrire ne casse rien
  bruyamment : il dégrade. Ajouter un consommateur sans désigner le
  producteur, c'est ajouter une dépendance à un fichier fantôme.
- **Reste ouvert** : trois personas au maximum est une limite posée au
  jugé, pour éviter le chœur. À vérifier sur un produit qui a réellement
  quatre rôles distincts.

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
  erreurs qui ne se rattrapent pas. Le TDD complet de
  Superpowers démarre en `pilote`.
- **Reste ouvert** : « invariant métier » reste un jugement. Sur le
  produit en cours, la liste était évidente — idempotence, geste joué
  deux fois, transition d'état interdite ; sur un domaine plus mou,
  moins.

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

- **Symptôme** : mode ÉTABLIR de `design-direction`, sur le produit en cours. La skill
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

---

## 2026-08-30 — Un blocage oublié dans la passe D2 : copywriting

- **Symptôme** : demande d'une page de vitrine pour le produit. La skill
  `copywriting` porte, en tête de fichier :
  « Refuser dans tous les cas s'il n'existe aucune SPEC ». Le produit avait zéro
  SPEC — le circuit long n'a jamais été emprunté, `feature-build` a
  construit directement. La skill aurait refusé d'écrire la page d'un
  produit qui tourne déjà.
- **Cause** : `.claude/skills/copywriting/SKILL.md`, § garde-fou
  d'entrée. La passe D2 a traité `spec-compiler`, `software-architect`,
  `domain-expert`, `idea-grill` et le hook, mais pas `copywriting` —
  son blocage ne portait pas sur la *preuve* mais sur l'existence d'un
  objet du graphe, et il est passé au travers de la relecture.
- **Correction** : le garde-fou devient « aucun refus ». La règle qui
  reste — ne rien promettre qui n'existe pas — se vérifie désormais
  contre `src/`, les TASK `done` et les ADR, pas contre une SPEC.
  Ce que le produit ne sait pas faire devient une section
  « où en est le produit » dans la page, pas un refus d'écrire.
- **Reste ouvert** : j'ai trouvé celui-là parce qu'il m'a gêné en
  construisant. Rien ne garantit qu'il n'en reste pas d'autres dans les
  skills que cette session n'a pas exercées — `visual-prompt` et
  `graph-index` n'ont jamais tourné. Une relecture ne les trouve pas ;
  seul l'usage les trouve.

---

## 2026-08-30 — copywriting et feature-build se contredisaient

- **Symptôme** : `copywriting` impose « produire 2 angles, laisser
  l'utilisateur choisir, ne pas recommander ». `feature-build` interdit
  « poser plus d'une question avant d'écrire du code ». Écrire la landing
  demandait de violer l'une des deux. Arbitré à la main.
- **Cause** : les deux skills ont été écrites pour des moments
  différents sans que la frontière soit dite. Le choix entre deux angles
  est un arbitrage de positionnement — il a du sens quand on s'adresse à
  de vraies personnes, pas quand on monte la première version d'une page.
- **Correction** : la règle des deux angles devient dépendante de la
  phase. En `local`, un angle est monté et l'autre reste dans le COPY,
  marqué `<!-- écarté -->` avec sa raison ; une ligne dit lequel a été
  monté et que l'autre se remonte en un tour. En `pilote`, les deux
  angles sont présentés et l'utilisateur choisit.
- **Reste ouvert** : c'est la deuxième fois qu'une contradiction entre
  deux skills se résout par le champ `phase`. Si un troisième cas
  apparaît, la phase mérite d'être un en-tête explicite dans chaque
  SKILL.md plutôt qu'une mention dispersée dans le corps.

---

## 2026-08-30 — Le socle traitait un changement de périmètre comme un affront

- **Symptôme** : demande d'ajouter deux rôles d'utilisateur d'un coup.
  ADR-001 les excluait explicitement de la v1. `product-owner` porte :
  « Hors périmètre ADR-001 → rejeté, sans discussion. Citer l'ADR. Si
  l'utilisateur insiste : → modifie ADR-001 d'abord. » En suivant la
  règle, j'aurais refusé une demande directe, une fois, de la personne
  qui décide du périmètre — et je lui aurais demandé d'aller éditer un
  fichier avant de revenir. Exactement le détour que le socle est censé
  supprimer.
- **Cause** : deux règles écrites pour un autre régime.
  1. `.claude/agents/product-owner.md`, règle 1 : le vocabulaire
     (« rejeté », « insiste ») suppose un product owner qui protège un
     périmètre contre un demandeur. En `exploration`, ce sont la même
     personne.
  2. `.claude/skills/feature-build/SKILL.md`, § « quand NE PAS
     l'utiliser » : le critère « touche l'authentification ou des
     données personnelles **en production** » a un qualificatif qui
     sauve, mais assez flou pour faire hésiter. Le vrai critère n'est
     pas le sujet, c'est la réversibilité dans la phase courante.
- **Correction** :
  - `product-owner` : une demande qui contredit un ADR déclenche une
    procédure en quatre gestes dans le même tour — dire lequel est
    contredit en une ligne, écrire un ADR nouveau qui lève ce point,
    laisser l'ancien intact, construire. Le seul refus qui subsiste :
    contredire un ADR écrit dans la session courante, où l'on demande
    lequel des deux vaut.
  - `feature-build` : le circuit long est déclenché par trois
    conditions vérifiables — quelqu'un d'autre dépend déjà de ce qu'on
    change, l'annuler coûte plus qu'un `git revert`, ou la phase est
    `pilote` et plus. Et une ligne explicite : contredire un ADR n'est
    pas un motif de circuit long, c'est un motif d'écrire un ADR.
- **Reste ouvert** : rien. ADR-004 a été écrit sans interrompre le
  travail, et il porte ce que la décision coûte — données personnelles
  qui entrent dans le produit, persistance devenue obligatoire.

---

## 2026-08-30 — Une feature a rendu fausse une phrase affichée ailleurs

- **Symptôme** : ajout d'un code d'accès à l'application. L'écran Profil
  s'est retrouvé avec, à quelques centimètres d'écart : une section qui
  propose de choisir un code, et une phrase écrite trois features plus
  tôt qui affirme « **Aucun PIN**, aucun mot de passe ». La contradiction
  était sur le même écran, et je ne l'ai vue qu'en regardant une capture.
- **Cause** : rien dans le socle ne traite une **promesse affichée**
  comme un objet durable. `DESIGN.md` a une section « Ce qu'on ne fait
  jamais » — des interdits pour celui qui écrit — mais aucune section
  pour ce que le produit **affirme à l'utilisateur**. Or une affirmation
  engage tous les écrans, y compris ceux qui n'existent pas encore.
  `design-critic` confronte l'écran qu'on vient d'écrire à `DESIGN.md` ;
  il ne pouvait pas voir qu'un autre écran venait de devenir faux.
- **Correction** :
  - `design-direction` : `DESIGN.md` gagne une section **« Promesses
    faites à l'utilisateur »**, et le mode UX/UI SENIOR commence par
    « quelle promesse cet écran met-il en jeu ? ».
  - `design-critic` : la promesse contredite devient sa **première**
    lentille, avant les valeurs en dur — c'est le seul défaut qui ne se
    voit pas sur l'écran examiné.
  - Dans le produit, la règle est en plus tenue par un test qui parcourt
    tous les gabarits : aucun n'a le droit de dire « aucun PIN », ni
    d'employer un même mot pour désigner à la fois le secret d'un tiers
    et celui de l'application.
- **Reste ouvert** : ce test est spécifique au vocabulaire du produit.
  Le socle ne peut pas le généraliser — il ne connaît pas les promesses
  d'un produit qu'il ne verra jamais. La section de `DESIGN.md` et la
  lentille du critique sont ce qu'on peut faire de mécanique ; le reste
  demande de relire la liste, et ça se dégrade.

---

## 2026-08-30 — Quatre défauts d'ergonomie qu'aucune règle ne couvrait

- **Symptôme** : l'utilisateur a buté sur un bouton grisé et a mis un
  moment à comprendre qu'il manquait un choix obligatoire ; il a relevé
  un bandeau de marque répété sur tous les écrans, une page de profil
  devenue interminable, et des champs de date deux fois plus grands que
  les autres avec le calendrier natif du navigateur.
- **Cause** : `design-direction` impose les cinq états d'un écran —
  vide, chargement, erreur récupérable, erreur définitive, succès —
  mais aucun ne couvre le **refus d'un formulaire incomplet**. Un
  bouton `disabled` passait donc pour un design correct. Rien non plus
  n'interdisait la marque répétée, la page-liste, ni le mélange d'un
  contrôle natif avec des contrôles maison.
- **Correction** :
  - `design-direction` gagne une question avant écriture — « que se
    passe-t-il quand ce formulaire est incomplet ? » — et quatre
    interdits : désactiver un bouton sans afficher pourquoi, répéter la
    marque sur un écran d'usage, laisser une page de réglages dépasser
    deux écrans, mélanger un contrôle natif avec des contrôles maison.
  - Dans le produit, `DESIGN.md` gagne les composants correspondants
    (`entete`, `identite`, `avatar`, `lien-ligne`, `calendrier`) et un
    calendrier maison qui reprend la grille de jours déjà employée pour
    le virement planifié.
- **Reste ouvert** : ces quatre défauts se voient en trois secondes sur
  un écran, et aucun test ne les aurait trouvés. Le socle a un critique
  à contexte vierge (`design-critic`) qui pourrait les voir — mais il
  lit du code, pas une capture. Tant qu'il ne regarde pas l'écran rendu,
  il restera aveugle à ce qu'un humain repère instantanément.

---

## 2026-08-30 — Deux collisions de noms CSS, la même cause

- **Symptôme** : deux fois dans la même session, une classe nouvelle a
  repris un nom déjà employé. `.hero` — carte de montant des écrans
  d'usage — réutilisé pour l'accroche de la vitrine, ce qui aurait
  appliqué un fond accentué à l'en-tête. Puis `.point` — les cartes
  « ce qui est difficile » de la vitrine — réutilisé pour le badge d'un
  bouton de filtre, qui a gonflé de 8 px à 34 et débordé de l'écran.
  Aucun des deux ne se voit dans le gabarit. Le premier a été attrapé en
  relisant, le second seulement sur une capture.
- **Cause** : `DESIGN.md` a une table des composants, mais rien ne dit
  qu'elle est **aussi le registre des noms pris**. Ni la skill ni le
  critique ne demandaient de la relire avant de nommer.
- **Correction** :
  - `design-direction` : la table est déclarée registre des noms, et le
    mode UX/UI SENIOR ajoute une question avant écriture — « quels noms
    est-ce que j'introduis, et sont-ils libres ? ».
  - `design-critic` : « nom de composant déjà pris » devient sa deuxième
    lentille, juste après la promesse contredite. C'est le défaut le
    moins cher à trouver en lisant, et le plus cher à trouver autrement.
- **Reste ouvert** : un contrôle mécanique serait possible — comparer
  les classes d'un gabarit aux sélecteurs déjà définis ailleurs — mais
  il faudrait analyser la feuille de style, et le socle ne sait pas dans
  quel langage le projet écrit son CSS. La lentille du critique est ce
  qu'on peut faire sans supposer une stack.

---

## 2026-08-30 — Un port qui compile n'est pas un port qui marche

- **Symptôme** : un portage Flutter passait `flutter analyze`
  sans un seul avertissement, `flutter test` au vert contre le vrai
  serveur — et le premier écran affiché après connexion était l'écran
  rouge de Flutter : `_Map<String, dynamic> is not a subtype of String`.
  Le serveur envoie `avatar` comme objet `{libelle, cle, svg}` ; le code
  Dart faisait `compte['avatar'] as String`. L'analyseur ne pouvait rien
  voir : la réponse JSON est `dynamic`, et `as String` sur du `dynamic`
  est un contrat que le compilateur accepte et que l'exécution seule
  tranche.
- **Cause** : la skill `portage` demandait de compiler et de tester. Elle
  ne demandait pas de **lancer et regarder**. Or c'est exactement à la
  frontière du port — là où un langage lit le JSON d'un autre — que le
  typage statique ne protège plus. Les tests d'API ne l'ont pas vu non
  plus : ils vérifiaient les clés de la réponse, jamais le rendu qui les
  consomme.
- **Correction** : `portage` gagne une étape non négociable avant de
  déclarer un port fait — lancer l'application sur un appareil ou un
  simulateur, ouvrir **chaque** écran, et le voir. Le motif est nommé :
  tout `as <Type>` posé sur une valeur venue du réseau est une assertion
  non vérifiée, et il y en a un par champ lu.
- **Ce qui l'a attrapé** : une capture d'écran du simulateur. Le même
  outil que pour les deux collisions CSS. Trois défauts sur trois
  trouvés en regardant, aucun en relisant.

---

## 2026-08-30 — Une liste à trois lignes ne montre pas le défaut

- **Symptôme** : l'utilisateur a dû signaler que les pages s'allongeaient
  sans fin. Chaque écran laissait ses listes grandir avec les
  données — 27 paiements, 40 achats, autant de tentatives qu'un client
  fait d'essais. Le total en bas, le bouton d'action, la barre
  d'onglets : tout partait hors de portée. Et l'en-tête, avec son retour,
  disparaissait dès le premier geste de défilement.
- **Cause** : les écrans ont été construits, relus et critiqués avec des
  données de démonstration — trois ou cinq lignes. À trois lignes, une
  liste sans plafond est indiscernable d'une liste plafonnée. Ni la
  skill ni le critique ne demandaient « et avec quarante ? ». Le défaut
  n'est pas dans le gabarit : il est dans le **volume**.
- **Correction** :
  - `design-critic` : « liste sans plafond » devient sa troisième
    lentille, juste après la collision de noms. Elle vise ce que le
    gabarit ne montre pas — une boucle dont la longueur vient des
    données — et vérifie les deux corollaires : le cadre défilant doit
    être atteignable au clavier, et son défilement doit se chaîner à la
    page, sinon la liste est un cul-de-sac.
  - Côté projet, la règle est passée dans `DESIGN.md` et surtout dans un
    **test** : toute liste bâtie par une boucle porte la classe, ou son
    exemption est écrite avec sa raison. Le test a immédiatement trouvé
    deux listes que je n'avais pas vues.
- **Ce qui vaut d'être retenu** : une exemption écrite dans un test vaut
  mieux qu'une règle en prose. La prose se relit ; le test se heurte.

---

## 2026-08-30 — Le mécanisme du web était un piège une fois porté

- **Symptôme** : les listes plafonnées du web, portées telles quelles
  en Flutter, ont produit l'inverse de ce qu'elles corrigeaient. Sur
  un écran de liste, le cadre dépassait par le bas de
  l'écran — et le doigt posé dessus faisait défiler **la liste**, pas la
  page. Une partie du cadre restait donc inatteignable.
- **Cause** : le navigateur **chaîne** le défilement — arrivé au bord
  d'une liste imbriquée, il passe la main à la page. Flutter ne le fait
  pas. Le mécanisme du web reposait sur un service rendu gratuitement par
  la plateforme, et que personne n'avait nommé. La skill demandait de ne
  pas dupliquer les *règles* ; elle ne disait rien des *mécanismes*.
- **Correction** : `portage` gagne une étape avant d'écrire — « qu'est-ce
  que le navigateur faisait gratuitement, ici ? » — et un interdit :
  recopier un mécanisme parce qu'il marche sur le web. On porte ce qu'il
  cherchait à obtenir. Dans le cas présent, l'intention « la page ne
  s'allonge pas sans fin » se réalise par une structure différente : un
  écran, un seul défilement, et ce qui déborde part sur son propre écran.
- **Ce qui l'a attrapé** : encore une capture. La quatrième de suite.
  Aucun de ces quatre défauts n'était visible dans le code.

---

## 2026-08-31 — Le web avait un chemin, le port en avait deux

- **Symptôme** : l'utilisateur s'est déconnecté de l'application portée
  et n'a pas eu « content de vous revoir » — il est retombé sur le choix
  du rôle, comme si l'appareil n'avait jamais vu personne. J'avais
  pourtant vérifié ce parcours en capture, la veille, et il marchait.
- **Cause** : il marchait **par le chemin que je venais d'écrire**. Sur
  le web, une session s'ouvre dans une seule fonction, qui pose le
  cookie de session et celui de l'appareil d'un même geste — un endroit,
  rien à oublier. Le port a deux chemins : saisir le code, ou voir son
  jeton restauré au démarrage. Je n'avais couvert que le premier. Le cas
  découvert est exactement celui de quelqu'un qui était **déjà
  connecté** quand la nouvelle version est arrivée — donc invisible tant
  qu'on teste avec une installation neuve.
- **Correction** : `portage` gagne une étape — pour chaque état que le
  port conserve, « par combien de chemins peut-on l'atteindre, et
  est-ce qu'ils l'écrivent tous ? » — et un interdit correspondant.
- **Ce qui vaut d'être retenu** : ouvrir chaque écran ne suffit pas si
  on les ouvre toujours dans le même ordre, depuis une installation
  neuve. Le défaut vivait dans la **deuxième** session, pas dans la
  première. C'est le premier des cinq derniers défauts qu'une capture
  n'aurait pas attrapé.

---

## 2026-08-31 — Trois pièges de plus, et une liste pour les retenir

- **Symptôme** : l'utilisateur a trouvé, en une session, que la page
  principal du port n'avait ni QR ni partage, qu'aucune ligne de
  paiement n'y ramenait, et qu'une feuille de détail s'ouvrait vide.
  Chacun a une cause différente, et aucune ne se voyait dans le code.
- **Causes**, dans l'ordre où elles se sont révélées :
  1. La feuille plantait sur `demande_a` — un horodatage, pas une chaîne
     — et le moteur peignait son écran d'erreur, muet en release. C'est la
     **troisième** fois qu'un `as` sur du JSON fait tomber un écran.
  2. Le gabarit web formate ses dates dans un filtre serveur ; l'API
     rendait des nombres. Le port n'avait rien à afficher.
  3. Le QR se rendait en filets espacés : segno s'appuie sur le
     `stroke-width: 1` implicite de la norme SVG, qu'un navigateur
     applique et que le moteur du port applique autrement.
- **Correction** : plutôt que trois rustines, la skill `portage` gagne une
  section nommée — **« ce que le navigateur faisait gratuitement »** —
  qui liste six services que la plateforme d'arrivée ne rend pas :
  typage, mise en forme, valeurs implicites d'un format, chaînage du
  défilement, unicité des chemins d'écriture, déclarations de
  permissions. Chacun avec le défaut observé et la règle qui l'évite. La
  section porte sa propre consigne d'entretien : *quand un nouveau piège
  se paie, on l'écrit ici*.
- **Ce qui vaut d'être retenu** : après le premier `as` cassé j'avais
  corrigé le champ ; après le deuxième aussi. Il a fallu le troisième
  pour traiter la **classe** de défaut — remplacer tous les casts par des
  lecteurs qui ne promettent rien. Une correction qui ne remonte pas à la
  classe se repaie, et une liste tenue vaut mieux que trois souvenirs.

---

## 2026-08-31 — Porter de mémoire, c'est ne porter que ce qu'on regarde

- **Symptôme** : l'utilisateur a listé, sur le seul écran de profil, trois
  fonctions absentes du port — choix du motif, apparence, suppression de
  compte — et a ajouté « et j'en passe ». Il avait raison : un inventaire
  mécanique du web a trouvé **42 routes, 23 écrans, 45 gestes**, dont
  cinq écrans entiers jamais portés, deux jeux de filtres, et les
  virements sautés de l'historique.
- **Cause** : un port se fait écran par écran, en regardant l'écran qu'on
  porte. **On ne voit pas ce qu'on ne regarde pas.** Le trou ne se
  manifeste ni à la compilation, ni en ouvrant les écrans portés — la
  skill `portage` demandait justement de les ouvrir un par un, ce que
  j'avais fait. Elle ne demandait nulle part de comparer le port à la
  **liste** de ce qu'il devait couvrir.
- **Correction** : nouvelle skill `parite`. Elle dérive la surface de la
  source par un script — jamais de mémoire, puisque c'est la mémoire qui
  a échoué —, écrit une table `product/assets/PARITE.md` à deux états
  seulement (« porté » ou « hors périmètre — raison »), et pose un test
  qui **échoue si un écran de la source n'a pas sa ligne**. `portage`
  gagne une étape « vérifier la parité », et CLAUDE.md la règle : un port
  n'est jamais fini tant que la table n'est pas verte.
- **Ce qui vaut d'être retenu** : « ouvrir chaque écran » et « n'oublier
  aucun écran » sont deux problèmes différents, et je traitais le second
  avec l'outil du premier. Vérifier ce qu'on a écrit ne dit rien de ce
  qu'on n'a pas écrit. Il faut partir de la **source**, pas du port.

---

## 2026-08-31 — Une skill qui écrit des TASK doit se déclarer au hook

- **Symptôme** : à la relecture de fin de session, `graph_index.py`
  signalait neuf incohérences. Huit étaient des « TASK orpheline — aucun
  parent SPEC/BRIEF », toutes écrites par les skills `portage` et
  `parite`.
- **Cause** : `DISPENSE_PARENT` ne contenait que `feature-build`. J'ai
  créé deux skills qui écrivent des TASK sans les y ajouter. Ces TASK
  n'ont pas de parent **par construction** — leur parent est le produit
  déjà spécifié qu'on porte — exactement comme celles de
  `feature-build`. Le hook les comptait donc comme des oublis, et un
  avertissement qui crie à tort finit par être ignoré, ce qui est
  précisément ce que le socle cherche à éviter.
- **Correction** : `DISPENSE_PARENT` accueille `portage` et `parite`, avec
  le commentaire qui dit pourquoi et qui prévient : **ajouter une skill
  qui écrit des TASK sans l'ajouter ici fait pleuvoir des « orphelin »
  qui n'en sont pas.** `PARITE.md` rejoint les fichiers hors graphe, à
  côté de `DESIGN.md` — c'est une référence, pas un nœud. CLAUDE.md dit
  les trois origines dispensées au lieu d'une.
- **Ce qui vaut d'être retenu** : le socle a une couture entre ce que les
  skills produisent et ce que les hooks attendent. Créer une skill qui
  écrit dans le graphe sans regarder cette couture produit du bruit — et
  le bruit use exactement le mécanisme qui devait alerter.

---

## 2026-08-31 — Le socle avait pris le vocabulaire de son premier projet

- **Symptôme** : l'utilisateur a relevé que le socle parlait d'argent
  alors qu'il doit être neutre. Le contrôle l'a confirmé et élargi : le
  produit d'origine était **nommé onze fois** dans le journal, et le
  domaine du paiement servait de **catégorie** dans trois règles
  centrales : la ligne non négociable sur la duplication, le seuil de
  test, et le critère du circuit long. Le socle est public : il léguait
  ce vocabulaire à tout projet qui le reprendrait.
- **Cause** : un socle s'écrit **pendant** un projet. Ses règles naissent
  de frictions réelles, et une friction réelle a un domaine. Le premier
  produit teint donc le socle sans que personne ne le décide — chaque
  entrée de ce journal a été écrite en regardant un écran précis.
- **Le test qui tranche** : l'argent **en exemple dans une liste** reste
  légitime — il rend la règle concrète. L'argent **comme catégorie** est
  une fuite : il fait croire que la règle ne vaut que là. La ligne non
  négociable vise donc désormais ce qui est **irréversible**, et cite
  plusieurs formes plutôt qu'une seule — une valeur qui bouge, un droit
  accordé, un envoi parti, un dossier détruit.
- **Correction** : les règles sont généralisées ; le journal garde ses
  défauts concrets mais ne nomme plus de produit. Et surtout
  `outils/neutralite.py`, lancé par `sfdev-new.sh` **au moment où le
  socle est donné à un nouveau projet** — c'est là que la fuite se
  paierait. Il ne devine pas les fuites à venir : il garantit qu'une
  fuite trouvée une fois ne revient pas. Il en a d'ailleurs trouvé une
  que j'avais manquée à la main — puis il a refusé cette entrée-ci, qui
  citait les formules fautives pour les montrer. J'ai paraphrasé plutôt
  que d'ouvrir une exception : une contrainte mécanique qui s'excuse ne
  contraint plus.
- **Ce qui vaut d'être retenu** : la neutralité d'un socle n'est pas un
  état, c'est un entretien. On ne peut pas l'obtenir en écrivant mieux —
  seulement en la vérifiant au moment où elle compte.

## 2026-09-03 — Deux serveurs sur le même produit, et c'est le mort qu'on regarde

- **Le défaut** : j'avais une pile conteneurisée sur un port et un serveur
  de développement sur un autre. J'ai arrêté le second à la fin d'un tour
  — proprement — et laissé le premier tourner. Il servait des images
  construites plusieurs tours plus tôt. L'utilisateur a donc ouvert
  l'adresse qui répondait, et jugé le produit sur une version morte : sans
  les correctifs du tour, sans les vrais plans, sans rien de ce qui venait
  d'être fait.
- **Cause** : le socle disait comment développer sur le web et ne disait
  rien sur **ce qui reste allumé**. Ouvrir un serveur est un geste
  d'agent ; le refermer n'était l'obligation de personne. Et un serveur ne
  vieillit pas visiblement : il répond `200` aussi bien mort que vivant.
- **Ce qui trompe** : deux adresses vivantes ressemblent à un confort —
  « celle-ci pour construire, celle-là pour montrer ». C'est l'inverse.
  Rien ne distingue les deux à l'écran, donc c'est l'habitude qui choisit,
  et l'habitude choisit celle qu'on a ouverte en premier.
- **Correction** : `### Un seul endroit où regarder`, dans la section du
  développement web. Libérer le port avant d'en ouvrir un autre ; refermer
  ce qu'on a ouvert, ou écrire ce qui reste ouvert, à quelle adresse et de
  quand ça date. La règle vaut explicitement pour une pile conteneurisée,
  parce que c'est celle qu'on oublie : elle survit à la fermeture du
  terminal.
- **Ce qui vaut d'être retenu** : le coût d'un serveur oublié ne se paie
  pas sur sa propre machine. Il se paie quand quelqu'un d'autre ouvre
  l'adresse qu'on lui a donnée. Un agent qui allume doit éteindre — ou
  dire ce qu'il laisse allumé.

## 2026-09-03 — Un jeu de règles qui ne sait que refuser produit des écrans morts

- **Le défaut** : un écran livré, conforme sur toute la ligne, et dont
  l'utilisateur a dit « ça ne donne plus envie d'être utilisé ». Six
  reproches précis, tous de la même forme : à chaque fois qu'une
  interaction n'était pas évidente, j'avais **ajouté une phrase** au lieu
  de redessiner. Un bouton introuvable → une phrase d'aide. Un contrôle
  ambigu → une phrase d'explication. Le champ qui naissait hors de
  l'écran → un défilement automatique pour aller le chercher.
- **Cause** : `DESIGN.md` avait une section « Ce qu'on ne fait JAMAIS » et
  **aucune** qui dise ce qu'on fait toujours. Toutes les règles étaient
  soustractives : ne pas surcharger, ne pas détourner, ne pas charger
  lourd. Aucune n'exigeait de franchise du geste ni d'envie. Un écran
  pouvait donc passer tous les contrôles **sans rien faire de mal** — et
  ne toucher personne. `design-critic` l'a validé pour la même raison :
  il cherchait des fautes, il n'en a trouvé aucune.
- **Ce qui trompe** : un jeu de règles négatives donne l'impression d'être
  exigeant. Il l'est — sur ce qu'il interdit. Il est totalement muet sur
  ce qu'il faudrait obtenir, et ce silence ne se voit pas : rien ne
  signale l'absence d'une exigence qui n'a jamais été écrite.
- **Le second défaut, dans la méthode** : la recherche de références
  s'arrêtait aux produits du même domaine. Or dans les métiers où le
  logiciel est acheté par quelqu'un qui ne s'en sert pas, les produits
  dominants sont complets et pénibles. S'aligner sur eux revient à
  **copier leurs défauts** en croyant faire son métier. La règle est
  venue de l'utilisateur, mot pour mot : si les produits les plus proches
  sont mauvais, il faut regarder les milieux connexes.
- **Correction** :
  - `geste-direct` — sept règles vérifiables par quelqu'un d'autre, dont
    celle qui commande les autres : **quand une interaction n'est pas
    évidente, on redessine la forme, on n'ajoute pas une phrase.** Une
    phrase nécessaire s'inscrit dans la TASK comme un défaut, pas comme
    une solution.
  - `references-croisees` — au moins deux références hors du domaine,
    choisies sur le **problème de forme** et non sur le vocabulaire ; une
    colonne « ce qu'on lui refuse » sans laquelle une référence n'a pas
    été examinée mais admirée ; et une ligne pour les hypothèses des
    autres qui ne tiennent pas chez nous.
  - `design-direction` — la section « Ce qu'on fait TOUJOURS » devient
    obligatoire dans `DESIGN.md`, avec quatre exigences imposées par le
    socle.
  - `design-critic` — une seconde lentille, six questions dont « qu'est-ce
    qui, dans cet écran, donne envie de s'en servir ? ». La conformité ne
    suffit plus à conclure.
  - `directeur-artistique` — un agent dont le seul travail est de refuser
    le tiède, contraint par une règle : **un reproche sans référence n'est
    pas recevable.** Il doit citer un produit précis qui fait mieux. Sans
    cette contrainte il produit du goût ; avec elle, quelque chose qu'on
    peut aller vérifier.
- **Ce qui vaut d'être retenu** : un contrôle qui ne cherche que des
  fautes valide tout ce qui n'en contient pas. C'est vrai d'un agent
  comme d'un test. Pour qu'un socle produise autre chose que du correct,
  il faut qu'une règle au moins exige quelque chose de **positif** — et
  qu'un relecteur ait le droit de dire « rien ici ne donne envie » sans
  que ce soit une opinion hors sujet.

## 2026-09-03 — Le vérificateur de types ne voit pas la feuille de style

- **Le défaut** : `tsc --noEmit` au vert, le serveur de développement qui
  compile, et la construction de production qui échoue sur une accolade
  orpheline laissée par une suppression de règles. Le défaut n'est apparu
  qu'au moment de fabriquer l'image — après un cycle complet de
  construction, et sur une pile qui a continué de servir l'ancienne
  version pendant ce temps.
- **Cause** : la boucle de vérification s'arrêtait au typage. C'est le
  contrôle le plus rapide, donc celui qu'on prend pour le contrôle. Il ne
  regarde qu'un langage sur les trois.
- **Ce qui trompe** : le serveur de développement est tolérant par
  construction — il doit l'être, sinon on ne pourrait pas travailler sur
  du code à moitié écrit. Sa tolérance donne l'illusion d'une validation.
- **Correction** : la **construction de production** entre dans la boucle,
  et elle passe **avant** les relectures. Faire relire un écran qui ne se
  construit pas est du temps perdu deux fois.
- **Ce qui vaut d'être retenu** : un contrôle rapide n'est pas un contrôle
  complet, et l'écart entre les deux ne se voit pas — c'est le propre
  d'un angle mort.

## 2026-09-03 — Une règle de style morte ne se plaint jamais

- **Le défaut** : une règle écrite pour un sélecteur que le code ne
  produit pas. `[data-pointer="oui"]` sur une visionneuse qui, depuis
  qu'on lui a retiré un mode, pose `data-actif`. La règle était juste, le
  composant était juste, et **l'affordance du geste principal avait
  disparu en silence** — le curseur ne changeait plus, donc rien ne disait
  que l'objet se touche.
- **Cause** : rien ne relie une déclaration de style à son emploi réel. Ni
  le vérificateur de types, ni la construction, ni la relecture humaine —
  qui lit les deux fichiers séparément et ne voit pas ce qui manque entre.
- **Ce qui trompe** : c'est la **deuxième fois** à l'identique. La
  première, une bibliothèque avait renommé une classe ; la seconde, c'est
  nous en retirant un attribut. Une occurrence est un accident, deux sont
  un mécanisme absent — et un mécanisme absent se reproduira sur chaque
  écran suivant qui pilote du style par attribut.
- **Correction** : `outils/styles_morts.py`. Il lit les sélecteurs, lit
  les littéraux du code, et signale les règles qui ne s'appliquent à rien
  et les classes posées sans déclaration. Il ne comprend pas le CSS et
  n'essaie pas : c'est grossier, et suffisant. Premier passage sur un
  projet réel : **30 règles mortes**, dont des restes d'un écran resserré
  trois tours plus tôt et jamais nettoyé.
- **Ce qui vaut d'être retenu** : les défauts qui comptent ne sont pas
  ceux qui échouent. Une règle morte ne casse rien, ne ralentit rien, ne
  lève aucune alerte — elle retire une affordance et se tait. Ce genre de
  défaut ne se corrige pas en relisant mieux : il se corrige en fabriquant
  la chose qui se plaint.

## 2026-09-03 — Quand l'outil d'observation et le serveur se contredisent

- **Le défaut** : un écran s'affichait noir dans le navigateur de
  vérification, sans la moindre erreur. J'ai cherché la cause dans la
  feature du jour, puis dans la couche en dessous, puis j'ai annulé le
  travail entier pour isoler — le noir restait. Ce n'était pas le
  produit : c'était l'onglet de vérification, dégradé après des dizaines
  de navigations. Un onglet neuf a affiché la page immédiatement, avec le
  même code.
- **Cause** : je disposais de deux témoins qui se contredisaient — le
  serveur répondait `200` en 133 ms et servait la page complète, l'écran
  montrait du noir — et j'ai systématiquement cru l'écran. Parce qu'il est
  plus proche de l'utilisateur, donc il « compte plus ».
- **Ce qui trompe** : c'est vrai qu'il compte plus. Mais il compte plus
  **quand il est fiable**, et rien ne dit qu'il l'est. Un outil
  d'observation dégradé ne s'annonce pas : il montre quelque chose, et ce
  quelque chose a l'air d'un symptôme.
- **Correction, dans `design-direction` § Après** : quand la
  vérification visuelle contredit ce que le serveur affirme, **remplacer
  l'outil d'observation avant de chercher dans le code**. Onglet neuf,
  session neuve. Ça coûte une seconde ; l'inverse coûte des heures, et
  produit en plus un diagnostic faux.
- **Ce qui vaut d'être retenu** : un outil de mesure fait partie du
  système mesuré. On le soupçonne au même titre que le reste — et en
  premier quand il est le seul à se plaindre.
