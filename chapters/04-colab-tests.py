# Parte 4 (Operadores): programas que dibujan, para Colab.
# Ejecuta primero, una vez, la celda «En el principio» (!pip install ColabTurtlePlus).

# %% Misión: Arte de puntos al azar
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import random

colores = ["red", "gold", "skyblue", "pink", "lime"]
speed(13)
penup()
hideturtle()
for i in range(50):
    x = random.randint(-240, 240)
    y = random.randint(-180, 180)
    goto(x, y)
    medida = random.randint(10, 40)
    tono = colores[random.randint(0, 4)]
    dot(medida, tono)

# %% Misión: Arte de puntos al azar, versión del reto (cielo de noche, 7 colores)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import random
bgcolor("black")

colores = ["red", "gold", "skyblue", "pink", "lime",
           "orange", "purple"]
speed(13)
penup()
hideturtle()
for i in range(200):
    x = random.randint(-240, 240)
    y = random.randint(0, 180)
    goto(x, y)
    medida = random.randint(10, 40)
    tono = colores[random.randint(0, len(colores) - 1)]
    dot(medida, tono)
