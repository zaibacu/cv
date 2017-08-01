COMPILER=pdflatex

__PHONY__: build

build:
	$(COMPILER) main.tex

clean:
