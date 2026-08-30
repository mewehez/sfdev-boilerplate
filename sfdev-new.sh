#!/usr/bin/env bash
# Crée un nouveau projet à partir de sfdev-boilerplate.
# Copie le socle sans son historique git, initialise un dépôt neuf.
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

say()  { printf '%s\n' "$*"; }
ask()  { printf '%s' "$1" >&2; read -r REPLY; printf '%s' "$REPLY"; }
die()  { printf '! %s\n' "$*" >&2; exit 1; }

say ""
say "  sfdev — nouveau projet"
say "  ─────────────────────"
say ""

# ---------------------------------------------------------------- nom
NAME="${1:-}"
while [ -z "$NAME" ]; do
  NAME="$(ask '  Nom du projet (kebab-case) : ')"
done
case "$NAME" in
  *[!a-zA-Z0-9._-]*) die "Nom invalide : lettres, chiffres, . _ - uniquement." ;;
esac

# ------------------------------------------------------------ chemin
DEFAULT_PARENT="$(dirname "$SRC")"
PARENT="$(ask "  Où le créer ? [$DEFAULT_PARENT] : ")"
PARENT="${PARENT:-$DEFAULT_PARENT}"
PARENT="${PARENT/#\~/$HOME}"
[ -d "$PARENT" ] || die "Dossier inexistant : $PARENT"

DEST="$PARENT/$NAME"
[ -e "$DEST" ] && die "Existe déjà : $DEST"

# ------------------------------------------------------------- pitch
say ""
say "  Le produit en une phrase — pour QUI, quel PROBLÈME, à quel MOMENT."
say "  (laisse vide si tu préfères le dire à Claude directement)"
PITCH="$(ask '  > ')"

# -------------------------------------------------------------- copie
say ""
say "  Copie du socle…"
mkdir -p "$DEST"
if command -v rsync >/dev/null 2>&1; then
  rsync -a \
    --exclude '.git' --exclude '.obsidian' --exclude '.DS_Store' \
    --exclude 'AMELIORATIONS.md' --exclude 'product/INDEX.md' \
    "$SRC"/ "$DEST"/
else
  (cd "$SRC" && tar --exclude='./.git' --exclude='./.obsidian' \
      --exclude='.DS_Store' --exclude='./AMELIORATIONS.md' \
      --exclude='./product/INDEX.md' -cf - .) | (cd "$DEST" && tar -xf -)
fi
rm -f "$DEST/sfdev-new.sh"

# Le README du socle décrit le socle, pas le projet. Il est conservé
# comme documentation d'outillage, et la place est laissée au projet.
mkdir -p "$DEST/docs"
mv "$DEST/README.md" "$DEST/docs/LE-SOCLE.md" 2>/dev/null || true
cat > "$DEST/README.md" <<'READMEEOF'
# __NAME__

__PITCH__

> Point de départ. À réécrire quand quelque chose tournera : comment
> lancer, ce que ça fait, ce qui n'existe pas encore.

## Où en est le projet
- `product/INDEX.md` — l'état du graphe, régénéré à chaque session
- `product/grill/` — la vision produit telle qu'elle a été dite
- `backlog/tasks/` — ce qui est fait, ce qui reste

## Travailler dessus

```bash
claude
```

Puis : `nouveau projet` — ou directement une feature.

Le fonctionnement du socle : `docs/LE-SOCLE.md`.
READMEEOF

PLACEHOLDER='<le produit en une phrase : pour QUI, quel PROBLÈME, à quel MOMENT>'
python3 - "$DEST/README.md" "$NAME" "${PITCH:-$PLACEHOLDER}" <<'PYEOF'
import sys, pathlib
p = pathlib.Path(sys.argv[1])
p.write_text(p.read_text().replace("__NAME__", sys.argv[2])
                          .replace("__PITCH__", sys.argv[3]))
PYEOF

chmod +x "$DEST/.claude/hooks/"*.py 2>/dev/null || true

# ------------------------------------------------------- amorce projet
cat > "$DEST/product/grill/$(date +%F)-vision.md" <<EOF
# Vision produit — $NAME

Fichier de travail, hors graphe : pas de frontmatter, pas d'ID.
Rempli par la skill \`project-grill\`, ÉTAPE 1.

## Le produit en une phrase
- ${PITCH:-<à remplir>}

## Features v1
- <à remplir>

## Écran principal — ce qu'on voit en l'ouvrant
- <à remplir>

## Parcours en 5 étapes
1.
2.
3.
4.
5.

## Ce qui n'existera PAS en v1
- <trois exclusions minimum>
EOF

# ---------------------------------------------------------------- git
if command -v git >/dev/null 2>&1; then
  git -C "$DEST" init -q
  git -C "$DEST" add -A
  git -C "$DEST" -c user.email=sfdev@local -c user.name=sfdev \
      commit -qm "socle sfdev — $NAME" || true
  say "  Dépôt git initialisé."
fi

# ------------------------------------------------------------- amorce
say ""
say "  ✓ $DEST"
say ""
say "  Ensuite :"
say ""
say "    cd $DEST"
say "    claude"
say ""
if [ -n "$PITCH" ]; then
  say "  Puis dis-lui :"
  say "    nouveau projet — $PITCH"
else
  say "  Puis dis-lui :  nouveau projet"
fi
say ""
say "  Il te demandera d'abord ce que l'application fait — les features,"
say "  l'écran principal, le parcours. Il construit ensuite, dans la"
say "  même session."
say ""
