# Guía de traducción: edición en español de «De Scratch a Python»

You are one of 12 translator agents. Each agent translates **one chapter** of the English workbook
*From Scratch to Python* into Spanish, together with its answers file and its Colab test file.
The coordinator assembles the book. Read this whole guide before you start.

ROOT = the top folder of the English repository (github.com/Setopy/JesusArrows-scratch2python), with this Spanish repository checked out at `ROOT/es/`
- English sources (read only, never edit): `ROOT/chapters/NN-*.tex`, `ROOT/chapters/NN-*-answers.tex`, `ROOT/chapters/NN-colab-tests.py`, `ROOT/preamble.tex`, `ROOT/chapters/STYLE.md` (the original writing rules; they still apply).
- Spanish edition: `ROOT/es/`. Its preamble `ROOT/es/preamble.tex` is already translated (box titles, «MISIÓN», «Aprenderás:», footer, scratch3 `else word=si no`, polyglossia Spanish hyphenation). Never edit it.
- You write ONLY: `ROOT/es/chapters/<same file name as English>.tex`, the matching `-answers.tex` (if the English chapter has one), `ROOT/es/chapters/NN-colab-tests.py`, and your scratch files `ROOT/es/chapters/_test-NN.tex` and `ROOT/es/chapters/_build-NN/`. Keep the English file names.

## 1. Audience and voice

- A **9-year-old** who knows Scratch 3.0, reading with a parent. Same warmth, energy and short sentences as the English. Friendly, celebratory, never babyish.
- **Latin American neutral Spanish** (the family lives in Mexico): use **tú** (never vosotros/usted for the child), "computadora" (not "ordenador"), "celular", "jugar", "mouse"/"ratón" → use **"ratón"** because Scratch es-419 says "ratón". Speak to the parent as "tú" too in the grown-ups pages ("Para los adultos").
- Natural, idiomatic Spanish, not word-for-word. Keep every explanation, analogy, box and table: **do not shorten or drop content**. Keep the same LaTeX structure, same environments, same `\needspace`, same order.
- Prose quotes: use «comillas angulares» for quoted words in prose (`\enquote` is not loaded; type « » directly). Replace LaTeX ``...'' quotes in prose with «...». Code keeps straight quotes.
- Spanish punctuation: ¿...? and ¡...! Always.
- Numbers in prose: decimal point stays a point in code; in prose avoid decimals or write them as in code.
- Faith-based wording (this is for a Christian family; keep it): the «En el principio» cell. Bible quote in Spanish, Reina-Valera 1960: «En el principio creó Dios los cielos y la tierra» (Génesis 1:1). Book names in Spanish (Génesis, Éxodo, Salmos...).

## 2. Fixed vocabulary (use exactly these)

| English | Spanish |
|---|---|
| workbook / this book | este libro (the Colab file is the *cuaderno*) |
| notebook (Colab) | cuaderno (de Colab) |
| code cell | celda de código |
| play button | botón de reproducir (▶) |
| stop button | botón de detener (■) |
| run (a cell) | ejecutar |
| sprite | objeto (this is what Scratch in Spanish calls a sprite) |
| the turtle | la tortuga |
| stage | escenario |
| block / script | bloque / programa |
| green flag | bandera verde |
| Extensions button | botón **Agregar Extensión** (abajo a la izquierda en Scratch) |
| Pen extension | extensión **Lápiz** |
| My Blocks / Make a Block | **Mis Bloques** / **Crear un bloque** |
| Make a Variable / Make a List | **Crear una variable** / **Crear una lista** |
| costume / backdrop | disfraz / fondo |
| loop | bucle |
| variable / list | variable / lista |
| function | función |
| indentation / indent | sangría / poner sangría (four spaces = cuatro espacios) |
| colon | dos puntos |
| quote marks | comillas |
| brackets ( ) / square brackets [ ] | paréntesis / corchetes |
| writing / text (string) | texto (the book calls strings «escritura» in places; use **texto**) |
| bug / debugging | bicho (error en el código) / depurar, cazar bichos |
| Bug Zoo / Bug hunt | Zoológico de Bichos / Caza de bichos |
| mission | misión |
| Step 1: Build it in Scratch | Paso 1: Constrúyelo en Scratch |
| Step 2: Type it in Colab | Paso 2: Escríbelo en Colab |
| Step 3: Read it line by line | Paso 3: Léelo línea por línea |
| Step 4: Run it | Paso 4: Ejecútalo |
| Step 5: Make it yours | Paso 5: Hazlo tuyo |
| Line / Scratch block / What it means (table heads) | Línea / Bloque de Scratch / Qué significa |
| Translate it yourself | Tradúcelo tú |
| My Python (ruled box title) | Mi Python |
| Two-line puzzle | Acertijo de dos líneas (box default already set) |
| Part checklist / I can... | Lista de la parte / Ya sé... (tick items start with «Ya sé...» or «Puedo...») |
| challenge | reto |
| PART n | PARTE n |
| the three starting lines | las tres líneas de inicio |
| the "In the beginning" cell | la celda «En el principio» |
| How it works. | Cómo funciona. |
| You should see | Deberías ver (box default already set) |
| grown-ups | los adultos («Para los adultos») |
| colour (prose) | color |
| Did you notice? / Watch out! / Make it yours | already set as box defaults: ¿Te diste cuenta? / ¡Cuidado! / Hazlo tuyo |
| answers | respuestas |
| Thonny / Colab / Python / Scratch | unchanged |

