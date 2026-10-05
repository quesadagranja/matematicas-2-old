# Matemáticas 2: apuntes originales en Beamer

Conversión del material PPTX original a LaTeX Beamer. Una diapositiva por cada diapositiva original, con texto y fórmulas editables y las ilustraciones originales.

## Compilación

Desde la raíz del repositorio:

```sh
latexmk -pdf -outdir=pdf main.tex
```

`main.tex` utiliza formato **16:9** y permite seleccionar los temas: por defecto está activo el tema 1. Descomenta las líneas `\subfile{temas/temaN.tex}` que quieras incluir. Puedes activar todos los temas para generar la asignatura completa. La portada general es opcional.

Cada tema también se puede compilar de forma independiente, con la misma configuración:

```sh
latexmk -pdf -outdir=pdf temas/tema1.tex
```

Si no utilizas `latexmk`, ejecuta `pdflatex -output-directory=pdf main.tex` dos veces (o sustituye `main.tex` por el tema correspondiente).

Requiere una distribución LaTeX con Beamer, babel (español), Latin Modern, amsmath, amssymb, mathtools, bm, array, TikZ y subfiles.

- `main.tex`: documento principal y selección de temas, en 16:9.
- `config.tex`: plantilla común en tonos azules, con portadas de degradado radial, símbolos matemáticos y cabeceras compactas, basada en la del repositorio `matematicas-2`.
- `temas/`: fuentes de los temas, compilables por separado o desde el documento principal.
- `imagenes/`: ilustraciones extraídas de los originales.
- `pdf/`: versiones compiladas. Los PDF existentes corresponden a la conversión anterior; vuelve a compilarlos para aplicar la nueva plantilla.

Tema 1: 22 diapositivas. Se corrigen erratas de redacción y se precisa que los niveles del ejemplo de la raíz están en [0,10]. En el ejercicio final, el apartado de tres variables se denomina superficie de nivel.
