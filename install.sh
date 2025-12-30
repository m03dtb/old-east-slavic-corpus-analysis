#!/usr/bin/env bash
set -e

python3 -m venv venv
source venv/bin/activate

if [[ "$VIRTUAL_ENV" == "$(pwd)/venv" ]]; then
  python -m pip install --upgrade pip
  python -m pip install ipykernel
  python -m pip install -r requirements.txt

  python -m ipykernel install --user \
    --name OES \
    --display-name "Python (OES)"
else
  echo "Error: virtual environment not activated correctly"
  exit 1
fi

echo "Setup complete."
echo "Activate with: source venv/bin/activate"
