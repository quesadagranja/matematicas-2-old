# Matemáticas 2 — apuntes

Repositorio para la renovación de los apuntes de Matemáticas 2 en LaTeX/Beamer, conservando el material anterior como referencia.

## Organización

- `main.tex`: documento principal de la **nueva versión**. Actualmente carga `new_version/tema01.tex`.
- `config_moderno.tex` y `contexto_estilos.tex`: preámbulo y estilos de los nuevos apuntes.
- `new_version/`: temas que se van renovando, con nombres `tema01.tex`, `tema02.tex`, etc.
- `original_version/`: los 11 temas de la versión original (`tema01.tex` a `tema11.tex`), sus notas, la configuración antigua y un `main.tex` independiente.
- `original_version/pdf/`: los 11 PDF originales, conservados como referencia y con numeración de dos dígitos.
- `pruebas/`: pilotos y borradores del tema 1. **No** forman parte del temario definitivo.
- `imagenes/`: imágenes compartidas por las dos versiones; los subdirectorios conservan por ahora sus nombres originales (`tema1`, ..., `tema11`) para no romper las referencias de LaTeX.
- `build/`: archivos generados por LaTeX; Git ignora su contenido, salvo `.gitkeep`.
- `.vscode/settings.json`: define una receta explícita de LaTeX Workshop que llama a `latexmk -outdir=%OUTDIR%` y deja los resultados en `build/`.
- `.latexmkrc`: establece `build/` como directorio de salida por defecto para `latexmk`, incluso si se invoca desde la terminal sin `-outdir`.

## Compilar la nueva versión

Desde la **raíz del repositorio**:

```bash
latexmk -pdf main.tex
```

Para compilar solo el tema 1 nuevo:

```bash
latexmk -pdf -outdir=build new_version/tema01.tex
```

El PDF generado se encuentra en `build/main.pdf`. La configuración de `latexmk` está en `.latexmkrc`; también se puede indicar `-outdir=build` explícitamente.

En **VS Code**, abre **la carpeta completa del repositorio** (no solo `main.tex`) y usa **LaTeX Workshop: Build LaTeX project**, con la receta `latexmk (build)` incluida en `.vscode/settings.json`. Si ejecutas `pdflatex main.tex` directamente, **no se aplica** ni `.latexmkrc` ni la receta de VS Code. En ese caso usa `pdflatex -output-directory=build main.tex` (con compilaciones adicionales si son necesarias).

Si ya se generó `main.pdf` en la raíz durante una compilación anterior, permanecerá allí hasta que lo borres manualmente; ninguna configuración lo mueve o elimina. Los archivos temporales nuevos **no** se suben a Git.

## Compilar la versión original

Desde la raíz:

```bash
latexmk -pdf -outdir=build/original original_version/main.tex
```

Para compilar de forma independiente, por ejemplo, el tema 10 original:

```bash
latexmk -pdf -outdir=build/original original_version/tema10.tex
```

`original_version/main.tex` usa `original_version/config.tex`. Los PDF históricos ya guardados en `original_version/pdf/` no se sobrescriben al compilar.

## Añadir un tema nuevo

Crear `new_version/tema02.tex` (o el siguiente número) y activar la correspondiente línea `\\subfile{new_version/tema02.tex}` de `main.tex`. Mantener la estructura de `subfiles` y compilar desde la raíz para que se encuentren correctamente las imágenes.

## Dependencias

Distribución LaTeX con Beamer, `subfiles`, `babel` (español), Latin Modern, paquetes AMS, `bm`, `array`, TikZ y `tcolorbox` (para la nueva plantilla).
