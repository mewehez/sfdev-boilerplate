# Couche rigueur — DÉSACTIVÉE par défaut

Ce fichier n'est chargé par personne. Il ne s'applique que si tu l'actives
explicitement. Tant qu'il dort, le projet tourne en `exploration` :
aucun blocage, nulle part.

Pourquoi il existe : construire par intuition est légitime tant que
personne d'autre ne paie l'erreur. Le jour où une piste se confirme et
où de l'argent, du réglementaire ou la confiance de quelqu'un entrent en
jeu, l'intuition ne suffit plus. Ce jour-là, on active.

---

## Comment activer

Une seule ligne, dans le corps de `product/decisions/ADR-002-regime-preuve.md` :

    regime: traces

ou `regime: terrain`, ou `regime: auto-usage`.

Le hook `graph_index.py` lit cette ligne. Elle suffit — rien d'autre à
câbler. Écris dans le même ADR **pourquoi** tu actives, et **ce que ça
coûte de te tromper** : c'est cette phrase qu'on relit pour désactiver.

Pour revenir en arrière : `regime: exploration`, ou supprime la ligne.

---

## Ce que chaque régime réactive

### `auto-usage`
- Tu es l'utilisateur. La preuve est ton usage documenté (`product/JOURNAL.md`).
- Le hook refuse tout `.claude/agents/*-persona.md` : tu n'as pas besoin
  d'un persona pour te simuler toi-même.

### `traces`
- La preuve est un `TRC` : une observation publique, sourcée, datée.
- Les personas sont reconstruits à partir des TRC, jamais imaginés.
- Deux traces de même `type` ET même domaine comptent pour une source.
- Le hook signale :
  - un BRIEF `ready` sans TRC/INT/DOM dans sa chaîne
  - un BRIEF `ready` adossé à une seule source distincte
  - une concentration > 60 % sur un même domaine
  - un seul `type` de trace toutes traces confondues
  - les TRC de plus de 6 mois

Collecte, par ordre de valeur : avis négatifs de concurrents > support et
FAQ > forums et groupes > offres d'emploi > presse. Chercher des traces,
pas des articles de synthèse.

Structure d'un TRC :

    ## Observé      — ce qui est là, verbatim
    ## Déduit       — ce que j'en tire, séparé, jamais fondu dans l'observé
    ## Limites      — ce que cet échantillon ne dit pas

### `terrain`
- Un `INT` avec `humain: oui` est obligatoire avant tout BRIEF `ready`.
- `domain-expert` refuse de répondre sur ce que *veulent* ou *vivent* les
  gens tant qu'il n'y a aucune interview ; il ne répond que sur les faits
  vérifiables (réglementation, acteurs, contraintes techniques).
- `spec-compiler` refuse de compiler une SPEC dont la chaîne n'a pas
  d'INT humaine.
- `humain: oui` n'est jamais falsifiable. Une session de persona est
  `humain: non`, sans exception ni raccourci.

---

## Le grill d'ouverture, version validation

`project-grill` ne pose ses questions de validation (ÉTAPE 2) que si le
régime n'est pas `exploration`. Les questions, dans l'ordre :

1. Pourquoi ce problème mérite d'être résolu ? Que coûte-t-il aujourd'hui ?
2. Qui le vit exactement ? (rôle, contexte, volume — pas une démographie)
3. Que font-ils aujourd'hui à la place ?
4. Qui résout déjà ça ? Pourquoi te choisirait-on ? Exiger un mécanisme,
   refuser « je ferai mieux ».
5. Quelle contrainte externe tue le projet si elle bouge ?
6. Qui paie, combien, contre quoi ?
7. Combien de personnes concernées as-tu interrogées ? (chiffre)

Verdict : `GO | GO_ÉTROIT | TERRAIN_D'ABORD | NO-GO`, avec
`## ! Ce qui ne tient pas` et `## [SUPPOSÉ] à valider` (minimum 3).

- interviews = 0 → `TERRAIN_D'ABORD` par défaut
- un acteur en place fait déjà exactement ça, sans différenciateur
  mécanique → `NO-GO`

Passer outre est permis : écrire `ADR-000` avec le verdict et les
objections **intactes**, plus la raison de l'utilisateur. Ne jamais
réécrire un verdict pour le rendre compatible avec la décision prise.

---

## Ce qui reste actif en `exploration`, et pourquoi

Ces règles-là ne dépendent pas de la preuve, elles dépendent de l'ordre.
Elles restent, régime ou pas :

- une TASK `dur` ne s'ouvre pas tant qu'une TASK `local` est ouverte
  (`phase_guard.py`, refus dur)
- un écran ne s'écrit pas sans `product/assets/DESIGN.md`
  (`phase_guard.py`, refus dur)
- un ID archivé n'est jamais réattribué
- un BRIEF `ready` est immuable
