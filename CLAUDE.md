# Règles projet

## Le contrat en une phrase
Une idée exprimée devient un produit qui tourne. La traçabilité suit,
elle ne précède jamais. Rien n'attend une preuve pour exister.

---

## Concision (s'applique à TOUS les agents et skills)
- Bullet points. Jamais de paragraphes.
- Aucun préambule, aucun récapitulatif de ce que tu viens de faire.
- Aucune reformulation de ma question.
- Marquage obligatoire :
  `→` action que je dois faire   `?` question   `!` risque/blocage
- Une seule question par tour. Attendre la réponse.
- Écran maximum. Si ça dépasse, écris dans un fichier et donne-moi
  le chemin + 3 bullets de synthèse.
- Jamais de validation gratuite ("bonne idée", "excellent point").

---

## Mode par défaut : `exploration`

C'est le mode unique, actif sans rien déclarer.

- **Aucun blocage, nulle part.** Ni sur une SPEC, ni sur un BRIEF, ni sur
  une TASK, ni sur le scaffolding. Aucun objet n'attend une preuve.
- Une hypothèse se trace (`SUG`), elle ne freine rien.
- Une recherche web et un raisonnement suffisent à écrire un `DOM`.
- Le hook affiche des lignes factuelles. Il ne produit aucune alerte de
  preuve, aucune injonction à interviewer.
- On construit par intuition, ou pour un portfolio. Un visuel sert
  justement à approcher les gens : il vient avant eux, pas après.

**Ce qui bloque quand même**, parce que ça relève de l'ordre et non de la
preuve — deux refus, deux seulement, tenus par `.claude/hooks/phase_guard.py` :
1. une TASK `phase: dur` tant qu'une TASK `phase: local` est ouverte ;
2. un écran sous `src/` tant que `product/assets/DESIGN.md` n'existe pas.

Un refus se lève en faisant la chose dans le bon ordre, jamais en
argumentant avec le hook.

### Activer la rigueur, plus tard
Une piste se confirme, quelqu'un d'autre commence à payer l'erreur :
écris `regime: traces` (ou `terrain`) dans le corps de
`product/decisions/ADR-002-regime-preuve.md` — mode d'emploi complet dans
`.claude/optional/RIGUEUR.md`.

---

## Phases d'exécution

Champ `phase:` obligatoire sur toute TASK. Trois valeurs, dans cet ordre :

| phase    | ce qu'elle contient |
|----------|---------------------|
| `local`  | ce qui fait tourner l'app sur la machine |
| `pilote` | ce qu'il faut pour la montrer à quelqu'un de réel |
| `dur`    | forme juridique, nom de domaine, hébergement, conformité, CGU, contrats opérateurs |

**Règle, tenue par le hook :** aucune TASK `dur` ouverte tant qu'une TASK
`local` reste ouverte.

Le juridique produit des **templates à trous** (`product/legal/`, hors
graphe, sans ID), jamais des blocages. Un template s'écrit quand on veut,
sans TASK — c'est une TASK `dur` qui est refusée, pas un fichier.

### Tests, par phase
- `local` : tester les **invariants métier** et les **erreurs qui coûtent
  cher** — une valeur qui bouge, un geste joué deux fois, une donnée
  perdue. Pas chaque fonction.
- `pilote` : le TDD complet de Superpowers démarre ici.
- `dur` : sans objet.

Écrire un test par fonction en phase `local` est une perte nette. Écrire
zéro test sur un invariant qui ne se rattrape pas est une faute.

---

## Les contrôles mécaniques

`outils/` porte les contrôles qui tiennent une règle à notre place. Ils
existent parce qu'une exemption écrite vaut mieux qu'une vigilance
espérée : ce qu'on a trouvé une fois ne doit pas revenir.

| contrôle | ce qu'il refuse |
|----------|-----------------|
| `neutralite.py` | le vocabulaire d'un projet passé, resté dans le socle |
| `styles_morts.py` | une règle CSS qui ne s'applique à rien, une classe jamais déclarée, **un nom du registre sans règle ni emploi** |
| `liens_morts.py` | un `[[lien]]` sans cible, un objet sans alias, un statut hors de sa liste fermée, un second coffre |
| `graphe_obsidian.py` | un frontmatter qu'Obsidian ne sait pas lire (et il le répare) |
| `dependances.py` | une faille connue dans ce qu'on installe |

**`outils/` est du socle : il se copie tel quel dans le projet suivant.**
Un outil qui ne vaut que pour CE produit — un dérivé d'image, un
importateur de format maison — va dans **`outils/produit/`**, qui ne se
copie pas. La frontière est dans l'arborescence, pas dans une intention :
c'est la seule forme qui survit à une relecture rapide.