Colab's menus appear in the language of the Google account. Write Colab interface names in Spanish
with the English in parentheses the first time on a page, e.g. **Entorno de ejecución** (*Runtime*) → **Ejecutar todas** (*Run all*);
**Herramientas** (*Tools*) → **Configuración** (*Settings*) → **Editor**; **+ Código** (*+ Code*);
**Archivo** (*File*) → **Subir cuaderno** (*Upload notebook*); the **Explicar error** (*Explain error*) button.

Python error messages are **always in English** (Python does not translate them). Keep them exactly as in the English book
inside `errorbox`/`\texttt`, and explain them in Spanish. Add (once per chapter where errors appear) a short note that
Python always writes its errors in English, and that the important word is the error name (`NameError`, ...).

## 3. Scratch blocks: official Spanish (Latinoamérica, es-419) labels

Every Scratch block (in scratch3 pictures **and** in `\chip`s **and** in prose) must use the official labels below, which
come from Scratch's own translation files (`ROOT/es/_ref/blocks-es-419.json`, `ext-es-419.json`; look up anything not listed).
Keep the scratch3 macro and change only the words. Default values: translate example text values ("Hello!" → "¡Hola!"),
keep numbers.

| English (scratch3 source) | Spanish |
|---|---|
| `\blockinit{when \greenflag clicked}` | `\blockinit{al presionar \greenflag}` |
| `when [space] key pressed` | `al presionar tecla \selectmenu{espacio}` (keys: flecha arriba/abajo/izquierda/derecha, cualquiera) |
| `when this sprite clicked` | `al hacer clic en este objeto` |
| `broadcast [message1]` / `when I receive [message1]` | `enviar \selectmenu{mensaje1}` / `al recibir \selectmenu{mensaje1}` |
| `move (10) steps` | `mover \ovalnum{10} pasos` |
| `turn ↻ (15) degrees` / `turn ↺` | `girar \turnright{} \ovalnum{15} grados` / `girar \turnleft{} ...` |
| `go to x: y:` / `go to [random position]` | `ir a x: \ovalnum{0} y: \ovalnum{0}` / `ir a \selectmenu{posición aleatoria}` |
| `glide (1) secs to x: y:` | `desplazar en \ovalnum{1} segs a x: \ovalnum{0} y: \ovalnum{0}` |
| `point in direction (90)` / `point towards [ ]` | `apuntar en dirección \ovalnum{90}` / `apuntar hacia \selectmenu{puntero del ratón}` |
| `change x by` / `set x to` / `change y by` / `set y to` | `cambiar x en` / `fijar x a` / `cambiar y en` / `fijar y a` |
| `if on edge, bounce` | `si toca un borde, rebotar` |
| `x position` / `y position` / `direction` | `posición en x` / `posición en y` / `dirección` |
| `say ( )` / `say ( ) for (2) seconds` | `decir` / `decir \ovalnum{¡Hola!} durante \ovalnum{2} segundos` |
| `think` / `think for secs` | `pensar` / `pensar ... durante ... segundos` |
| `switch costume to` / `next costume` | `cambiar disfraz a` / `siguiente disfraz` |
| `switch backdrop to` / `next backdrop` | `cambiar fondo a` / `siguiente fondo` |
| `set size to (100) %` / `change size by` | `fijar tamaño a \ovalnum{100} \%` / `cambiar tamaño en` |
| `change [color] effect by` / `set [color] effect to` | `cambiar el efecto \selectmenu{color} en` / `fijar efecto \selectmenu{color} a` |
| `show` / `hide` | `mostrar` / `esconder` |
| `go to [front] layer` | `ir a la capa \selectmenu{delantera}` |
| `start sound` / `play sound until done` / `stop all sounds` | `iniciar sonido` / `tocar sonido ... hasta que termine` / `detener todos los sonidos` |
| `change volume by` / `set volume to %` | `cambiar volumen en` / `fijar volumen a ... \%` |
| `wait (1) seconds` / `wait until` | `esperar \ovalnum{1} segundos` / `esperar hasta que` |
| `repeat (10)` / `forever` / `repeat until` | `repetir \ovalnum{10}` / `por siempre` / `repetir hasta que` |
| `if < > then` / `else` | `si ... entonces` / `si no` (preamble sets `else word=si no`) |
| `stop [all]` / `[this script]` / `[other scripts in sprite]` | `detener \selectmenu{todos}` / `este programa` / `otros programas en el objeto` |
| `create clone of [myself]` / `when I start as a clone` / `delete this clone` | `crear clon de \selectmenu{mí mismo}` / `al comenzar como clon` / `eliminar este clon` |
| `ask ( ) and wait` / `answer` | `preguntar \ovalnum{¿Cómo te llamas?} y esperar` / `respuesta` |
| `touching [ ]?` / `touching color?` | `¿tocando \selectmenu{...}?` / `¿tocando el color ...?` (edge = `el borde`, mouse = `el puntero del ratón`) |
| `distance to` / `key [space] pressed?` | `distancia a` / `¿tecla \selectmenu{espacio} presionada?` |
| `timer` / `reset timer` / `mouse x` / `mouse y` | `cronómetro` / `reiniciar cronómetro` / `posición x del ratón` / `posición y del ratón` |
| `pick random (1) to (10)` | `elegir número al azar entre \ovalnum{1} y \ovalnum{10}` |
| `( ) and ( )` / `or` / `not` | `y` / `o` / `no` |
| `join` / `letter (1) of` / `length of` / `contains?` | `unir` / `letra \ovalnum{1} de` / `longitud de` / `¿\ovalnum{manzana} contiene \ovalnum{a}?` |
| `( ) mod ( )` / `round` / `[abs] of` / `sqrt` | `módulo` / `redondear` / `\selectmenu{valor absoluto} de` / `raíz cuadrada` |
| `set [my variable] to` / `change [ ] by` | `fijar \selectmenu{puntos} a` / `cambiar \selectmenu{puntos} en` |
| `show variable` / `hide variable` | `mostrar variable` / `esconder variable` |
| `add ( ) to [list]` / `delete ( ) of` / `delete all of` | `añadir \ovalnum{manzana} a \selectmenu{comida}` / `eliminar \ovalnum{1} de` / `Eliminar todos de` |
| `insert ( ) at ( ) of` / `replace item ( ) of ( ) with ( )` | `insertar ... en ... de ...` / `reemplazar elemento ... de ... con ...` |
| `item ( ) of` / `item # of ( ) in` / `length of [list]` | `elemento ... de` / `\# de elemento de ... en ...` / `longitud de` |
| `[list] contains ( )?` | `¿\ovalnum{manzana} está en \selectmenu{comida}?` (es-419 order: item first) |
| `define [name]` | `\initmoreblocks{definir \namemoreblocks{...}}` |
| Pen: `pen down` / `pen up` / `erase all` / `stamp` | `bajar lápiz` / `subir lápiz` / `borrar todo` / `sellar` |
| Pen: `set pen color to` / `change pen color by` / `set pen size to` / `change pen size by` | `fijar color de lápiz a` / `cambiar color de lápiz en` / `fijar tamaño de lápiz a` / `cambiar tamaño de lápiz en` |
| Categories | Movimiento, Apariencia, Sonido, Eventos, Control, Sensores, Operadores, Variables, Listas, Mis Bloques, Lápiz, Música |

