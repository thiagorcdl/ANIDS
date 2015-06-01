all: tg.pdf

clean:
	rm -f *.aux *.bll *.bak *.blg *.log *.blg *.toc *.lot *.lof \
	  *.idx *.lg *.ind *.pdf *.bbl

tg.pdf: tg.tex introducao.tex bib.bib ufpr.cls resumo.tex conclusao.tex
	pdflatex tg.tex
	bibtex tg
	iconv -f iso88591 -t utf8 tg.bbl > .tmp.bbl
	mv .tmp.bbl tg.bbl
	pdflatex tg.tex
	pdflatex tg.tex

.PHONY: all clean