### ! Un contrôle ne prouve que ce qu'il MESURE

Vert ne veut pas dire juste. Trois familles, et la troisième est celle
qu'aucune relecture n'attrape :

- **il mesure à côté** — un contrôle vérifiait qu'un alias *existait*, là
  où il fallait vérifier qu'il se *résolvait* ;
- **il mesure une chose absente** — des tests verts sur une
  fonctionnalité retirée de l'écran la veille. Un test vert sur une
  fonctionnalité absente est un **faux témoin** : il ne se signale pas,
  et il fait croire à une couverture qu'on n'a pas ;
- **il ne peut pas voir ce qu'il cherche.** Un contrôle qui compare A et
  B ne voit jamais ce qui n'est **ni dans A ni dans B**. Un nom qui vit
  dans un document prescriptif sans une seule règle et sans un seul
  emploi n'est ni une règle morte, ni une classe orpheline : il n'est
  nulle part, et le contrôle rend « cohérent ».

Deux conséquences, et elles sont contre-intuitives :

- **Retirer une fonctionnalité, c'est retirer ses tests dans le même
  geste.** Un test qu'on laisse derrière soi ne devient pas inutile, il
  devient menteur.
- **Quand l'observation contredit le contrôle, le contrôle est le
  suspect.** On remplace l'instrument avant de chercher la cause.

Et **avant de croire une mesure négative, lui montrer un cas positif.**
Une sonde qui n'a jamais rien vu bouger n'a rien prouvé — elle n'a même
pas prouvé qu'elle fonctionne. Corollaire pour les tests : un test qui
passe du premier coup sur un défaut qu'on vient de corriger doit être vu
**échouer** sur le code d'avant, sinon on ne sait pas ce qu'il tient.

### ! « Je n'ai pas regardé » n'est pas « je n'ai rien vu »

Un contrôle a trois issues, pas deux : **rien à signaler**, **j'ai
trouvé**, et **je n'ai pas pu regarder**. Les deux dernières se
ressemblent — un code de retour non nul — et les confondre coûte des
deux côtés :

- il **crie pour rien** là où ses outils manquent, et un contrôle qui
  crie pour rien cesse d'être lu ;
- ou, pire dans l'autre sens, un « rien à signaler » qui voulait dire
  « je n'ai rien ouvert » **rassure à tort**.

→ **Trois codes de retour, et le troisième se dit en toutes lettres.**

`!` **Et une leçon écrite dans un outil ne la lui fait pas tenir
partout.** Le cas trouvé : un audit de dépendances portait ce troisième
code dans sa propre documentation — pour « l'auditeur manque » — et
rendait quand même **vert** sur un dépôt où il n'y avait **aucun verrou à
ouvrir**. Même aveuglement, un étage au-dessus, sous le nez de la règle
qui l'interdit. En posant un garde, se demander de quoi d'autre « ne rien
voir » peut vouloir dire.

→ **Ce qui l'attrape, c'est le COMPTE.** Les autres contrôles tournent
eux aussi à vide sur un dépôt neuf — et ils s'en sortent parce qu'ils le
disent dans la même phrase : « 0 objets », « aucune feuille de style ».
Seul celui qui annonçait « rien à signaler » sans dire **combien il avait
regardé** était indistinguable d'un vrai vert. Un contrôle qui rend
« propre » rend aussi la taille de ce qu'il a ouvert.

→ Et **un contrôle se place là où vivent les données qu'il mesure.** Un
outil qui déduit son contexte de son propre emplacement ne survit pas au
déplacement : lancé ailleurs, il ne plante pas — il répond « rien en
attente », ce qui est plausible. Quand il dépend d'un service, il dit
**contre quoi** il a travaillé, sinon une réponse vide se lit comme une
bonne nouvelle.

### ! Un contrôle qui crie pour rien cesse d'être lu

Un faux positif coûte plus cher ici qu'ailleurs, parce qu'un contrôle est
fait pour être lu **rarement** : chaque ligne qu'il sort doit valoir une
lecture. Ce qu'un contrôle n'est pas censé regarder — du code entre
backticks, une valeur calculée à l'exécution, les dépendances installées
— ne se signale pas.

→ **La portée d'un contrôle fait partie de ce qu'il affirme.** Un contrôle
juste, appliqué au mauvais périmètre, produit des faux positifs qui ont
l'air de vrais — et on finit par corriger le code au lieu de corriger la
portée.


