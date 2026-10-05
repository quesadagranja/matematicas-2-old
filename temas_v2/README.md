# Temas con progresión didáctica

## Tema 1: funciones de varias variables

63 diapositivas. Conserva los contenidos, ejemplos matemáticos y ejercicios del tema original, con recordatorios de una variable, evaluaciones numéricas, restricciones de dominio, ejemplos graduados y aplicaciones antes de la formalización de los conjuntos de nivel.

Desde la raíz del repositorio:

```sh
mkdir -p pdf_v2
pdflatex -output-directory=pdf_v2 temas_v2/tema1.tex
pdflatex -output-directory=pdf_v2 temas_v2/tema1.tex
```

Se reutiliza `config.tex` y las ilustraciones de `imagenes/tema1/`.

## Imágenes pendientes

El documento compila sin estas imágenes y muestra un recuadro descriptivo. Al añadir los archivos siguientes se incorporan automáticamente, conservando sus proporciones:

- `imagenes/tema1/v2_plano_suma.png`: plano z=x+y con ejes etiquetados y puntos (0,0,0), (1,0,1) y (0,1,1).
- `imagenes/tema1/v2_chip_temperatura.png`: mapa térmico de un procesador con escala en grados Celsius y una línea de igual temperatura. Si los datos son simulados, debe indicarse en la imagen.

No se requiere ninguna imagen decorativa adicional. Los mapas topográficos y las superficies originales ya permiten explicar visualmente los conceptos.
