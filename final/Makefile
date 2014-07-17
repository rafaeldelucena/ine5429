PROJECT=relatorio
all:
	bibtex $(PROJECT)
	latex $(PROJECT)
	pdflatex $(PROJECT).tex

clean:
	rm -f $(PROJECT).pdf $(PROJECT).bbl

run:
	evince $(PROJECT).pdf &

minning:
	./poclbm.py  stratum://18firgLYHgebHbEyudWC8t1DVaxUAasx9o:@stratum.mining.eligius.st:3334