### ! Un contrôle qui applique une règle écrite ailleurs la LIT

Un contrôle a gagné la validation des statuts contre les listes fermées
de `CLAUDE.md` — et sa table a été **tapée de mémoire** plutôt que lue.
Cinq jours ont suffi pour que l'écart se voie, et il était double : une
liste au mauvais genre et amputée d'une valeur documentée, et **cinq
types sur onze absents**. Le contrôle rendait « cohérent » pour ceux
qu'il n'avait jamais ouverts.

Le coût n'est pas le faux négatif, il est pire : au premier objet portant
la valeur légitime que la table ignorait, on corrige **le document** au
lieu de l'outil. Un contrôle juste appliqué à la mauvaise règle produit
des faux positifs qui ont l'air de vrais.

> **Deux sources pour une même règle finissent par divorcer**, exactement
> comme deux sources pour un même nombre.

→ **Quand un contrôle applique une règle écrite ailleurs, il la lit.** Le
document prescrit, l'outil applique. La divergence n'est alors plus à
corriger — elle est devenue impossible, et corriger la règle suffit à
corriger le contrôle.

→ Et **ce qui ressemble à un littéral n'en est pas toujours un** : une
valeur comme « remplacé par <TYPE>-nnn » est un **motif**. La lire
littéralement rejette la seule forme que la règle autorise.

`!` Le troisième verdict vaut ici aussi, et c'est la deuxième fois de
suite qu'il manquait : quand la règle est introuvable, le contrôle le
**dit** et ne rend pas vert sur zéro liste vérifiée.

### La règle de travail

**Un outil corrigé rend une leçon, et la leçon revient ici.** Un correctif
qui reste dans le fichier de l'outil protège ce projet ; écrit dans le
socle, il protège les suivants. C'est la seule raison d'avoir un socle
plutôt qu'un dossier de scripts.

Concrètement, à chaque correction d'outil :

- le **cas** rejoint le contrôle, pour qu'il ne revienne pas ;
- la **leçon**, si elle se généralise, rejoint cette section ;
- le **fait** — ce qui a été trouvé, et ce que ça a coûté — rejoint la
  TASK en cours, jamais le seul message de fin de tour.

`!` Cette règle se suit **dans le produit** et s'oublie en montant : le
`CLAUDE.md` qu'on a sous la main pendant qu'on travaille est celui du
produit. La remontée demande un second geste que rien ne réclame — et
tant qu'elle n'est pas faite, le projet suivant repart sans la leçon,
c'est-à-dire qu'il la réapprendra en la payant.

---

## Le chemin par défaut : la feature

L'étalon est le mode non structuré : l'utilisateur dit une feature, un
écran tourne à la fin du tour. Si le processus produit moins que ça,
c'est le processus qui a tort.

Sur "je veux que…", "ajoute…", "l'écran doit…" → skill `feature-build`.
Elle construit d'abord et trace ensuite, dans le même tour.

Le circuit long (IDEA → grill → SPEC → BRIEF → TASK) existe pour ce qui
est cher à défaire : un contrat de données, un format d'échange, de
l'argent, de l'authentification. Pas pour le reste.

Et quand ce n'est pas le **quoi** qui est en jeu mais la **forme** — il
faut le faire, reste à savoir comment, et plusieurs manières tiennent
debout — la skill `conception-adverse` fait proposer par un agent et
attaquer par un autre avant qu'une ligne soit écrite. Une conception
faite seul converge vers la première idée : non parce qu'elle est bonne,
mais parce que chaque minute passée dessus la rend plus coûteuse à
abandonner.

---

## Devancer la demande

Écouter les utilisateurs produit des produits corrects. Aucun produit
marquant n'a été demandé : **on ne demande que ce qu'on sait déjà
nommer**. Un produit qui ne fait que ce qui a été dit reste plat, et il
le reste sans que personne s'en plaigne — c'est ce qui rend ce défaut
difficile à voir.

La règle est en deux temps, et le second n'annule pas le premier :

1. **Proposer ce que personne n'a demandé fait partie du travail.** Pas
   à la place de ce qui est demandé — en plus, et régulièrement.
2. **Ce qui est proposé se fait juger avant d'être construit.** La skill
   `devancer` tient les deux : `devanceur` propose (sept lentilles
   génératives, deux propositions au moins doivent déranger),
   `epreuve-du-reel` juge sur une échelle fermée et ne peut tuer qu'en
   nommant un empêchement.

