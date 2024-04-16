#/bin/bash
conda activate python3.10
cp src/CNAME _build/html/
jupyter-book build .
ghp-import -n -p -f _build/html
