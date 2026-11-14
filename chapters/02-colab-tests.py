# Parte 2: Bucles. Programas de dibujo, uno por celda. Ejecuta primero "!pip install ColabTurtlePlus".

# %% Concepto: repetir se convierte en for (cuadrado)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
for i in range(4):
    forward(100)
    right(90)
print("¡Cuadrado listo!")

# %% ¡Cuidado! El bicho tramposo de la sangría (roto a propósito, sin error; dibuja una línea larga)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
for i in range(4):
    forward(100)
right(90)

# %% Concepto: un bucle dentro de otro bucle (seis triángulos)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
for i in range(6):
    for j in range(3):
        forward(80)
        right(120)
    right(60)

# %% Concepto: por siempre se convierte en while True (no termina nunca: presiona el botón de detener)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
while True:
    forward(100)
    right(90)

# %% Misión: Dibuja figuras por el camino corto
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
pencolor("blue")
pensize(3)
for i in range(3):
    forward(120)
    right(120)

# %% Misión: Estrellas
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
pencolor("gold")
pensize(4)
penup()
goto(-75, 30)
pendown()
for i in range(5):
    forward(150)
    right(144)

# %% Misión: Espiral cuadrada
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
pencolor("purple")
speed(13)
for i in range(40):
    forward(i * 5)
    right(90)

# %% Misión: Flor de cuadrados
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
pencolor("deeppink")
speed(13)
for i in range(12):
    for j in range(4):
        forward(80)
        right(90)
    right(30)

# %% Tradúcelo tú (respuesta)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
pensize(4)
pencolor("purple")
for i in range(8):
    for j in range(6):
        forward(40)
        right(60)
    right(45)
penup()
print("¡Listo!")