`!` « Personne ne l'a demandé » n'est pas une objection recevable dans ce
dispositif ; « c'est ambitieux » non plus. Ce qui tue une proposition est
un empêchement nommé : un fait établi contredit, un ADR contredit, une
ressource que le terrain n'a pas, un tiers qui n'existe pas, un volume
qui n'arrivera pas, un risque que le produit a écrit refuser.

`!` Ne pas confondre avec `feature-scout`, qui **déduit** du produit ce
qui lui manque et répond à « qu'est-ce qui manque ». Ici on répond à
« qu'est-ce que personne n'a imaginé », et la réponse n'est pas dans le
produit.

### Un refus se défend comme une feature

Une section « ce que le produit ne fera pas » est utile — et elle devient
un réflexe dès qu'elle est gratuite. Chaque ligne dit **laquelle des
deux** elle est :

- une **contrainte** — une loi, un fait de terrain sourcé, une promesse
  déjà faite. Elle cite son DOM ou son ADR ;
- une **prudence** — un choix de portée. Elle dit ce qu'on gagne à ne pas
  le faire, et **ce qu'on perd**. Une prudence se rediscute ; une
  contrainte, non.

Un refus qui ne dit ni l'un ni l'autre est une opinion déguisée en règle.

### Une question dont la réponse est publique ne se pose pas

Quand un choix technique a une **convention établie** — le nom d'un
paramètre de redirection, un format d'échange, une structure d'URL, un
code de statut —, chercher ce qui se fait le plus et **proposer**, au
lieu de poser la question à froid. Poser une question dont la réponse
est publique coûte un tour pour rien.

Et la convention ne s'arrête presque jamais au nom : elle porte sa
précaution. `?next=` (Django), `callbackUrl` (NextAuth), `ReturnUrl`
(ASP.NET) sont la norme — et la norme inclut de n'accepter qu'un chemin
**interne**, sans quoi le produit devient un tremplin de redirection.
Rendre le nom sans la précaution, c'est n'avoir rien cherché.

`!` La question se pose quand elle est **propre au produit** : un
arbitrage de portée, une promesse, un compromis local. Là, personne
d'autre n'a la réponse, et `G2` tient — son avis l'emporte.

### Une page, c'est des fonctionnalités et une présentation

Les deux se traitent séparément, et dans cet ordre. Mélanger produit
toujours le même défaut : on discute d'une couleur avant de savoir ce que
la page doit permettre, et la fonction manquante se découvre une fois la
maquette faite. La skill `concevoir-une-page` tient l'ordre — les
fonctions d'abord (`suggester`), la présentation ensuite.

### Deux surfaces veut dire deux écrans, pas un écran rétréci

Le téléphone est le lieu du geste unique, à une main, sous mauvaise
connexion. **Il n'est pas la mesure de ce que le produit peut porter.**
Concevoir pour lui d'abord et « adapter » au grand écran produit un
produit plat des deux côtés : la densité que le bureau permet ne s'y
invente jamais après coup.

Quand un produit a deux surfaces, chacune a **son propre plan**. Le même
objet montré dans deux compositions, jamais la même composition à deux
tailles.

Deux agents portent ces paradigmes et se dispatchent **en parallèle**,
sans voir le travail l'un de l'autre : `designer-telephone` et
`designer-bureau`. Ils s'appuient sur une référence commune —
`design-direction/references/paradigmes-de-surface.md` : constantes
physiques, familles de motifs éprouvés, et quel design pour quel type
d'application. Un motif ne se cite pas pour sa notoriété, mais parce
qu'il résout le problème posé.

`!` Un même produit **change de famille** selon la surface : un outil
dense sur bureau peut être un outil de terrain sur téléphone. Ce n'est
pas une réduction, ce sont deux applications qui partagent une base de
données.

`!` Ce qu'un designer ne dessine pas : un logo, une icône, une
illustration. Il écrit un `PROMPT-nnn` (`visual-prompt`) et laisse le
trou. Un trou se voit et se comble ; un emoji posé en attendant reste.

---

## Rien ne se propose qui ne soit déjà écrit

Toute suite possible — un défaut trouvé en passant, une amélioration
entrevue, une question laissée ouverte par une relecture — **s'écrit
avant d'être proposée**. IDEA si c'est une idée, TASK si c'est du travail
identifié, la section « ce qui reste ouvert » de la TASK en cours si
c'est une conséquence de ce qu'on vient de faire.

Pourquoi cet ordre et pas l'inverse : une proposition orale n'a que deux
issues — **oui tout de suite, ou perdue**. Écrite d'abord, elle en a
trois : on la prend, on la rejette *avec sa raison consignée*, ou on fait
autre chose et elle attend sans se dissoudre. La troisième est la plus
fréquente, et c'est celle que l'oral détruit.

