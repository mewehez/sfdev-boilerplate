# Les deux paradigmes — ce qui ne se transpose pas

Référence commune à `designer-telephone` et `designer-bureau`. Elle ne
décrit pas un style : elle décrit **ce que l'appareil impose**, ce que
les systèmes établis en ont tiré, et ce qui échoue quand on transpose.

`!` Une surface n'est pas une taille d'écran. C'est un couple **appareil
+ posture** : ce que la main peut atteindre, ce que l'œil embrasse, et
combien de temps la personne restera.

---

## 1. Ce que l'appareil impose

| | téléphone | bureau |
|---|---|---|
| entrée | doigt, imprécis, opaque (la main cache) | pointeur précis + clavier |
| survol | **n'existe pas** | existe, et porte l'action secondaire |
| champ visuel | une chose à la fois | plusieurs zones simultanées |
| posture | debout, en marchant, interrompu | assis, en session, répétitif |
| durée | secondes | dizaines de minutes |
| erreur | coûteuse : refaire demande de revenir | bon marché : annuler suffit |
| réseau | variable, parfois absent | stable |
| sortie | rien n'est imprimé | on imprime, on exporte, on présente |

**La conséquence qui commande tout** : sur téléphone on **lit, confirme
et capture** ; sur bureau on **compose, compare et corrige**. Une
interface qui fait composer au pouce, ou lire une chose à la fois sur
1440 px, se trompe de paradigme — pas de taille.

---

## 2. Constantes physiques, non négociables

**Téléphone**
- Cible tactile : **44 × 44 pt** (Apple HIG) / **48 × 48 dp** (Material 3).
  En deçà, l'échec de frappe se mesure, il ne se discute pas.
- Zone du pouce : le **tiers bas** de l'écran. Ce qui engage y vit ; ce
  qui détruit n'y vit pas.
- Champ de saisie : **16 px minimum**. En dessous, iOS zoome à la mise
  au point et l'écran saute.
- Zones sûres : encoche, barre de gestes, coins arrondis.
- Une main : le haut de l'écran est atteignable en se contorsionnant.
  Un geste principal en haut à droite est un geste à deux mains.

**Bureau**
- Cible pointeur : 24 à 32 px suffisent ; l'espace gagné va à la densité.
- La ligne de texte reste lisible entre **45 et 75 caractères** — d'où
  des colonnes, pas une ligne de 1400 px.
- Le survol révèle, il ne cache jamais l'information nécessaire :
  ce qui n'est visible qu'au survol n'existe pas pour qui ne survole pas.
- Le clavier est une entrée première, pas un raccourci d'expert : Échap,
  Entrée, Tab, flèches, et une palette de commandes au-delà d'une
  vingtaine d'actions.

---

## 3. Les familles de motifs qui ont fait leurs preuves

### Téléphone

| motif | quand | ce qu'il remplace |
|---|---|---|
| barre d'onglets basse, 3 à 5 destinations | navigation de pair, plate | un menu latéral |
| **feuille basse** (bottom sheet) | choix ou détail bref sans quitter | une boîte modale centrée |
| une question par écran | saisie longue, formulaire | un formulaire à dix champs |
| action principale ancrée au pouce | un seul geste engage l'écran | un bouton en haut à droite |
| liste, pas tableau | données à parcourir | quatre colonnes serrées |
| dévoilement progressif | l'essentiel d'abord, le reste au geste | tout affiché, plus rien lu |
| glissement latéral **en doublon** d'un bouton | raccourci d'habitué | un glissement seul, invisible |
| squelette de chargement | attente > 300 ms | un rouet qui ne dit rien |
| état vide qui **instruit** | zéro élément | « aucune donnée » |

### Bureau

| motif | quand | ce qu'il remplace |
|---|---|---|
| **maître-détail** (liste + panneau) | parcourir puis agir, sans perdre sa place | une navigation page à page |
| tableau dense, en-tête collant, tri | comparer des lignes homogènes | des cartes empilées |
| barre latérale sectionnée | plus de cinq destinations | un menu caché derrière trois traits |
| panneau d'inspection à droite | propriétés de l'objet sélectionné | une page d'édition séparée |
| édition en ligne | corriger une valeur parmi cent | un formulaire modal par ligne |
| sélection multiple + action groupée | le même geste sur dix objets | dix fois le même geste |
| palette de commandes (`Cmd+K`) | au-delà d'une vingtaine d'actions | un menu à trois niveaux |
| annuler plutôt que confirmer | action réversible et fréquente | une confirmation à chaque fois |
| survol pour révéler le secondaire | actions rares sur une ligne | trois boutons sur chaque ligne |
| vue scindée / deux volets | comparer, ou éditer en voyant le résultat | un aller-retour |

