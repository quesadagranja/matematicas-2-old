import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# ============================================================
# Configuración
# ============================================================

R = 10.0
N = 500
LEVELS = [2, 4, 6, 8, 9]

OUT_PNG = "curvas_nivel_semiesfera.png"
OUT_SVG = "curvas_nivel_semiesfera.svg"

# Color rojo oscuro, legible en fondo blanco
LEVEL_COLOR = '#8B0000'   # dark red

# ============================================================
# Malla y función
# ============================================================

x = np.linspace(-R, R, N)
y = np.linspace(-R, R, N)
X, Y = np.meshgrid(x, y)

inside = X**2 + Y**2 <= R**2
Z = np.full_like(X, np.nan, dtype=float)
Z[inside] = np.sqrt(R**2 - X[inside]**2 - Y[inside]**2)

# ============================================================
# Figura con dos paneles
# ============================================================

fig = plt.figure(figsize=(8, 10))

# ------------------------------------------------------------
# Panel superior: superficie 3D
# ------------------------------------------------------------
ax1 = fig.add_subplot(2, 1, 1, projection='3d')

ax1.plot_surface(
    X, Y, Z,
    cmap='Blues',
    linewidth=0,
    antialiased=True,
    alpha=0.95
)

theta = np.linspace(0, 2*np.pi, 500)
for k in LEVELS:
    r = np.sqrt(R**2 - k**2)
    xc = r * np.cos(theta)
    yc = r * np.sin(theta)
    zc = np.full_like(theta, k)
    ax1.plot(
        xc, yc, zc,
        color=LEVEL_COLOR,
        linewidth=2.2
    )

ax1.set_xlabel(r'$x$', fontsize=16, labelpad=8)
ax1.set_ylabel(r'$y$', fontsize=16, labelpad=8)
ax1.set_zlabel(r'$z$', fontsize=16, labelpad=8)

ax1.set_xlim(-R, R)
ax1.set_ylim(-R, R)
ax1.set_zlim(0, R)

ax1.view_init(elev=28, azim=-50)

try:
    ax1.set_box_aspect((1, 1, 0.7))
except Exception:
    pass

# ------------------------------------------------------------
# Panel inferior: curvas de nivel
# ------------------------------------------------------------
ax2 = fig.add_subplot(2, 1, 2)

cf = ax2.contourf(
    X, Y, Z,
    levels=30,
    cmap='Blues',
    alpha=0.35
)

cs = ax2.contour(
    X, Y, Z,
    levels=LEVELS,
    colors=LEVEL_COLOR,
    linewidths=2.2
)

ax2.clabel(cs, inline=True, fmt=r'$z=%g$', fontsize=10, colors=LEVEL_COLOR)

# Borde del dominio
ax2.plot(
    R*np.cos(theta), R*np.sin(theta),
    color=LEVEL_COLOR,
    linewidth=2
)

ax2.set_xlabel(r'$x$', fontsize=16)
ax2.set_ylabel(r'$y$', fontsize=16)

ax2.set_aspect('equal', adjustable='box')
ax2.set_xlim(-R - 0.5, R + 0.5)
ax2.set_ylim(-R - 0.5, R + 0.5)
ax2.grid(True, alpha=0.25)

# ============================================================
# Guardado y visualización
# ============================================================

plt.tight_layout()
plt.savefig(OUT_PNG, dpi=300, bbox_inches='tight', pad_inches=0.02)
plt.savefig(OUT_SVG, bbox_inches='tight', pad_inches=0.02)
plt.show()