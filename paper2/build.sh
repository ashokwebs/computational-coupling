#!/usr/bin/env bash
# Build paper2. Usage: ./build.sh   (from the paper2/ directory)
# Requires: texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended
set -euo pipefail
cd "$(dirname "$0")"

pdflatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null
bibtex main > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null

echo "built: $(pwd)/main.pdf"
echo "  pages:     $(pdfinfo main.pdf | awk '/^Pages/{print $2}')"
echo "  overfull:  $(grep -c 'Overfull' main.log || true)"
echo "  undefined: $(grep -cE 'LaTeX Warning: (Citation|Reference).*undefined' main.log || true)"

# Font-shape warnings from the hyphenat package are expected and cosmetic.
