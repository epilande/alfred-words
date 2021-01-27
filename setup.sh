#!/usr/bin/env bash

source="$(pwd)/src/*"

if [[ -z "$1" ]]; then
  # Open Alfred workflow in terminal and run `pwd | pbcopy`.
  # Then run `./setup.sh <ALFRED_WORKFLOW_PATH>`.
  echo "Argument missing: Alfred workflow directory must be supplied."
  exit 1
fi

echo "📦 Installing python3 modules..."

/usr/bin/python3 -m pip install --target ./src/lib --requirement requirements.txt

echo "🔗 Symlinking $source to $1"

ln -s ${source} $1
