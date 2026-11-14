# Pruebas de Colab del capítulo 09 (El Zoológico de Bichos). Ejecuta la celda
# «En el principio» (!pip install ColabTurtlePlus) una vez antes de estas.

# %% Caza de bichos 9 (roto a propósito, sin error): dibuja una línea larga, no un cuadrado
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
for i in range(4):
    forward(50)
right(90)

# %% Caza de bichos 9 (arreglado): dibuja un cuadrado
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
for i in range(4):
    forward(50)
    right(90)

# %% Tarjeta 4 del zoológico (roto a propósito, espera NameError ... Did you mean: 'forward'?)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
forwad(100)
