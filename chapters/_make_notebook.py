"""Reconstruye 'es/Mis aventuras con Python.ipynb' a partir de los capítulos en español
(misiones, código y caza de bichos). Es la versión en español de ../../chapters/_make_notebook.py."""
import re, json, pathlib
es = pathlib.Path(__file__).resolve().parent.parent
ch = es / "chapters"
def md(text): return {"cell_type": "markdown", "metadata": {}, "source": text.strip("\n").splitlines(True)}
def code(text): return {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": text.strip("\n").splitlines(True)}
def clean(t):
    t = re.sub(r"\\texttt\{([^{}]*)\}", r"`\1`", t); t = re.sub(r"\\textbf\{([^{}]*)\}", r"**\1**", t)
    t = re.sub(r"\\emph\{([^{}]*)\}", r"*\1*", t)
    t = re.sub(r"\\py\|([^|]*)\|", r"`\1`", t); t = t.replace("``", "«").replace("''", "»").replace("\\&", "&").replace("~", " ")
    t = t.replace("\\%", "%").replace("\\#", "#").replace("\\_", "_")
    return re.sub(r"\\[a-zA-Z]+\*?(\[[^]]*\])?", "", t).replace("{", "").replace("}", "").strip()
START = "from ColabTurtlePlus.Turtle import *\nclearscreen()\ninitializeTurtle((480, 360))"
cells = [md("""# 🐢 Mis aventuras con Python
### El cuaderno que acompaña a tu libro *De Scratch a Python*

¡Hola, programador o programadora! Cada misión de tu libro tiene su lugar aquí.

* Los cuadros grises son **celdas de código**. Haz clic en el **botón redondo ▶** a la izquierda de una celda para ejecutarla. ¡Es tu bandera verde!
* También puedes hacer clic dentro de la celda y presionar **Mayús + Intro** (*Shift + Enter*).
* Cada misión muestra el código del libro. **Escríbelo tú** en la celda vacía de abajo, letra por letra. ¡Así se aprende!
* Python habla inglés: sus palabras (`for`, `print`, `forward`...) siempre van en inglés. Los nombres que tú inventas van en español.
* ¿Te equivocaste? No pasa nada. Borra lo que escribiste y vuelve a intentarlo."""),
 md("""## ⭐ La celda «En el principio»
**Ejecuta esta celda primero, cada vez que abras este cuaderno.** Descarga las herramientas de dibujo de la tortuga, como cuando en Scratch haces clic en *Agregar Extensión* y eliges *Lápiz*.

⚠️ Tiene que decir **ColabTurtlePlus** (con *Plus*). Una biblioteca llamada ColabTurtle es otra distinta y no funciona con este libro."""),
 code("!pip install ColabTurtlePlus"),
 md(f"""## 🟨 Las tres líneas de inicio
Todo dibujo empieza con estas tres líneas. Hacen el trabajo de **al presionar bandera verde**: preparan el escenario (480 por 360, igual que en Scratch) y la tortuga.
```python
{START}
```
Después solo escribes órdenes como `forward(100)`. Ejecuta esta celda para probar:"""),
 code(START + "\nforward(100)")]
n = 0
for f in sorted(ch.glob("0[1-8]-*.tex")):
    if f.name.endswith("-answers.tex"): continue
    s = f.read_text(encoding="utf-8")
    m = re.search(r"\\partopener\{[^}]*\}\{([^}]*)\}\{([^}]*)\}", s)
    head = (m.group(1).capitalize() + ": " + m.group(2)) if m and m.group(1).upper().startswith("PARTE") else (m.group(2) if m else f.stem)
    cells.append(md(f"---\n# {head}"))
    marks = [(mm.start(), "mission", clean(mm.group(1))) for mm in re.finditer(r"\\mission\{((?:[^{}]|\{[^{}]*\})*)\}", s)]
    marks += [(mm.start(), "sub", clean(mm.group(1))) for mm in re.finditer(r"\\subsection\*\{((?:[^{}]|\{[^{}]*\})*)\}", s)]
    marks.sort()
    groups = []
    for bm in re.finditer(r"\\begin\{typethis\}(?:\[[^]]*\])?\n(.*?)\\end\{typethis\}", s, re.S):
        prev = [k for k in marks if k[0] < bm.start()]
        mission = next((k for k in reversed(prev) if k[1] == "mission"), None)
        label = prev[-1] if prev else (0, "sub", head)
        key = mission if (mission and not [k for k in prev if k[0] > mission[0] and k[1] == "sub" and "Tradúcelo" in k[2]]) else label
        if groups and groups[-1][0] == key: groups[-1][1].append(bm.group(1).rstrip())
        else: groups.append((key, [bm.group(1).rstrip()]))
    seen = set()
    for key, blocks in groups:
        title = key[2]
        if key[1] == "mission":
            if key not in seen: n += 1; seen.add(key)
            heading = f"## Misión {n}: {title}"
        else:
            heading = f"## {title}"
        src = "\n".join(blocks)
        cells.append(md(f"{heading}\n**Escribe esto en la celda de abajo** (está en la página de la misión, en tu libro):\n```python\n{src}\n```"))
        cells.append(code("# Escribe tu código aquí y luego presiona el botón ▶"))
        cells.append(code("# Hazlo tuyo: prueba aquí un reto del libro"))
bz = (ch / "09-bug-zoo.tex").read_text(encoding="utf-8")
hunts = re.findall(r"\\bzhunt\{(\d+)\}\{((?:[^{}]|\{[^{}]*\})*)\}\s*\\begin\{code\}\n(.*?)\\end\{code\}", bz, re.S)
cells.append(md("---\n# 🐞 Caza de bichos\nCada celda de abajo tiene **un bicho** (viene del Zoológico de Bichos de tu libro). Ejecútala, lee la **última línea** del texto rojo, arregla el código y vuelve a ejecutarla. Algunos bichos son tramposos y **no** muestran texto rojo: ¡revisa lo que de verdad hizo el programa!\n\nPython siempre escribe sus errores en inglés. Lo importante es el nombre del error (`NameError`, `SyntaxError`...).\n\nConsejo: Colab te dice que un nombre *is not defined* (no está definido), pero no adivina la palabra correcta. Revisa muy bien la ortografía y las mayúsculas."))
for num, desc, src in hunts:
    cells.append(md(f"**Caza de bichos {num}.** {clean(desc)}"))
    cells.append(code(src.rstrip()))
cells.append(md("---\n# 🎨 Juego libre\nElige uno de **tus propios** proyectos de Scratch y escríbelo aquí en Python. Ten abierto el Diccionario de bloques de tu libro para ayudarte."))
cells.append(code(START + "\n\n# Mi propio proyecto"))
cells.append(md("""---
### Si algo sale mal
* **¿Una celda no deja de ejecutarse?** Haz clic en el botón ■ de detener, donde estaba el botón de reproducir.
* **¿`No module named 'ColabTurtlePlus'`?** Vuelve a ejecutar la celda «En el principio».
* **¿`NameError`?** Revisa la ortografía, o ejecuta primero las celdas de arriba. También puedes abrir el menú **Entorno de ejecución** (*Runtime*) y elegir **Ejecutar todas** (*Run all*).
* Debajo de un error, el botón **Explicar error** (*Explain error*) puede ayudarte, ¡pero primero sé tú el detective!"""))
nb = {"cells": cells, "metadata": {"colab": {"provenance": [], "toc_visible": True}, "kernelspec": {"name": "python3", "display_name": "Python 3"}, "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 0}
(es / "Mis aventuras con Python.ipynb").write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
print(len(cells), "celdas,", n, "misiones,", len(hunts), "cazas de bichos")
