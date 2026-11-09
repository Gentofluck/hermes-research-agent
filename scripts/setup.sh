#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
[ -f .env ] && set -a && . ./.env && set +a
DATA="${HERMES_DATA:-./data}"
mkdir -p "$DATA/workspace"
if [ ! -f "$DATA/config.yaml" ]; then
  cp seed/config.yaml "$DATA/config.yaml"
fi
docker compose run --rm hermes-agent setup
