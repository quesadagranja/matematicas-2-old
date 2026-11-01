"""Superficie de f(x,y)=(3x-5y)/(y-x²) y cilindro singular.

Requisitos: numpy, matplotlib.
Guarda un PNG y un SVG junto al script, y abre la figura.
"""
from pathlib import Path
from io import BytesIO

from PIL import Image
from matplotlib.transforms import Bbox

import matplotlib.pyplot as plt
import numpy as np

# ------------------ Parámetros para las diapositivas ------------------
X_LIM = (-2.0, 2.0)
Y_LIM = (-1.5, 4.2)
Z_LIM = (-6.0, 6.0)  # Zoom vertical en torno a 0; probar (-4, 4)
EPS = 0.06  # Banda visual oculta alrededor de y = x² (no es el dominio excluido)
ELEV, AZIM = 25, -65  # Orientación de la cámara
ALPHA_SUPERFICIE = 1.0  # Superficie azul totalmente opaca
ALPHA_CILINDRO = 0.18  # Solo el cilindro rojo es transparente
MOSTRAR = True  # False si solo quieres guardar imágenes

# ------------------ Superficie de la función ------------------
x = np.linspace(*X_LIM, 360)
y = np.linspace(*Y_LIM, 420)
X, Y = np.meshgrid(x, y)
D = Y - X**2

with np.errstate(divide="ignore", invalid="ignore"):
    Z = (3 * X - 5 * Y) / D

# Recorte *visual*: no altera el dominio matemático de la función.
fuera_rango = (Z < Z_LIM[0]) | (Z > Z_LIM[1])
Z_arriba = np.ma.masked_where((D <= EPS) | fuera_rango, Z)
Z_abajo = np.ma.masked_where((D >= -EPS) | fuera_rango, Z)

fig = plt.figure(figsize=(11.5, 7.0), dpi=180)
ax = fig.add_subplot(111, projection="3d", computed_zorder=False)

for Zi in (Z_arriba, Z_abajo):
    ax.plot_surface(
        X, Y, Zi,
        color="#3D83B7", alpha=ALPHA_SUPERFICIE,
        rcount=170, ccount=170,
        linewidth=0, edgecolor="none", antialiased=True,
        zorder=2,
    )

# ------------------ Cilindro parabólico vertical ------------------
# Parametrización: (x,y,z) = (u,u²,v).
max_u = min(max(abs(X_LIM[0]), abs(X_LIM[1])), np.sqrt(Y_LIM[1]))
u = np.linspace(-max_u, max_u, 170)
v = np.linspace(*Z_LIM, 28)
U, V = np.meshgrid(u, v)
ax.plot_surface(
    U, U**2, V,
    color="#E34B4B", alpha=ALPHA_CILINDRO,
    rstride=1, cstride=1,
    linewidth=0, shade=False, zorder=3,
)

# ------------------ Formato de la figura ------------------
ax.set_xlim(*X_LIM)
ax.set_ylim(*Y_LIM)
ax.set_zlim(*Z_LIM)
ax.set_xlabel(r"$x$", fontsize=16, labelpad=7)
ax.set_ylabel(r"$y$", fontsize=16, labelpad=7)
ax.set_zlabel(r"$z$", fontsize=16, labelpad=4)
ax.tick_params(axis="both", labelsize=10, pad=1)
ax.set_zticks([-6, -3, 0, 3, 6])
ax.view_init(elev=ELEV, azim=AZIM)

# Es fundamental: proporciones visuales, NO las longitudes numéricas de los ejes.
# Evita que el eje z se vea excesivamente estirado.
ax.set_box_aspect((1.25, 1.15, 0.66), zoom=0.84)
ax.grid(True, alpha=0.2)
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

# ------------------ Exportación SIN márgenes blancos ------------------
# bbox_inches="tight" no siempre elimina el gran espacio vacío que dejan
# los ejes 3D. Se mide el contenido dibujado y se recorta con precisión.
out = Path(__file__).resolve().parent
nombre = "t01_parabola_domain_sin_margenes"
dpi = 250

buf = BytesIO()
fig.savefig(buf, format="png", dpi=dpi, facecolor="white")
buf.seek(0)
im = Image.open(buf).convert("RGB")

# Detectamos todo píxel no blanco: incluye ejes, números y etiquetas.
pixeles = np.asarray(im)
contenido = np.any(pixeles < 250, axis=2)
filas, columnas = np.where(contenido)
if filas.size == 0:
    raise RuntimeError("La figura está vacía")

# Sin padding adicional: se eliminan los márgenes por los cuatro lados.
x0, x1 = int(columnas.min()), int(columnas.max()) + 1
y0, y1 = int(filas.min()), int(filas.max()) + 1
im.crop((x0, y0, x1, y1)).save(out / f"{nombre}.png")

# SVG recortado en las mismas coordenadas físicas que el PNG.
ancho, alto = im.size
recorte_vectorial = Bbox.from_extents(
    x0 / dpi,
    (alto - y1) / dpi,
    x1 / dpi,
    (alto - y0) / dpi,
)
fig.savefig(
    out / f"{nombre}.svg",
    bbox_inches=recorte_vectorial,
    pad_inches=0,
    facecolor="white",
)

if MOSTRAR:
    plt.show()
