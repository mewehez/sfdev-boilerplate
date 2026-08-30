---
name: portage
description: Porte l'application web existante vers un téléphone ou un
  ordinateur — PWA, Capacitor, Tauri. Déclencher sur "je veux le voir sur
  mon téléphone", "en faire une vraie app", "sur l'App Store", "une appli
  desktop", "installable". Ne développe jamais de feature.
---

# Portage

## La règle avant tout
**Une feature se développe sur le web. Le port ne fait que l'emballer.**

Un cycle web dure quelques secondes : enregistrer, recharger, voir. Un
cycle natif dure quelques minutes : compiler, signer, installer,
relancer. Développer dans le port multiplie ce coût par le nombre
d'essais. Et une feature écrite deux fois diverge toujours.

Si l'utilisateur demande une feature « pour le mobile » : la construire
sur le web avec `feature-build`, puis revenir ici. Le dire en une ligne,
sans négocier.

Le portage est de **phase `pilote`**. `phase_guard.py` refuse d'écrire
sous `mobile/`, `desktop/`, `ios/` ou `android/` tant qu'une TASK `local`
est ouverte — on ne porte pas une application inachevée.

---

## Les défauts, décidés une fois pour toutes
- **Mobile → PWA.**
- **Desktop → Tauri v2.**

Ce sont les points de départ. On n'en change qu'en nommant la capacité
qui manque, et en l'écrivant dans un ADR.

## Choisir la cible — quatre marches, dans cet ordre

Ne jamais monter une marche sans que la précédente soit insuffisante.
Chaque marche coûte un ordre de grandeur de plus que la précédente.

### 1. PWA — presque gratuit, commence toujours ici
Un manifeste, un service worker, des icônes. L'application s'installe
depuis le navigateur, s'ouvre en plein écran, a son icône.

**Ce que ça donne** : écran d'accueil, plein écran sans barre de
navigateur, écran de démarrage, mode hors ligne pour la coquille.
**Ce que ça ne donne pas** : caméra en arrière-plan, biométrie,
notifications poussées sur iOS hors app installée, présence en magasin.

**Quand c'est la bonne réponse — souvent** : un utilisateur sur un
réseau lent ou un forfait compté. Pas de magasin, pas de
téléchargement de plusieurs dizaines de mégaoctets, pas de mise à jour
à installer. Sur un marché où la donnée se paie au mégaoctet, c'est un
argument produit, pas un compromis technique.

### 2. Capacitor — quand une capacité native manque vraiment
Emballe le web dans une coquille native iOS et Android, et donne accès
au matériel par des greffons.

**Ne monter ici que si l'une de ces choses est nécessaire** :
- lecture de code-barres ou de QR **par la caméra**, dans l'app
- déverrouillage **biométrique**
- **notifications poussées** fiables, application fermée
- stockage chiffré par le système
- présence dans un **magasin d'applications**, parce qu'on la demande

**! Ce que ça exige du web** : Capacitor embarque des fichiers
statiques. Une application **rendue côté serveur** ne s'embarque pas
telle quelle — il faut soit pointer la coquille vers un serveur distant
(et l'app n'est alors qu'un navigateur déguisé, sans mode hors ligne),
soit extraire la partie cliente. **Le dire avant de commencer.** C'est le
piège classique de cette marche.

### 3. Tauri v2 — le défaut pour le desktop
Binaires très légers, cœur Rust, iOS et Android depuis la v2.
**C'est le défaut sur ordinateur**, sans discussion préalable.

Le cœur est en Rust : **un port dans un autre langage n'est pas un
problème**. Une coquille écrite ailleurs que dans le langage du produit,
c'est la norme — Capacitor colle du Swift et du Kotlin, Tauri du Rust.

### 4. Réécriture native — Flutter, Kotlin Multiplatform, React Native
**Ce n'est pas interdit.** C'est une décision, pas une dérive.

Elle se prend les yeux ouverts, avec un ADR qui répond à une seule
question :

> **Qu'est-ce qui va exister en deux exemplaires, et comment on
> garantit qu'ils disent la même chose ?**

Ce qui coûte n'est pas le langage : c'est la **duplication d'une règle**.
Un écran redessiné dans un autre langage se corrige. Une règle d'argent
— idempotence, réconciliation, calcul d'un solde — écrite deux fois
diverge, et les deux versions ont raison chacune de son côté.

Donc, dans l'ADR :
- **La logique qui décide de l'argent n'existe qu'une fois.** Soit elle
  reste sur le serveur et l'app est un client ; soit elle est déplacée,
  et le serveur consomme la même. Jamais deux implémentations.
- Ce qui est légitimement réécrit : écrans, navigation, colle native.
- Ce qui ne l'est jamais : les invariants, testés une seule fois.

Si l'utilisateur choisit une réécriture, l'accompagner. Ne pas y revenir
à chaque tour.

---

## Procédure

### 1. Vérifier que le web est prêt
- Toutes les TASK `local` sont `done` — sinon le hook refusera de toute
  façon.
- L'application est utilisable au clavier et lisible à 360 px de large.
- `product/assets/DESIGN.md` respecte déjà `env(safe-area-inset-*)` :
  une encoche se traite en CSS, pas dans le port.

### 2. Nommer la capacité manquante
Une seule question :
`? Qu'est-ce que le navigateur ne sait pas faire, et dont tu as besoin ?`

- Rien, sur téléphone → **PWA**. C'est le défaut, s'arrêter là.
- Poste de travail → **Tauri v2**. C'est le défaut, s'arrêter là.
- Caméra, biométrie, notifications, magasin → **Capacitor**.
- Une raison assumée d'écrire une app native → **marche 4**, avec son
  ADR et la question de ce qui existera en double.

Écrire un ADR : la cible retenue, la capacité qui la justifie, les
marches écartées et pourquoi.

### 3. Porter
Le port vit dans `mobile/` ou `desktop/`. Il ne contient que :
- configuration de build, identifiants d'application, signature
- coquille native et sa configuration
- branchements de capacités natives, **fins** : appeler le web, pas
  décider à sa place
- icônes et écrans de démarrage

Chaque capacité native est appelée depuis le web derrière un test de
disponibilité, pour que **le web reste utilisable seul**. Un port ne rend
jamais le web moins bon.

### 4. Vérifier sur l'appareil
Ne pas conclure sur un émulateur seul. Contrôler : encoche haute et
barre de geste basse, clavier qui ne recouvre pas le champ actif, retour
arrière du système, rotation, et la coupure réseau — c'est le cas qui
compte le plus.

## Sortie — ≤ 8 bullets
## Cible — <PWA | Capacitor | Tauri> · <la capacité qui la justifie>
## Écarté — <les marches non prises, en une ligne chacune>
## Ajouté — <chemins créés>
## Le web n'a pas bougé — <ou ce qui a changé, et pourquoi>
## Tourne avec — `<commande>` → <ce qu'on doit voir>
## → À vérifier sur l'appareil : <la liste courte>

---

## Interdits
- Développer une feature dans le port. Jamais, sous aucun prétexte.
- Dupliquer un écran, une règle métier, un calcul de montant.
- Monter une marche sans avoir nommé la capacité qui la justifie.
- Présenter une réécriture native comme un portage : ce sont deux
  choses, et les confondre fait sous-estimer le coût.
- Refuser une réécriture que l'utilisateur a décidée. On l'accompagne,
  après avoir écrit ce qui existera en double.
- Laisser une règle d'argent exister en deux exemplaires. C'est la
  seule ligne qui ne se négocie pas.
- Porter tant qu'une TASK `local` est ouverte.
- Corriger dans le port ce qui se corrige dans le CSS du web.
- Conclure sans avoir vu tourner sur un appareil réel.
