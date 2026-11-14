# Programas de dibujo de chapters/00-front.tex (pega cada pieza en Colab).
# Ejecuta primero, una vez, la celda «En el principio»:  !pip install ColabTurtlePlus

# %% Conoce Google Colab: primera línea
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
forward(100)

# %% Palabras de Scratch: ir a y apuntar en dirección
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
goto(100, 80)
setheading(90 - 180)
forward(50)

# %% Hábito 1: los espacios muestran qué va adentro
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
for i in range(4):
    forward(100)
    right(90)
penup()

# %% En qué se diferencia Colab: un solo bucle mueve todos los objetos
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
gato = Turtle()
perro = Turtle()
perro.left(90)
for i in range(10):
    gato.forward(10)
    perro.forward(10)

# %% En qué se diferencia Colab: figuras y colores
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
shape("turtle")
color("gold")
forward(100)
