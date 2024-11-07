#!/bin/bash

python3 -m venv .venv

source ".venv/bin/activate"
# .\.venv\Scripts\activate  # windows

pip install wheel ruff

python3 setup.py sdist
target=$(ls -t dist/rangeutils-*.tar.gz | head -1)
pip install "$target"

deactivate


# poetry env use python3
# poetry config --list
# poetry config virtualenvs.in-project true
