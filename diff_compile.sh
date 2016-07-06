#!/bin/sh
latexdiff --flatten /home/mark/repos/thesis_asSubmitted/thesis.tex /home/mark/repos/thesis/thesis.tex > /home/mark/repos/thesis/diff.tex && pdflatex -interaction nonstopmode /home/mark/repos/thesis/diff.tex

