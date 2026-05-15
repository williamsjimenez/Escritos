#!/usr/bin/env bash
set -euo pipefail

if ! command -v python3 >/dev/null 2>&1; then
  echo "❌ No se encontró python3 instalado en este sistema."
  exit 1
fi

echo "Iniciando servidor web..."
echo "Abre en tu navegador: http://127.0.0.1:8000"
HOST=0.0.0.0 PORT=8000 python3 app.py
