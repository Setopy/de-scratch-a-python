# De Scratch a Python

**🌐 Sitio web: <https://setopy.github.io/JesusArrows-de-scratch-a-python/>** (se puede instalar como app)

[![Abrir el cuaderno en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Setopy/JesusArrows-de-scratch-a-python/blob/main/Mis%20aventuras%20con%20Python.ipynb)

Un libro de trabajo para un niño o niña de 9 años que ya sabe usar [Scratch](https://scratch.mit.edu) y está listo para Python de verdad. Cada categoría de bloques de Scratch 3.0 aparece junto a su Python, listo para ejecutar en **Google Colab**, con la tortuga en el lugar del escenario de Scratch. No hay que instalar nada: basta con un navegador y una cuenta de Google.

Es la edición en español (de México, con los nombres oficiales de los bloques de Scratch en español latinoamericano) de [*From Scratch to Python*](https://github.com/Setopy/JesusArrows-scratch2python).

> Ya sabes programar. Cada vez que encajas bloques de Scratch, estás escribiendo un programa. Python usa las mismas ideas: solo escribes las palabras en lugar de arrastrar bloques.

| | |
|---|---|
| 📘 **El libro** | [`de-scratch-a-python.pdf`](de-scratch-a-python.pdf): 277 páginas, 35 misiones, respuestas al final |
| 🐢 **El cuaderno** | [`Mis aventuras con Python.ipynb`](Mis%20aventuras%20con%20Python.ipynb): el código de cada misión, con una celda vacía para escribir |

## Para los adultos: cómo empezar

1. **Imprime o abre el PDF.** Lee primero *Para los adultos*, cerca del final (unos 10 minutos).
2. **Abre el cuaderno en Colab** con el botón de arriba y elige *Archivo → Guardar una copia en Drive* para que se guarde el trabajo.
3. **Ejecuta la celda «En el principio»** (`!pip install ColabTurtlePlus`) cada vez que abras el cuaderno.
4. **Haz una misión por sesión** (20 a 30 minutos). Cada misión tiene cinco pasos: constrúyelo en Scratch, escríbelo en Colab, léelo línea por línea, ejecútalo y hazlo tuyo.

Las palabras de Python (`for`, `print`, `forward`...) y los nombres de los colores (`"red"`, `"gold"`) siempre van en inglés. Los nombres que el niño inventa van en español, sin acentos ni ñ para que sea fácil escribirlos: `puntos`, `respuesta`, `cuadrado(lado)`. Los mensajes de error de Python también salen en inglés; el libro explica cada uno en español.

## Así es una misión

| Scratch | Python |
|---|---|
| al presionar bandera verde | *(presiona el botón ▶)* |
| repetir 4 | `for i in range(4):` |
| mover 100 pasos | `    forward(100)` |
| girar ↻ 90 grados | `    right(90)` |

```python
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))   # el mismo escenario de 480 x 360 que Scratch

for i in range(4):
    forward(100)
    right(90)
```

## Qué hay en el libro

| Sección | Bloques de Scratch | Python que enseña | Misiones |
|---|---|---|---|
| Páginas iniciales | | Conoce Colab, palabras de Scratch y de Python, cuatro hábitos nuevos | |
| **Parte 1: Movimiento y Lápiz** | Movimiento, Lápiz | `forward`, `right`, `goto`, `setheading`, `pencolor`, `stamp` | 3 |
| **Parte 2: Bucles** | Control (bucles) | `for i in range()`, `while True`, bucles anidados, `time.sleep` | 4 |
| **Parte 3: Variables y listas** | Variables, Listas | `=`, `+=`, listas, `append`, contar desde 0 | 4 |
| **Parte 4: Operadores** | Operadores | cuentas, `random.randint`, `==`, unir texto, `%`, `round` | 4 |
| **Parte 5: Sensores y decisiones** | Sensores, Control (si) | `input()`, `int()`, `if`/`elif`/`else`, `while`, cronómetros | 4 |
| **Parte 6: Mis Bloques** | Mis Bloques, clones | `def`, entradas, `return`, más objetos con `Turtle()` | 4 |
| **Parte 7: Apariencia, sonido y eventos** | Apariencia, Sonido, Eventos | disfraces, música con `pitido()`, mensajes como funciones | 4 |
| **Grandes proyectos** | todos | ocho juegos, de *Anima tu nombre* a *Juego de persecución* | 8 |
| **El Zoológico de Bichos** | | leer errores, 12 bichos comunes, 10 cazas de bichos | |
| **Diccionario de bloques** | los 147 bloques | el Python de cada bloque de Scratch, más una hoja de ayuda | |
| **Para los adultos** | | cómo llevar una sesión, ritmo sugerido, consejos de Colab, Thonny | |

## La app

El sitio web se puede instalar en una computadora, tableta o celular (botón **Instalar la app** en Chrome o Edge; en iPhone o iPad, *Compartir → Agregar a inicio*). La app guarda la página y el PDF en el dispositivo, así que el libro se puede leer sin internet. Programar en Colab sí necesita conexión.

## Cómo está organizado

```
de-scratch-a-python.tex          archivo principal: \input del preámbulo y de cada capítulo
de-scratch-a-python.pdf          el libro compilado
preamble.tex                     el aspecto compartido (cajas, colores, código, misiones)
Mis aventuras con Python.ipynb   el cuaderno de Colab (se genera a partir de los capítulos)
index.html, manifest.webmanifest, sw.js, icons/   el sitio web instalable
chapters/
  00-front.tex ... 11-grown-ups.tex   un archivo por parte, más NN-*-answers.tex
  NN-colab-tests.py                   los programas de cada capítulo, para probarlos
  ES-STYLE.md                         guía de traducción y glosario
  _make_mission_chart.py              reconstruye 00-mission-chart.tex
  _make_notebook.py                   reconstruye el cuaderno
  _run_tests.py                       prueba los programas con ColabTurtlePlus
  _harness.tex, _test-NN.tex          compilan un capítulo solo
```

## Compilar y probar

Compila el PDF con [Tectonic](https://tectonic-typesetting.github.io):

```bash
tectonic de-scratch-a-python.tex
```

Después de editar un capítulo, reconstruye la tabla de misiones y el cuaderno:

```bash
python3 chapters/_make_mission_chart.py
```

```bash
python3 chapters/_make_notebook.py
```

Prueba los programas de todos los capítulos con la biblioteca real, dentro de un entorno virtual que tenga `ColabTurtlePlus`, `numpy` e `ipython`:

```bash
python -I chapters/_run_tests.py chapters/*-colab-tests.py
```

Última prueba (13 nov 2026): 92 pasan, 0 fallan, 2 se omiten (uno corre para siempre a propósito y otro necesita un archivo local).

Si cambias el PDF o la página, sube el número de `VERSION` en `sw.js` para que las apps instaladas se actualicen.

## Créditos

- [ColabTurtlePlus](https://github.com/mathriddle/ColabTurtlePlus) de Larry Riddle, basado en [ColabTurtle](https://github.com/tolgaatam/ColabTurtle) de Tolga Atam
- Los dibujos de bloques de Scratch se hacen con el paquete de LaTeX [`scratch3`](https://ctan.org/pkg/scratch3)
- Los nombres de los bloques en español son los de la traducción oficial de Scratch (español de Latinoamérica)

Este es un libro independiente. No lo hacen Scratch, la Fundación Scratch, el MIT ni Google, ni tiene relación con ellos. Scratch es un proyecto de la Fundación Scratch.