### Ce qui échoue en traversant

- **Téléphone → bureau** : une colonne unique centrée sur un écran large.
  L'espace n'est pas un luxe, c'est la matière de la comparaison. Un
  outil professionnel qui n'affiche qu'un objet à la fois oblige à tenir
  le reste de mémoire.
- **Bureau → téléphone** : un tableau qui défile horizontalement, un
  survol qui porte une action, une boîte modale qui couvre le contexte,
  un formulaire à douze champs.
- **Les deux sens** : la même composition redimensionnée. Deux surfaces
  veut dire **deux compositions du même objet**, jamais une composition
  à deux tailles.

---

## 4. Quel design pour quel type d'application

Le type d'application commande plus que le goût. Se tromper de famille
produit une interface correcte et inadaptée.

| type | ce qui compte | famille de motifs | à regarder |
|---|---|---|---|
| **outil professionnel dense** (suivi, ERP, gestion) | densité, vitesse, clavier, comparaison | maître-détail, tableaux, palette, raccourcis | Linear, Height, Superhuman, Stripe Dashboard |
| **espace de composition** (documents, plans, design) | canevas maximal, outils périphériques, annuler | canevas + inspecteur, calques, zoom | Figma, Notion, Excalidraw |
| **grand public transactionnel** (payer, réserver, valider) | une décision claire, zéro ambiguïté, confiance | une action par écran, récapitulatif, preuve | Stripe Checkout, Wise, Revolut |
| **terrain / mobilité** (saisir sur place, hors bureau) | une main, gros doigts, réseau incertain, soleil | listes, contraste fort, saisie brève, hors-ligne | WhatsApp, Google Maps en navigation |
| **lecture / contenu** | rythme de lecture, hiérarchie typographique | colonne mesurée, titres, images | Stripe Docs, Substack |
| **tableau de bord** | ce qui a changé, l'anomalie | un chiffre de tête, séries, filtres | Datadog, Vercel |

`!` Un même produit change de famille selon la surface. Un ERP est un
**outil dense** sur bureau et un **outil de terrain** sur téléphone. Ce
n'est pas une réduction : ce sont deux applications qui partagent une
base de données.

---

## 5. Les systèmes établis, et ce qu'on leur emprunte

- **Apple HIG** — la hiérarchie tactile, les feuilles, les zones sûres,
  le refus des commandes cachées. À suivre sur téléphone même hors iOS.
- **Material 3** — les cibles 48 dp, l'élévation qui signifie une
  couche, la barre de navigation basse, les états de composant.
- **Systèmes professionnels** (Carbon d'IBM, Fluent de Microsoft,
  Atlassian, Polaris de Shopify) — la densité assumée, les tableaux, les
  panneaux, les états vides qui instruisent.
- **Ce qu'on n'emprunte pas** : leur identité visuelle. On emprunte des
  **résolutions de problème**, pas une esthétique. Un produit qui
  ressemble à Material est un produit sans visage.

`!` Un motif ne se cite pas parce qu'il est connu, mais parce qu'il
résout **le problème posé**. Une palette de commandes dans un produit à
six actions est une citation, pas une décision.

---

## 6. Ce qui reste vrai des deux côtés

- Une seule action principale par écran et par surface.
- Ce qui est irréversible se dit **au geste**, pas dans une aide.
- Un état vide instruit ; il ne constate pas.
- Le mouvement sert à expliquer un changement de lieu, jamais à décorer.
- Le contraste et la taille de texte sont des contraintes
  d'accessibilité, pas des variables de style : 4,5:1 sur le texte
  courant, cible atteignable au clavier, ordre de tabulation qui suit
  l'ordre visuel.
- Ce qui n'a pas de nom dans le registre de composants du produit
  n'existe pas : un motif importé se nomme avant d'être posé.
