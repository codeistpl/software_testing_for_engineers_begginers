#!/usr/bin/env bash
set -euo pipefail

# Creates a virtual environment in .venv and installs requirements (if present).
PYTHON=${PYTHON:-python3}

echo "Creating virtual environment at .venv using ${PYTHON}..."
${PYTHON} -m venv .venv
echo "Activating and installing requirements..."
source .venv/bin/activate
python -m pip install --upgrade pip
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
else
  echo "No requirements.txt found; venv created without packages."
fi
echo
echo "Done. Activate with: source .venv/bin/activate"
