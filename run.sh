#!/usr/bin/env bash
set -euo pipefail

if ! command -v python3 >/dev/null 2>&1; then
  echo "❌ No se encontró python3 instalado en este sistema."
  exit 1
fi

python3 app.py
