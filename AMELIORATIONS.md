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
