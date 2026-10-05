# Revisión del tema 10

Se conservan las 49 diapositivas, sus ejemplos, el orden de los cálculos y las gráficas originales. Las fórmulas, sistemas y tablas son editables en LaTeX. Las tablas sucesivas tienen celdas y posiciones fijas, incluidas las de Hermite con nodos repetidos.

Correcciones y precisiones:

- La función de los ejemplos es (x/2)^(x-2), como en el tema 9. Se conserva su derivada f(x)((x-2)/x+ln(x/2)).
- Hermite tiene grado como máximo 2n+1; el grado efectivo no tiene que ser impar.
- La base de Hermite usa L'_(n,i)(x_i), evaluada en el nodo, y la segunda base multiplica (x-x_i) por el cuadrado de L_(n,i).
- En las diferencias divididas se duplica cada nodo y se asigna su derivada a la diferencia de nodos iguales. Se han normalizado los índices y corregido etiquetas.
- Los cálculos de Hermite se hacen sin redondeos intermedios. La tabla muestra cuatro decimales y las expresiones de los polinomios muestran seis. En x=3: H3=0.607821, H4=1.654898 y H5=1.309795 (aproximadamente).
- Los polinomios intermedios de grado par satisfacen solo las condiciones de interpolación incluidas hasta ese punto de la tabla.
- La condición de interpolación del spline es S(x_i)=f(x_i); las condiciones de enlace usan S_i y S_(i+1) en x_(i+1).
- Los coeficientes del spline se han calculado con aritmética racional. En el último tramo del ejemplo con cinco nodos, el coeficiente cuadrático correcto es 447/64, no 445/64, y el término cúbico usa (x-4)^3, no (x-2)^3.

Verificación matemática: H5 reproduce los valores y derivadas en 1, 4 y 2. Ambos ejemplos de spline interpolan todos los nodos, tienen primera y segunda derivadas continuas en cada enlace, y segunda derivada nula en los extremos.

Compilar desde la raíz del repositorio:

    pdflatex -output-directory=pdf temas/tema10.tex
    pdflatex -output-directory=pdf temas/tema10.tex

El tema utiliza array y tikz, además de config.tex.
