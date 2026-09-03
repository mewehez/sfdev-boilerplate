---
name: design-direction
description: Établit la direction de design du produit puis tient le rôle
  d'UX/UI senior sur chaque écran. Déclencher AVANT le premier écran, ou
  sur "le design", "à quoi ça ressemble", "l'interface", "c'est moche",
  "rends ça cohérent". Écrit product/assets/DESIGN.md.
---

# Direction de design

Le hook `phase_guard.py` refuse tout fichier d'écran sous `src/` tant que
`product/assets/DESIGN.md` n'existe pas. Cette skill est ce qui lève le
refus. Elle prend un tour, pas une session.

Deux modes.

---

# MODE ÉTABLIR — une seule fois par projet

Déclenché quand `product/assets/DESIGN.md` n'existe pas.

## 1. Regarder ce qui existe vraiment
Passer par la skill `references-croisees`. Elle impose ce qui ne vient
pas naturellement : **au moins deux références hors du domaine**, et
l'écriture de ce que les produits proches font **mal**.

Chercher en ligne **3 à 5 produits réels** proches du domaine — pas des
dribbble shots, pas des templates : des produits que des gens utilisent.
Privilégier ceux du même contexte géographique et matériel que
l'utilisateur final.

`!` Et ne pas s'aligner sur eux par défaut. Dans les métiers où le
logiciel est acheté par quelqu'un qui ne s'en sert pas, les produits
dominants sont complets et pénibles : s'aligner revient à copier leurs
défauts. C'est là que les références lointaines gagnent leur place.

**Ce qu'une recherche textuelle donne vraiment** — le relever, l'écrire
en `DOM-nnn` avec sa `source:`, et s'en servir pour trancher le parti :
- ce que le produit met en avant : l'action qu'il rend évidente, ce qu'il
  relègue, combien de niveaux de navigation il assume
- les gestes réels du métier — un code dicté à voix haute, un scan, un
  numéro tapé. Ils écrivent l'interface plus sûrement qu'une palette.
- les contraintes documentées : délais, plafonds, frais, codes d'erreur
- les états que le produit doit couvrir, déduits de ses modes de panne

**Ce qu'elle ne donne jamais** : une valeur de couleur, un nom de police,
une densité mesurée. Ne pas prétendre les avoir trouvées.
- `? Tu as une capture d'écran d'un de ces produits ?` — poser une fois.
  Si oui, la lire. Si non, avancer : ce n'est pas une condition.
- Sans capture, la palette et la typographie sont des **choix**, dérivés
  du contexte d'usage (§ Contexte) et non d'une référence. `DESIGN.md`
  doit le dire, à sa section Références.

## 2. Trancher
Ne pas moyenner les cinq. Choisir **un parti** et nommer ce qu'il
sacrifie. Un design qui ne sacrifie rien n'en est pas un.

## 3. Écrire product/assets/DESIGN.md
Hors graphe : pas de frontmatter, pas d'ID. C'est une référence, pas un
nœud.

    # Direction de design — <projet>

    ## Parti
    - <une phrase : ce que l'interface privilégie, et ce qu'elle sacrifie>
    ## Références
    - <produit> — <ce qu'on lui prend> [DOM-nnn]
    <!-- Ce qui vient d'une capture est sourcé. Ce qui vient du contexte
         d'usage est un choix : le dire, ne pas l'habiller en référence. -->
    ## Contexte d'usage
    - <appareil, taille d'écran, luminosité, connexion, main libre ou non>

    ## Tokens
    ### Couleurs
    - `--bg`, `--surface`, `--text`, `--text-muted`, `--border`
    - `--accent` (action), `--success`, `--warning`, `--danger`
    - valeurs en clair ET en sombre, chacune définie explicitement
    ### Espacements
    - échelle fermée : 4 / 8 / 12 / 16 / 24 / 32 / 48 — rien d'autre
    ### Rayons
    - 2 valeurs maximum
    ### Typographie
    - une famille, deux au plus ; échelle fermée de 4 à 6 tailles
    - graisses utilisées, avec leur rôle

    ## Composants de base
    - <nom> — quand l'utiliser, quand ne pas l'utiliser
    <!-- Cette table est aussi le registre des NOMS pris. Avant d'en
         créer un, la relire : une collision de classes ne se voit pas
         dans le gabarit, elle se voit à l'écran, plus tard. -->
    (bouton primaire/secondaire, champ, carte, badge de statut, montant,
     état vide, erreur en ligne, indicateur de chargement)

    ## États — obligatoires pour chaque écran
    - vide, chargement, erreur récupérable, erreur définitive, succès

    ## Promesses faites à l'utilisateur
    - <ce que l'interface AFFIRME : « nous ne stockons jamais X »,
       « vous voyez toujours Y ». Chacune engage tout le produit,
       y compris les écrans qui n'existent pas encore.>

    ## Ce qu'on fait TOUJOURS
    - <exigences positives. Cette section est OBLIGATOIRE, et elle
       n'est pas la négation de la suivante.

       ! Un jeu de règles uniquement soustractif produit des écrans qui
       ne font rien de mal et ne donnent envie à personne — ils passent
       tous les contrôles, parce que les contrôles ne cherchent que des
       fautes. Constaté, et corrigé par cette section.

       Le socle en impose quatre, le domaine en ajoute :
       - le geste principal de l'écran est atteignable sans changer de
         mode, et c'est le geste le moins cher de l'écran
       - ce qui découle d'un toucher apparaît à l'endroit touché
       - un retour d'action est continu chaque fois qu'il peut l'être,
         jamais un simple compteur
       - un écran contient au moins une chose qu'on raconterait à
         quelqu'un d'autre. Sans ça, il est correct et mort.>

    ## Ce qu'on ne fait JAMAIS
    - <interdits explicites, tirés du contexte d'usage>
    - <et celui-ci, toujours : ajouter une phrase d'instruction pour
       clore un problème d'interaction. Une phrase nécessaire est l'aveu
       d'une forme ratée — elle s'inscrit dans la TASK comme un défaut.>

