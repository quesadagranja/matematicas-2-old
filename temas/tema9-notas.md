# Revisión del tema 9

Se conserva la correspondencia de 105 diapositivas, las figuras originales y el desarrollo progresivo de los ejemplos. Las fórmulas y las tablas, incluidas las pirámides de Neville y de diferencias divididas, están escritas en LaTeX. Las celdas se reservan desde el inicio y mantienen su geometría al aparecer resultados o fracciones.

Correcciones matemáticas:

- La función de los ejemplos es (x/2)^(x-2), con exponente, como muestran los valores y las fórmulas del original.
- Taylor: derivada de orden n en el término general; el resto tiende a cero al acercarse al centro para orden fijo. Aumentar el orden no asegura por sí solo convergencia ni disminución monótona del error.
- Existencia y unicidad: grado como máximo n, nodos distintos dos a dos y valores arbitrarios y_i.
- Weierstrass garantiza aproximación uniforme, sin imponer interpolación en nodos prefijados.
- Un polinomio con las raíces indicadas puede incluir un factor constante; las bases de Lagrange tienen grado n y el interpolante puede tener grado menor.
- En la comparación de grados, P_2 tiene un término más que P_1.
- Error absoluto del ejemplo lineal en 5/2: 0.131966, en lugar de 0.148. Se han recalculado los demás errores.
- En las tablas de Lagrange, el tercer nodo es x_2=3 y su valor es f(x_2)=3/2; se corrigen las etiquetas que mezclaban ambos.
- Coeficientes superiores de las tablas triangulares: se leen en el borde superior del triángulo escalonado.
- Último polinomio: el coeficiente de x² es 19/15, no 3/5. La expresión final es -2x³/15+19x²/15-28x/5+8 y se ha comprobado en los cuatro nodos.

Compilación desde la raíz del repositorio:

    pdflatex -output-directory=pdf temas/tema9.tex
    pdflatex -output-directory=pdf temas/tema9.tex

El preámbulo del tema utiliza array y tikz, además de la configuración común.
