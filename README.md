About
======
A project which is basically CV generator for myself.

Generating newest version
==========================


Prerequisites
--------------
It is based on [LaTeX](https://www.latex-project.org/), thus relevant packages are required.
Currently it expects to find `pdflatex` compiler.

GNUMake - compile process uses a little bit of [GNUMake](https://www.gnu.org/software/make/), thus this tool is required as well

Actual generation
------------------
`make` command should do everything for you, output is `main.pdf` file.

Latest Version
===============
It is expected to be found in [Releases](https://github.com/zaibacu/cv/releases) section

Using as a template for your own CV
===================================
Yes you can. I'm putting it inside Github.com mostly due to own comfort.
However most parts are done having flexibility in mind.
- `variaables.tex` - here you setup basic facts about you
- `sections/expierence.tex` - work expierence blocks goes here
- `sections/education.tex` - education blocks goes here
- `sections/volunteering.tex` - volunteering stuff goes here
- `sections/projects.tex` - short info about projects goes here
- `sections/skills.tex` - simple skill table
- `sections/languages.tex` - simple language table

Most of the sections can be removed via `main.tex`.
Pictures goes into `media/` folder
