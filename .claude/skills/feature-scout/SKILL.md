---
name: feature-scout
description: Propose des features quand l'utilisateur est à court d'idées.
  Déclencher sur "des idées de features ?", "qu'est-ce qu'on ajoute", "je
  ne sais pas quoi faire ensuite", "propose-moi quelque chose", "qu'est-ce
  qui manque". Trois propositions maximum, tirées du produit réel.
---

# Éclaireur de features

Le piège de « propose-moi des features » est connu : on obtient une liste
de généralités qui iraient à n'importe quel produit — notifications,
tableau de bord, mode sombre, export CSV. Elles ne coûtent rien à écrire
et ne valent rien à lire.

Une bonne proposition vient **du produit lui-même** : d'un fait de
domaine qu'on a collecté, d'un trou dans le parcours, d'une conséquence
que le produit signale sans la traiter. Elle est vérifiable, pas
imaginée.

---

## AVANT de proposer quoi que ce soit — lire

Sans cette lecture, tu proposeras ce qui existe déjà. C'est la seule
façon de rater complètement.

1. `product/INDEX.md` — la file de grill : ce qui est **déjà capturé**
   n'est pas une proposition. On le rappelle, on ne le réinvente pas.
2. `backlog/tasks/` — ce qui est `done`. Ne jamais proposer ça.
3. `product/decisions/` — tout ADR. Ce qui est **explicitement exclu**
   ne se propose pas sans dire quel ADR il faudrait lever.
4. `product/domain/` — les DOM et TRC. C'est le gisement principal.
5. `src/` — ce qui tourne vraiment. Les écrans, le parcours réel.

---

## Les sept lentilles

Passer le produit sous chacune. La plupart ne donneront rien : c'est
normal, on cherche les deux ou trois qui mordent.

### 1. Le trou dans le parcours
Dérouler le parcours principal, étape par étape. Où l'utilisateur doit-il
**sortir du produit** pour finir ce qu'il a commencé ? Où reste-t-il
sans réponse ?

### 2. La conséquence non traitée
Le produit **signale** quelque chose et n'offre aucun geste pour le
traiter. Un écran qui dit « à rembourser » sans bouton de remboursement.
Un avertissement sans action. C'est la lentille la plus productive :
le produit a déjà fait le travail de détection.

### 3. Le fait de domaine non exploité
Relire les DOM un par un. Chacun affirme quelque chose de vrai sur le
métier. Lequel n'est utilisé par **aucune** feature ? Un chiffre sourcé
qui ne sert à rien est souvent une feature qui attend.

### 4. Ce que fait le voisin
Chercher en ligne 2 ou 3 produits réels du même domaine. Ce qu'ils ont et
qu'on n'a pas. Pour chacun : est-ce que ça compte **ici**, dans ce
contexte d'usage précis ? Beaucoup de leurs features ne comptent pas —
le dire est aussi utile que le contraire.

### 5. Le deuxième usage
Qui d'autre touche ce produit, occasionnellement ? Un employé, un
associé, un comptable, un proche. Ce qu'il fait aujourd'hui à la place.

### 6. Ce qui casse à l'échelle
Multiplier le volume par cent. Quel écran devient inutilisable ? Quelle
liste sans recherche devient un mur ? Ce n'est une feature que si le
volume est plausible — sinon c'est de l'anticipation.

### 7. La file de grill
Les IDEA `raw` et `parked` déjà là. Certaines redeviennent pertinentes
parce que le produit a changé depuis leur capture. Le dire, avec ce qui
a changé.

---

## Séparer une feature d'un défaut
Si une lentille révèle que le produit **fait faux** — un libellé qui ment,
un calcul erroné, un cas non géré — ce n'est PAS une proposition de
feature. Le sortir à part, avant les propositions, en une ligne :

`! Défaut — <ce qui est faux>, dans <fichier:ligne>.`

Ne jamais déguiser un correctif en nouveauté.

---

## Sortie — trois propositions, JAMAIS plus

Trois est un maximum, pas une cible. Deux bonnes valent mieux que trois
dont une remplit. L'attention est la ressource rare ; une liste de dix
propositions se lit comme une liste de zéro.

    ! Défaut repéré — <une ligne, ou rien>

    ## A — <la feature en ≤ 10 mots, dans les mots de l'utilisateur>
    - D'où ça vient : <lentille> — <la source précise : DOM-nnn,
      écran, fichier:ligne>
    - Ce que ça change pour lui : <une phrase, côté utilisateur>
    - ! Ce que ça coûte : <structurellement — pas en jours>
    - Ce que ça déclasse : <ce qui passe après>
    - ? La question qui décide : <une seule>

    ## B — ...
    ## C — ...

    ## Déjà dans la file
    - [[IDEA-nnn]] <titre> — <pourquoi c'est redevenu pertinent, ou rien>

    → Tu en retiens laquelle ? Je capture les autres en IDEA.

## Après le choix
- Écrire **chaque** proposition non retenue en `IDEA-nnn` `status: raw`,
  `origine: agent`, `contexte: feature-scout`. Capturer à tort coûte
  trois lignes ; perdre une idée coûte de la retrouver.
- La retenue part directement en `feature-build` si la phase est `local`.
  Ne pas passer par un grill : l'utilisateur vient de choisir.

---

## Interdits
- Proposer plus de trois choses. Jamais.
- Enchaîner une deuxième salve sans qu'on la demande.
- Proposer ce qui est déjà `done`, déjà dans la file de grill, ou
  explicitement exclu par un ADR — sauf en nommant l'ADR à lever.
- Proposer une feature générique qui irait à n'importe quel produit.
  Test : si la proposition tient sans changer un mot pour un autre
  projet, elle ne vaut rien. La jeter.
- Recommander. Tu proposes, il choisit. S'il demande ton avis : donner
  le critère qui départage, pas la réponse.
- Estimer en jours, en points, en semaines.
- Déguiser un correctif en feature.
- Proposer sans avoir lu `src/`. C'est ce qui produit les doublons.
