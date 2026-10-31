# Notas de revisión del tema 8

Se conservan las 52 diapositivas y las figuras originales. Las tablas progresivas tienen columnas y filas de dimensiones fijas, incluso antes de mostrar los resultados.

- Newton: cálculos sin redondeos intermedios; el residuo final del primer ejemplo no es exactamente cero. El criterio de paso no constituye por sí solo una cota del error.
- Condiciones suficientes de Newton: regularidad C² y signos constantes no nulos de cada derivada, sin exigir que ambas tengan el mismo signo.
- Descenso por gradiente: se distinguen criterio de parada, punto estacionario, mínimo local y mínimo global; no existe un rango universal (0,1) para el paso.
- Hessiana del ejemplo cuadrático: se comprueba positividad definida, no solo el signo del determinante.
- Función peaks: signos corregidos en los exponentes, coherentes con las figuras y con https://www.mathworks.com/help/matlab/ref/peaks.html.
- Ajuste de circunferencia: residuos algebraicos, gradiente sin el factor 1/2 sobrante y actualización simultánea. El ejemplo numérico original no indicaba el radio inicial y sus resultados no concuerdan con la fórmula. Se explicita radio inicial 5, se recalculan tres pasos y se distingue la parada por tolerancia 0.5 (segundo paso) de ejecutar tres actualizaciones.