Spanish labels are longer. After compiling, check that chips and block pictures do not overflow table columns; if one does,
break a `\chip` into two chips with `\newline`, or shorten a default value, never the block label itself.

## 4. Python code

- **Python keywords and library names never change**: `for`, `while`, `if`, `def`, `print`, `input`, `range`, `forward`, `right`, `goto`, `pencolor`, `Turtle`, `random.randint`, etc. Say so once where it matters: «Python habla inglés: sus palabras (`for`, `print`, `forward`...) siempre van en inglés».
- **Translate what the child invents**: variable names, function names, sprite names, text in quotes, comments.
  - Names: Spanish **without accents and without ñ** (they are hard to type and confuse beginners): `respuesta`, `nombre`, `edad`, `puntos`, `secreto`, `intento`, `veces`, `gato`, `perro`, `cuadrado(lado)`, `estrella`, `triangulo`, `saltar()`, `comida`, `colores`, `notas`, `tamano` is ugly, prefer `medida`/`lado`. Use the same Spanish name for the same thing throughout your chapter. Keep `i`, `x`, `y`.
  - Text in quotes: natural Spanish **with** accents and ¿¡: `input("¿Cómo te llamas? ")`, `print("¡Lo lograste!")`.
  - Colour names stay **English** (the library only understands HTML colour names): `pencolor("red")`. The first time a chapter uses colours, add a short note: «Los colores se escriben en inglés: `"red"` es rojo, `"blue"` azul, `"gold"` dorado...».
  - Answers the child types (e.g. "left"/"right" in a game, "yes"/"no") become Spanish ("izquierda", "si"), and the code must compare with exactly the same Spanish words. Prefer answers without accents for typing (`"si"`), and mention it.