- La question de fin de tour ne fait donc que **désigner** ce qui existe
  déjà, avec son ID. Elle n'introduit rien.
- `!` Ne jamais présenter comme choix quelque chose dont l'utilisateur ne
  peut pas relire le détail. Un choix sans trace lui demande de se fier à
  une mémoire qui n'est pas la sienne.
- Écrire coûte trois lignes. Reconstruire de mémoire, deux tours plus
  tard, coûte le tour entier — et on ne reconstruit jamais la raison,
  seulement la conclusion.

### Une idée qui arrive en cours de route

Elle **passe devant**. Celui qui l'apporte sait ce qui compte, et
l'ordre du backlog n'est pas un argument contre.

Mais avant de la traiter, une vérification, et elle est mécanique :

> **Est-ce qu'une TASK ou une IDEA déjà écrite la contient ?**

Chercher le sujet dans `backlog/tasks/` et `product/ideas/`. Le résultat
s'annonce avant de commencer : « c'est TASK-nnn, je l'élargis » ou « rien
ne la couvre, je capture ».

Ce qu'on évite ainsi n'est pas du travail en double — c'est pire : deux
passages sur les mêmes fichiers, à deux moments, avec deux raisonnements
qui divergent. Le second ne sait pas ce que le premier a tranché.

---

## Le web est le lieu du développement

**Une feature se développe sur le web. Toujours.** Le mobile et le
desktop ne font que **porter** ce qui existe déjà — ils n'ajoutent jamais
un comportement que le web n'a pas.

Pourquoi cette règle et pas une autre : un cycle web est de quelques
secondes — enregistrer, recharger, voir. Un cycle mobile natif est de
quelques minutes — compiler, signer, installer, relancer. Développer une
feature dans le port multiplie ce coût par le nombre d'essais, c'est-à-dire
par beaucoup. Et une feature écrite deux fois diverge toujours.

- Une feature demandée « pour le mobile » se construit **sur le web**,
  puis se porte.
- Un port ne contient que : configuration de build, coquille native,
  branchements de capacités natives (caméra, biométrie, notifications),
  icônes et signature. **Aucune règle métier, aucun écran.**
- Un correctif qui ne concerne que le port (une marge sous l'encoche, un
  clavier qui recouvre un champ) se fait dans le CSS du web, pas dans le
  port. Le web doit rester juste tout seul.

### Un seul endroit où regarder

Un serveur de développement s'ouvre pour être **regardé**. S'il y en a
deux, l'un des deux ment — et rien ne dit lequel.

- **Avant d'ouvrir un port, libérer celui qui sert déjà le produit.** Pas
  « en ouvrir un autre à côté » : le port occupé est occupé par une
  version, et c'est celle-là qu'on va regarder par habitude.
- **Un serveur laissé derrière soi n'est pas neutre.** Il continue de
  servir l'état du code au moment où il a démarré. Plus le tour avance,
  plus ce qu'il montre est faux — et il ne le dit pas.
- **À la fin d'un tour, on referme ce qu'on a ouvert**, ou on écrit noir
  sur blanc ce qui reste ouvert, à quelle adresse, et de quand ça date.
- La même règle vaut pour une pile conteneurisée : une pile qui tourne
  sur d'anciennes images est un piège, pas une commodité. On la
  reconstruit, ou on l'arrête.

Le coût de l'oubli ne se paie pas sur sa propre machine : il se paie
quand quelqu'un d'autre ouvre l'adresse qu'on lui a donnée et juge le
produit sur une version morte.

**Cibles par défaut** : `PWA` sur téléphone, `Tauri v2` sur ordinateur.
On n'en change qu'en nommant la capacité qui manque.

Un port écrit dans un **autre langage** n'est pas un problème — Tauri est
en Rust, Capacitor colle du Swift et du Kotlin. Une **réécriture native**
(Flutter, Kotlin Multiplatform, React Native) n'est pas interdite non
plus : c'est une décision, qui s'écrit dans un ADR.

La seule ligne qui ne se négocie pas : **la logique qui décide de
ce qui est irréversible n'existe qu'une fois.** Un écran redessiné se
corrige ; une règle d'idempotence écrite deux fois diverge, et les deux
versions ont raison chacune de son côté. Ce qui ne se reprend pas prend
mille formes selon le produit — une valeur qui bouge, un droit accordé,
un envoi parti, un dossier détruit.

