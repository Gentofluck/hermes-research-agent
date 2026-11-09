#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
[ -f .env ] && set -a && . ./.env && set +a
DATA="${HERMES_DATA:-./data}"
FORCE="${1:-}"
mkdir -p "$DATA/memories" "$DATA/skills" "$DATA/scripts"
for f in USER.md MEMORY.md; do
  if [ -e "$DATA/memories/$f" ] && [ "$FORCE" != "--force" ]; then
    echo "пропущен $f (уже есть; --force чтобы перезаписать)"
  else
    cp "seed/memories/$f" "$DATA/memories/$f" && echo "скопирован $f"
  fi
done
cp seed/scripts/*.py "$DATA/scripts/"
cp -R seed/skills/. "$DATA/skills/" && echo "навыки скопированы: $(cd seed/skills && find . -name SKILL.md | tr '\n' ' ')"
echo "Перезапустите агента: docker compose restart"