- **Keep every program's line structure identical** to the English (same number of lines, same order, blank lines in the same places), so the line numbers in the «Línea» tables stay right. If a translated line becomes longer than about 55 characters, shorten the Spanish text, don't add a line. If you truly must change line count, fix every table and reference.
- `outputbox` contents must show exactly what the Spanish program prints (re-run it).
- In the line-by-line tables, the «Bloque de Scratch» column uses the Spanish Scratch labels and the code column uses the Spanish code.

## 5. The Colab test file (`ROOT/es/chapters/NN-colab-tests.py`)

Translate `ROOT/chapters/NN-colab-tests.py` piece by piece: same pieces, same order, translated `# %%` names, code exactly
matching your Spanish chapter. Markers:
- `# escribe: p. ej. Ana, 7` (replaces `# needs typing: e.g. Ana, 7`): comma-separated answers typed in turn.
- A piece that is broken on purpose and must raise an error: put `(roto a propósito, espera NameError)` in its `# %%` name.
- A logic bug that runs without error: `(roto a propósito, sin error)`.

Then run it with the real ColabTurtlePlus library (Colab's display is stubbed), using a virtual environment that has `ColabTurtlePlus`, `numpy` and `ipython` installed:

```
<venv>/bin/python -I ROOT/es/chapters/_run_tests.py ROOT/es/chapters/NN-colab-tests.py
```

Every piece must PASS (SKIP is fine for `while True` and file reading). Also test every **non-drawing** program in your chapter
that is not in the test file (input programs, list programs...) with `printf 'Ana\n7\n' | python3 -I prog.py`, so that
every `typethis`/`code` box in your Spanish chapter has been run. Bug-zoo programs must fail in the same way as the English.

## 6. Compile and look

1. `cp ROOT/es/chapters/_harness.tex ROOT/es/chapters/_test-NN.tex` and replace `XX-name` with your file name (delete the answers lines if there is no answers file; for chapter 00 also add nothing else).
2. From `ROOT/es` run: `mkdir -p chapters/_build-NN && tectonic -o chapters/_build-NN chapters/_test-NN.tex` (allow several minutes; use a long timeout).
3. `pdftoppm -r 40 -png chapters/_build-NN/_test-NN.pdf chapters/_build-NN/pg` and LOOK at the pages with the Read tool. Fix overflowing chips/blocks/code, orphaned headings, half-empty pages. The Spanish text is ~15–25% longer; adjust `\needspace` if needed.
4. No compile errors. Overfull boxes over ~10pt must be fixed.

Gotchas (from the English guide): `\py|...|` cannot go inside `\chip`, `\subsection`, tcolorbox `title=` or other macro arguments: use `\texttt{}`. Escape `#`, `%`, `_`, `&`, `$` outside code. In `\texttt{}` write `¿` and `¡` directly. Mission titles go in `\mission{Título}{aprenderás ...}`: the second argument is the «Aprenderás:» text, in lowercase.

## 7. Final reply

At most 150 words: your files, page count of your test PDF, test results (PASS/FAIL/SKIP numbers and what else you ran), and anything the coordinator must know (a name you chose that other chapters might use, a label you could not find, an overflow you could not fix).