Le portage est une activité de **phase `pilote`** : on ne porte pas une
application qui n'est pas finie. Le hook `phase_guard.py` refuse d'écrire
sous `mobile/`, `desktop/`, `ios/` ou `android/` tant qu'une TASK `local`
est ouverte.

Un port se fait écran par écran, de mémoire — et **on ne voit pas ce
qu'on ne regarde pas**. Le trou ne se manifeste ni à la compilation ni à
l'ouverture des écrans portés : il se manifeste le jour où quelqu'un
cherche un réglage et ne le trouve pas. Donc **l'inventaire de ce qu'il
y a à porter se dérive de la source, jamais de tête**, et il vit dans
`product/assets/PARITE.md`, tenu par un test.

Un port n'est **jamais fini** tant que cette table n'est pas verte. Un
geste non porté n'est pas un oubli : c'est une TASK, ou une raison
écrite en toutes lettres.

Skills : `portage` choisit la cible et écrit le port ; `parite` vérifie
qu'il dit tout ce que la source dit.

---

## Conventions d'ID

Format strict : `<TYPE>-nnn` — exactement 3 chiffres, zéros inclus.
`ADR-001`, jamais `ADR-1` ni `ADR-0001`. Le hook rejette tout le reste.

IDEA-nnn    product/ideas/                idée, à n'importe quel stade
SPEC-nnn    product/specs/                comportement attendu, testable
BRIEF-nnn   product/specs/briefs/         spec compilée, prête à exécuter
ADR-nnn     product/decisions/            décision + alternatives écartées
DOM-nnn     product/domain/               fait de domaine, sourcé
TRC-nnn     product/domain/traces/        observation publique, sourcée, datée
SUG-nnn     product/domain/suggestions/   hypothèse retenue, non validée
INT-nnn     product/domain/interviews/    échange avec un expert
COPY-nnn    product/copy/                 texte destiné à l'utilisateur final
PROMPT-nnn  product/assets/prompts/       prompt de génération visuelle
TASK-nnn    backlog/tasks/                unité d'implémentation

Hors graphe — le hook les ignore (ni ID, ni frontmatter attendus) :
`product/grill/`, `product/legal/`,
`product/assets/DESIGN.md`, `product/JOURNAL.md`, `AMELIORATIONS.md`.

Avant d'attribuer un ID : lire `product/INDEX.md`, y compris la section
`## IDs réservés — archivés`. Un ID archivé n'est JAMAIS réattribué.

### Frontmatter — commun à tous
---
id: <TYPE>-nnn
title: ...
status: <voir ci-dessous>
links: [ID, ID]
updated: AAAA-MM-JJ
---

### Status valides, par type
IDEA    raw | parked | specd | killed
SPEC    specd | remplacée | caduque
BRIEF   draft | ready | shipped | caduc
ADR     actif | remplacé par ADR-nnn
DOM     raw | hypothèse | confirmé
TRC     raw | confirmé
SUG     pending | validé | invalidé | abandonné
INT     raw | confirmé
COPY    draft | retenu | rejeté
PROMPT  draft | generated | retenu | rejeté | remplacé par PROMPT-nnn | remplacé
TASK    todo | doing | done

`!` `PROMPT` porte **`remplacé` tout court**, en plus de « remplacé par
PROMPT-nnn », et ce n'est pas un doublon : un prompt peut être supplanté
par une solution qui **n'est pas un prompt** — une règle de style, un
composant, rien du tout. Sans ce mot, deux prompts restent `retenu` pour
un seul emplacement, et le filtre « ce qui est retenu » rend faux.


### Champs supplémentaires obligatoires
TASK    phase: local | pilote | dur
        origine: feature-build     (si la trace a été écrite après le code)
IDEA    origine: utilisateur | agent   contexte: <où l'idée est née>
DOM     source: <URL ou libellé stable>
SUG     question: <la question restée sans réponse>
        appelant: <skill ou agent>   preuve: <vide tant que pending>
TRC     source, type, echantillon        (régime `traces` — voir RIGUEUR.md)
INT     humain: oui | non
COPY    persona: <role>-persona (sauf auto-usage)
PROMPT  outil: <modèle utilisé>

`chemin: court` reste accepté sur une TASK, mais ne sert plus à
contourner un blocage : il n'y en a plus.

---

## Règles de graphe

Ce sont des constats, pas des barrières. Le hook les liste dans
`! Incohérences` ; rien ne s'arrête.