## 4. Sortie — ≤ 6 bullets
## DESIGN.md écrit — <chemin>
## Parti retenu — <une ligne, avec le sacrifice>
## Références — <les produits, avec leur DOM>
## → Le refus d'écran est levé

---

# MODE UX/UI SENIOR — à chaque écran

Déclenché quand `DESIGN.md` existe et qu'un écran est à écrire ou à revoir.

## Avant d'écrire
Lire `DESIGN.md`, **§ Promesses en premier**. Puis, en 4 bullets maximum :

- **La promesse que cet écran met en jeu** — laquelle des affirmations
  déjà faites ailleurs cet écran pourrait-il rendre fausse ? Une feature
  qui contredit une promesse écrite est un bug, même si elle marche.
- **Le travail de l'écran** — la seule chose que l'utilisateur vient y
  faire. Une seule. S'il y en a deux, c'est deux écrans.
- **La hiérarchie** — ce qui est lu en premier, deuxième, jamais.
- **Les cinq états** — vide, chargement, erreur récupérable, erreur
  définitive, succès. Aucun ne se découvre en production.
- **Le refus** — si l'écran a un formulaire : que se passe-t-il quand
  il est incomplet ? Un bouton grisé ne dit pas CE QUI manque. On laisse
  cliquer et on répond sur le champ fautif. Un bouton ne se désactive
  que si la raison est affichée à sa place.
- **Ce que je réutilise** — les composants existants, nommés.
- **Les noms que j'introduis** — vérifiés contre la table des composants
  de `DESIGN.md`. Un nom déjà pris hérite silencieusement d'une autre
  mise en page.

## Pendant
- **La skill `geste-direct` avant d'écrire l'écran**, dès qu'il contient
  un geste. Elle rend une table — geste principal et son coût, commandes
  qui doublent un geste natif, modes, phrases d'instruction, retours. Cette
  table est ensuite vérifiée contre le code par `design-critic` : sans
  cette vérification, elle reste une intention.
- Aucune valeur en dur : tout passe par les tokens. Une couleur écrite en
  hexadécimal dans un composant est un bug.
- Un seul accent par écran. Deux boutons primaires n'existent pas.
- Le montant, la date et le statut sont formatés au même endroit, partout.
- L'action principale est atteignable au pouce si le contexte est mobile.

## Après — confrontation, en deux temps
1. `design-critic` sur l'écran écrit. Il a un contexte vierge : il voit
   ce que la session a cessé de voir. Appliquer ce qu'il remonte, ou
   écrire pourquoi on ne l'applique pas.
2. **`directeur-artistique` ensuite**, et seulement ensuite — son travail
   commence là où la conformité s'arrête. `design-critic` cherche des
   fautes ; lui refuse le tiède, et doit citer un produit qui fait mieux.

`!` Ne pas déclarer un écran fini avant ces deux passages. Un écran sans
faute n'est pas un écran réussi.

## Sortie — ≤ 6 bullets
## Écran — <nom> : <son travail en une ligne>
## Hiérarchie — <1er / 2e / relégué>
## États couverts — <les 5, ou ce qui manque et pourquoi>
## ! Écart à DESIGN.md — <l'écart assumé, ou "aucun">

---

## Interdits
- Écrire un écran sans avoir lu `DESIGN.md` dans le tour courant.
- Ajouter une couleur, une taille ou un espacement hors des tokens.
  Si le token manque, modifier `DESIGN.md` d'abord — et le dire.
- Livrer un écran sans état d'erreur ni état de chargement.
- Désactiver un bouton sans afficher pourquoi. Le grisé est un refus
  muet : l'utilisateur cherche, ne trouve pas, et part.
- Répéter la marque sur un écran d'usage. Elle sert là où quelqu'un ne
  sait pas encore où il est, nulle part ailleurs.
- Laisser une page de réglages dépasser deux écrans : chaque groupe
  devient sa page, avec son retour.
- Mélanger un contrôle natif du navigateur (date, couleur, sélecteur)
  avec des contrôles maison. Il arrive avec ses tailles et son
  vocabulaire ; le produit n'a qu'un seul objet par geste.
- Sortir un design "moderne", "épuré", "premium" : ces mots ne décrivent
  rien. Décrire ce qui est à l'écran.
- Copier une esthétique occidentale par défaut quand le contexte d'usage
  dit autre chose.
- Établir la direction sans avoir regardé de vrais produits.
- Présenter une palette ou une typographie comme « reprise de X » quand
  elle n'a pas été vue. Un choix assumé vaut mieux qu'une fausse source.
