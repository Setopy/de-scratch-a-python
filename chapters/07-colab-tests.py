# Parte 7: Apariencia, sonido y eventos. Programas de prueba para Colab.
# Ejecuta la celda «En el principio» (!pip install ColabTurtlePlus) antes de estas.
# Cada pieza está completa. Las piezas de sonido necesitan antes la pieza «celda de sonido».

# %% Concepto: palabras en el escenario (decir durante 2 segundos)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import time

shape("turtle")
globo = Turtle()
globo.hideturtle()
globo.penup()
globo.goto(0, 30)
globo.write("¡Hola!", align="center",
            font=("Arial", 20, "normal"))
time.sleep(2)
globo.clear()

# %% Concepto: pensar en el escenario
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import time

shape("turtle")
globo = Turtle()
globo.hideturtle()
globo.penup()
globo.goto(0, 30)
globo.write("Mmm...", align="center",
            font=("Arial", 20, "italic"))
time.sleep(2)
globo.clear()

# %% Concepto: cambiar disfraz
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))

shape("turtle")

# %% Concepto: siguiente disfraz
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import time

disfraces = ["turtle", "circle",
             "square"]
n = 0
shape(disfraces[n])
for i in range(6):
    time.sleep(1)
    n = (n + 1) % len(disfraces)
    shape(disfraces[n])

# %% Concepto: fijar tamaño y cambiar tamaño
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import time

shape("turtle")
shapesize(2)
time.sleep(1)
medida = 200
for i in range(5):
    medida = medida + 50
    shapesize(medida / 100)
    time.sleep(0.5)

# %% Concepto: mostrar y esconder
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import time

shape("turtle")
for i in range(3):
    hideturtle()
    time.sleep(0.5)
    showturtle()
    time.sleep(0.5)

# %% Concepto: fondo y efecto de color
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import time

shape("turtle")
shapesize(3)
bgcolor("skyblue")
arcoiris = ["red", "orange",
            "gold", "green"]
for c in arcoiris:
    color(c)
    time.sleep(0.5)

# %% Concepto: celda de sonido (ejecútala una vez)
import numpy as np
from IPython.display import Audio, display

def pitido(frec=440, segs=0.5):
    instantes = np.linspace(0, segs, int(22050 * segs))
    sonido = np.sin(2 * np.pi * frec * instantes)
    display(Audio(sonido, rate=22050, autoplay=True))

# %% Concepto: iniciar sonido y tocar hasta que termine
import time
pitido(262)
time.sleep(0.5)
pitido(330)
time.sleep(0.5)
pitido(392, 1)

# %% Concepto: una melodía desde una lista
import time
notas = [262, 294, 330, 349, 392, 440, 494, 523]
for nota in notas:
    pitido(nota, 0.3)
    time.sleep(0.4)

# %% Concepto: melodía en un solo sonido (si las notas se amontonan)
def tocar_melodia(notas, segs=0.4):
    partes = []
    for nota in notas:
        instantes = np.linspace(0, segs, int(22050 * segs))
        partes.append(np.sin(2 * np.pi * nota * instantes))
    cancion = np.concatenate(partes)
    display(Audio(cancion, rate=22050, autoplay=True))

tocar_melodia([262, 262, 392, 392, 440, 440, 392])

# %% Concepto: las teclas se convierten en turnos con input()
# escribe: p. ej. a, i, a, d, a (una por pregunta)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))

shape("turtle")
for turno in range(5):
    tecla = input("¿a, i o d? ")
    if tecla == "a":
        forward(50)
    elif tecla == "i":
        left(90)
    elif tecla == "d":
        right(90)

# %% Concepto: un bucle mueve a todos los objetos
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))

hideturtle()
gato = Turtle()
gato.shape("turtle")
perro = Turtle()
perro.shape("circle")
perro.left(90)
for paso in range(20):
    gato.forward(10)
    perro.forward(5)

# %% Misión: Desfile de disfraces
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import time

disfraces = ["turtle", "circle", "square", "triangle"]
colores = ["green", "red", "blue", "orange"]
n = 0
medida = 100
bgcolor("lavender")
for i in range(8):
    shape(disfraces[n])
    color(colores[n])
    shapesize(medida / 100)
    print("Disfraz", n + 1, disfraces[n])
    time.sleep(0.5)
    n = (n + 1) % len(disfraces)
    medida = medida + 50
hideturtle()
print("¡Tarán!")

# %% Misión: Hacer música (ejecuta antes la celda de sonido)
import time
Do = 262
Re = 294
Mi = 330
Fa = 349
Sol = 392
La = 440

melodia = [Do, Do, Sol, Sol, La, La, Sol]
tiempos = [1, 1, 1, 1, 1, 1, 2]
for i in range(len(melodia)):
    segs = tiempos[i] * 0.4
    pitido(melodia[i], segs)
    time.sleep(segs + 0.1)
print("Estrellita, ¿dónde estás?")

# %% Misión: Hacer música, respuesta del reto ¡Feliz cumpleaños!
import time
Sol = 392
La = 440
Si = 494
Do2 = 523
melodia = [Sol, Sol, La, Sol, Do2, Si]
tiempos = [0.75, 0.25, 1, 1, 1, 2]
for i in range(len(melodia)):
    segs = tiempos[i] * 0.5
    pitido(melodia[i], segs)
    time.sleep(segs + 0.1)

# %% Misión: Carrera de tortugas
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import random

def crear_corredor(su_color, y):
    corredor = Turtle()
    corredor.shape("turtle")
    corredor.color(su_color)
    corredor.penup()
    corredor.goto(-200, y)
    corredor.pendown()
    return corredor

hideturtle()
rojo = crear_corredor("red", 50)
azul = crear_corredor("blue", -50)

while rojo.xcor() < 200 and azul.xcor() < 200:
    rojo.forward(random.randint(1, 20))
    azul.forward(random.randint(1, 20))

if rojo.xcor() > azul.xcor():
    print("¡Gana Rojo!")
    rojo.write("¡Gané!", font=("Arial", 16, "bold"))
else:
    print("¡Gana Azul!")
    azul.write("¡Gané!", font=("Arial", 16, "bold"))

# %% Tradúcelo tú (respuesta)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import time

shape("turtle")
shapesize(3)
for i in range(3):
    hideturtle()
    time.sleep(0.5)
    showturtle()
    time.sleep(0.5)
print("¡Bu!")
time.sleep(2)
