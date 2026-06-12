#!/bin/bash
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode trabajo_investigacion.tex
pdflatex -interaction=nonstopmode trabajo_investigacion.tex
echo "✓ PDF generado: trabajo_investigacion.pdf"
