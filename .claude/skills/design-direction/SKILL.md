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
Chercher en ligne **3 à 5 produits réels** proches du domaine — pas des
dribbble shots, pas des templates : des produits que des gens utilisent.
Privilégier ceux du même contexte géographique et matériel que
l'utilisateur final.

Pour chacun, relever, factuellement :
- **structure de navigation** — combien de niveaux, où vit l'action
  principale, ce qui est toujours visible
- **densité** — combien d'objets par écran, tailles de cible tactile
- **typographie** — familles, nombre de tailles réellement utilisées,
  graisses
- **palette** — combien de couleurs portent du sens, laquelle est la
  couleur d'action, comment le succès et l'échec sont signalés
- **états d'erreur et de chargement** — la partie que tout le monde
  saute et qui distingue un produit d'une maquette

Écrire ce qui est trouvé en `DOM-nnn` (avec `source:`), pas en mémoire.

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
    (bouton primaire/secondaire, champ, carte, badge de statut, montant,
     état vide, erreur en ligne, indicateur de chargement)

    ## États — obligatoires pour chaque écran
    - vide, chargement, erreur récupérable, erreur définitive, succès

    ## Ce qu'on ne fait JAMAIS
    - <interdits explicites, tirés du contexte d'usage>

## 4. Sortie — ≤ 6 bullets
## DESIGN.md écrit — <chemin>
## Parti retenu — <une ligne, avec le sacrifice>
## Références — <les produits, avec leur DOM>
## → Le refus d'écran est levé

---

# MODE UX/UI SENIOR — à chaque écran

Déclenché quand `DESIGN.md` existe et qu'un écran est à écrire ou à revoir.

## Avant d'écrire
Lire `DESIGN.md`. Puis, en 4 bullets maximum :
- **Le travail de l'écran** — la seule chose que l'utilisateur vient y
  faire. Une seule. S'il y en a deux, c'est deux écrans.
- **La hiérarchie** — ce qui est lu en premier, deuxième, jamais.
- **Les cinq états** — vide, chargement, erreur récupérable, erreur
  définitive, succès. Aucun ne se découvre en production.
- **Ce que je réutilise** — les composants existants, nommés.

## Pendant
- Aucune valeur en dur : tout passe par les tokens. Une couleur écrite en
  hexadécimal dans un composant est un bug.
- Un seul accent par écran. Deux boutons primaires n'existent pas.
- Le montant, la date et le statut sont formatés au même endroit, partout.
- L'action principale est atteignable au pouce si le contexte est mobile.

## Après — confrontation
Dispatcher l'agent `design-critic` sur l'écran écrit. Il a un contexte
vierge : il voit ce que la session a cessé de voir. Appliquer ce qu'il
remonte, ou écrire pourquoi on ne l'applique pas.

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
- Sortir un design "moderne", "épuré", "premium" : ces mots ne décrivent
  rien. Décrire ce qui est à l'écran.
- Copier une esthétique occidentale par défaut quand le contexte d'usage
  dit autre chose.
- Établir la direction sans avoir regardé de vrais produits.