- Une SPEC cite l'IDEA dont elle vient.
- Un BRIEF cite au moins une SPEC.
- Une TASK cite une SPEC ou un BRIEF — sauf si elle porte
  `origine: feature-build | portage | parite` (trace écrite après le
  code, ou port d'un produit déjà spécifié) ou
  `chemin: court`. Le hook lit ces deux champs et dispense ; sans eux,
  il signale.
- Un COPY cite la SPEC ou l'IDEA qu'il sert.
- Un PROMPT cite le COPY ou la SPEC qui le motive.
- Un fait sans source est `[SUPPOSÉ]`, pas un DOM.
- Un BRIEF `ready` est immuable — une correction crée BRIEF-nnn+1 qui
  référence l'ancien.

### Hypothèses
Une option choisie dans une liste proposée par `suggester` reste
`[SUPPOSÉ]`. La cocher ne la transforme pas en fait.

  pending    retenu, sans preuve — **ne freine rien**
  validé     un TRC/INT/DOM postérieur le confirme (renseigner `preuve:`)
  invalidé   une preuve postérieure le contredit
  abandonné  l'option n'est plus dans le projet

Tout objet dont une décision repose sur un SUG `pending` le déclare dans
`links:`. C'est ce lien qui rend la dette visible — visible, pas bloquante.

---

## Recherche en ligne
Chercher librement. Ce qui est trouvé est écrit en DOM (ou TRC) avant
d'être utilisé, jamais gardé en tête. Priorité de sources : régulateur,
opérateur, documentation officielle, avant blogs et comparatifs.

Demander l'autorisation seulement si la recherche va coûter plusieurs
tours, ou sortir du sujet en cours.

---

## Rien ne s'écrit de mémoire

Un nom de fichier, une signature, le comportement d'un outil, **une
constante empruntée à un autre projet** : ça se lit chez son auteur. Un
défaut, lui, se **reproduit** avant de se corriger — sans ça c'est une
hypothèse, pas un défaut.

Pourquoi cette règle et pas une autre : écrire de mémoire ne produit
presque jamais une erreur franche. Ça produit du **plausible** — qui passe
la relecture, qui passe la capture d'écran, et qui casse plus loin. Le coût
ne se paie pas à l'écriture, il se paie en tours.

- Quand un outil sait poser une valeur, le laisser faire plutôt que la
  retaper.
- Une hypothèse énoncée se **nomme** hypothèse, avec ce qui la confirmerait.
- Une valeur reprise à un projet tiers **cite le fichier d'où elle vient**.
  « relevé dans `src/svg.ts` de chessground » vaut mieux que la valeur
  seule : le prochain qui la trouve suspecte saura où vérifier, au lieu de
  la retoucher au jugé.

`!` Le piège propre à un système emprunté, c'est que **le souvenir en est
inégal**. Sur cinq teintes de pinceau reprises à chessground, les cinq
étaient justes ; sur cinq valeurs de géométrie du même fichier, quatre
étaient fausses — dont un trait deux fois et demie trop épais. Rien de tout
ça ne se voit sur une capture isolée : tout se voit à côté de l'original.
Et c'est d'avoir raison sur la moitié visible qui rend l'autre moitié
crédible.

---

## Le défaut qui ne lève rien

Un défaut qui plante se signale lui-même. Le défaut coûteux ne lève rien :
il rend un **compte faux**. Et il le rend précisément dans l'écran dont le
compte est la raison d'être.

Cas d'espèce : deux entrées de cache pour une même partie, parce que
l'identifiant était le condensat d'un texte non normalisé — l'export NDJSON
de Lichess termine le PGN par deux sauts de ligne de plus que
`/game/export`. Trois octets. Aucune exception, aucune trace, et la vue
« Motifs » comptait la partie deux fois et chacun de ses motifs deux fois.

- **Un identifiant dérivé d'un texte venu du dehors se normalise avant de
  se hacher.** Deux portes d'entrée pour la même donnée, c'est deux formats
  jusqu'à preuve du contraire.
- Une vue qui compte se vérifie **sur son compte**, pas sur son rendu : le
  nombre de fichiers n'est pas le nombre d'objets.
- Quand un symptôme et un défaut apparaissent dans le même tour, la
  tentation est de les relier. Ici le doublon était réel *et* n'expliquait
  pas le symptôme — la variante servie faisait bien deux coups, parce que
  le moteur tourne sous plafond de temps. **Diagnostiquer sur la donnée
  servie, jamais sur celle qu'on croit servie.**

`!` Corollaire d'affichage : une évaluation, une date, un numéro de coup
**signent la position qui est à l'écran**. Dès que l'écran montre autre
chose — une variante d'entraînement, une prévisualisation — la légende qui
n'a pas suivi ne décore pas, elle ment.

Et quand deux vues montrent la même chose — l'échiquier et sa légende, la
liste et son compteur — elles se dérivent d'**une seule fonction**. Filtrées
chacune de son côté, elles finissent par ne plus avoir les mêmes indices,
et le survol de la troisième ligne éteint la deuxième flèche.

---

## Une mesure se mesure aussi

Une vérification qui ne peut pas réussir rend le même verdict que le
défaut qu'elle cherche. C'est un faux négatif, et un faux négatif ne
ressemble pas à une panne : il ressemble à un résultat.

Cas d'espèce : pour vérifier une animation, j'ai relevé
`el.style.transform` — le style **en ligne**. Or la technique employée
(FLIP) pose ce style à sa valeur finale dès le premier tour et laisse la
transition CSS interpoler dans le style **calculé**. La mesure affichait
donc l'arrivée à 30 ms comme à 400 ms, et se lisait « rien ne bouge ».
L'animation marchait. Il s'en est fallu d'un tour que je répare du code
juste.

- **Avant de croire une mesure négative, lui montrer un cas positif.**
  Ici `prefers-reduced-motion` sert de témoin : la même sonde rend 0 image
  en vol quand l'animation est coupée, et 11 quand elle ne l'est pas.
  Deux nombres différents prouvent que la sonde regarde quelque chose.
- Une sonde qui n'a jamais rien vu bouger n'a rien prouvé — elle n'a même
  pas prouvé qu'elle fonctionne.
- Le corollaire vaut pour les tests : un test qui passe du premier coup
  sur un défaut qu'on vient de corriger doit être vu **échouer** sur le
  code d'avant, sinon on ne sait pas ce qu'il tient.

`!` Le piège est plus vicieux qu'une sonde muette, qui se remarque. Ici
la sonde parlait, elle rendait des chiffres plausibles et cohérents entre
eux — simplement, c'étaient toujours les mêmes.

---

## Design

Avant le premier écran : skill `design-direction`. Elle écrit
`product/assets/DESIGN.md` (tokens, composants, ce qu'on ne fait jamais)
à partir de 3 à 5 produits réels du domaine.

Tout écran est confronté à `DESIGN.md` avant d'être écrit. Un écran qui
s'en écarte s'écarte volontairement, et le dit.

`phase_guard.py` refuse tout fichier d'écran sous `src/` tant que
`DESIGN.md` est absent. Ce n'est pas un avertissement.

---

## Archivage
Va dans `product/archive/` (sous-chemin d'origine conservé) :
IDEA killed, SPEC/BRIEF caducs, SUG abandonné, TRC dont la source a disparu.

N'y va JAMAIS : un ADR (une décision reste vraie même remplacée — marquer
`status: remplacé par ADR-nnn`), un INT, un DOM (une observation ne
devient pas fausse, elle vieillit).

On archive, on ne supprime pas. Le frontmatter reste intact.

---

## Navigation
`product/INDEX.md` est régénéré par `.claude/hooks/graph_index.py` aux
événements SessionStart et Stop. Ne jamais l'éditer à la main.
La skill `graph-index` sert à LIRE l'index et à réparer le graphe.

Ouvrir `product/` comme coffre Obsidian : les `[[ID]]` deviennent
cliquables, la vue graphe est native.

---

## Répartition avec Superpowers

Ce dépôt gère l'AMONT : quoi construire, pourquoi, dans quel ordre.
Superpowers gère l'AVAL : comment le construire correctement.

- En phase `local`, `feature-build` construit directement. Superpowers
  n'est pas convoqué pour un écran de démo.
- En phase `pilote` et au-delà, un BRIEF `ready` passe la main à
  Superpowers via `/write-plan` ou `/execute-plan`, jamais en paraphrasant
  le BRIEF dans le chat.
- Retour : TASK `done`, BRIEF `shipped`. Si l'implémentation révèle un
  manque, capturer en IDEA — ne pas patcher un BRIEF `ready`.

Ce qu'on ne réécrit jamais : TDD, débogage systématique, revue en deux
temps, sous-agents, plans d'exécution. Toute skill locale qui recouvre
ça est à supprimer — le hook le signale.

Collision de vocabulaire : `/brainstorm` de Superpowers raffine une
exigence avant code ; nos grills décident s'il faut construire.

---

## Budget de contexte au SessionStart
Superpowers et notre hook injectent tous les deux. Le nôtre tient en
4 lignes quand tout va bien, jusqu'à 8 quand plusieurs constats tombent.
Si le SessionStart devient lourd, retirer le hook `Stop` avant de
toucher au `SessionStart`.
