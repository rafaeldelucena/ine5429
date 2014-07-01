PROJECT=relatorio
all:
	bibtex $(PROJECT)
	latex $(PROJECT)
	pdflatex $(PROJECT).tex

clean:
	rm -f $(PROJECT).pdf $(PROJECT).bbl

run:
	evince $(PROJECT).pdf &
