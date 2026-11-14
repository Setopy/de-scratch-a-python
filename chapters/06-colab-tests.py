# Parte 6 (Mis Bloques): todos los programas de dibujo, listos para pegar en Colab.
# Ejecuta primero "!pip install ColabTurtlePlus" una vez. Cada pieza está completa.

# %% Concepto: entrada numérica (cuadrado)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))

def cuadrado(lado):
    for i in range(4):
        forward(lado)
        right(90)

cuadrado(50)
cuadrado(100)

# %% Concepto: varias entradas (poligono)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))

def poligono(lados, medida):
    for i in range(lados):
        forward(medida)
        right(360 / lados)

poligono(3, 100)
poligono(6, 50)

# %% Concepto: ejecutar sin actualizar la pantalla (animationOff)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))

def cuadrado(lado):
    for i in range(4):
        forward(lado)
        right(90)

def flor():
    animationOff()
    for i in range(36):
        cuadrado(80)
        right(10)
    animationOn()

flor()

# %% Concepto: más objetos (gato y perro)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))

gato = Turtle()
perro = Turtle()
gato.pencolor("orange")
perro.pencolor("blue")
gato.forward(100)
perro.left(90)
perro.forward(100)

# %% Concepto: pasarle un objeto a un bloque
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))

gato = Turtle()
perro = Turtle()
gato.pencolor("orange")
perro.pencolor("blue")

def cuadrado(t, lado):
    for i in range(4):
        t.forward(lado)
        t.right(90)

cuadrado(gato, 60)
cuadrado(perro, 100)

# %% Concepto: clones como una lista de objetos
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))

ejercito = []
for i in range(5):
    s = Turtle()
    s.shape("turtle")
    s.penup()
    s.goto(-200, 120 - i * 60)
    ejercito.append(s)

for s in ejercito:
    s.forward(100)

# %% Extra: cortador de galletas (una clase pequeña)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))

class Hormiga:
    def __init__(self, y):
        self.t = Turtle()
        self.t.shape("turtle")
        self.t.penup()
        self.t.goto(-200, y)

    def mover(self):
        self.t.forward(30)

hormigas = []
for i in range(3):
    hormigas.append(Hormiga(i * 60))

for paso in range(5):
    for h in hormigas:
        h.mover()

# %% Extra: árbol recursivo
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
speed(13)

def arbol(medida):
    if medida < 10:
        return
    forward(medida)
    left(30)
    arbol(medida * 0.7)
    right(60)
    arbol(medida * 0.7)
    left(30)
    back(medida)

penup()
goto(0, -170)
setheading(90)
pendown()
arbol(80)

# %% Misión: Haz tu propio bloque
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))

def cuadrado(lado):
    for i in range(4):
        forward(lado)
        right(90)

cuadrado(40)
cuadrado(80)
cuadrado(120)

# %% Misión: Haz tu propio bloque, reto de la flor
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
speed(13)

def cuadrado(lado):
    for i in range(4):
        forward(lado)
        right(90)

for i in range(12):
    cuadrado(80)
    right(30)

# %% Misión: Máquina de figuras
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
speed(13)

def poligono(lados, medida):
    for i in range(lados):
        forward(medida)
        right(360 / lados)

def flor(petalos, lados, medida):
    for i in range(petalos):
        poligono(lados, medida)
        right(360 / petalos)

penup()
goto(-170, 60)
pendown()
pencolor("blue")
poligono(5, 70)

penup()
goto(90, 0)
pendown()
pencolor("purple")
flor(12, 6, 40)

# %% Misión: Ejército de objetos
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))

colores = ["red", "orange", "gold", "green", "blue"]
ejercito = []
for i in range(5):
    s = Turtle()
    s.shape("turtle")
    s.color(colores[i])
    s.speed(13)
    s.penup()
    s.goto(-200, 120 - i * 60)
    s.pendown()
    ejercito.append(s)

def marchar(pasos):
    for s in ejercito:
        s.forward(pasos)

for paso in range(4):
    marchar(80)

# %% Tradúcelo tú: dos estrellas doradas
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))

def estrella(medida):
    for i in range(5):
        forward(medida)
        right(144)

pencolor("gold")
estrella(100)
estrella(50)
