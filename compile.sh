pdflatex -draftmode thesis
bibtex thesis # or biber
makeindex thesis.idx # if needed
#makeindex -s style.gls ...# for glossary if needed
pdflatex -draftmode thesis.tex
pdflatex thesis
