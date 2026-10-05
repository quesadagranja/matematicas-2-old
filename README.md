# Matemáticas 2: apuntes originales en Beamer

Conversión del material PPTX original a LaTeX Beamer. Una diapositiva por cada diapositiva original, con texto y fórmulas editables y las ilustraciones originales.

## Compilación

Desde la raíz del repositorio:

```sh
pdflatex -output-directory=pdf temas/tema1.tex
pdflatex -output-directory=pdf temas/tema1.tex
```

Requiere una distribución LaTeX con Beamer, babel (español), amsmath y amssymb.

- `config.tex`: formato común 4:3, fondo blanco y títulos azules.
- `temas/`: fuentes de los temas.
- `imagenes/`: ilustraciones extraídas de los originales.
- `pdf/`: versiones compiladas.

Tema 1: 22 diapositivas. Se corrigen erratas de redacción y se precisa que los niveles del ejemplo de la raíz están en [0,10]. En el ejercicio final, el apartado de tres variables se denomina superficie de nivel.
