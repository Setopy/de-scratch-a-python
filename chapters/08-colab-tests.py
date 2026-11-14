# 08 Grandes proyectos: programas de dibujo para Colab (ejecuta "!pip install ColabTurtlePlus" una vez primero)

# %% Gran proyecto: Anima tu nombre
# escribe: ¿Cómo te llamas? (p. ej. Ximena)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import random
import time

bgcolor("black")
hideturtle()
penup()
speed(13)
colores = ["red", "orange", "gold", "lime", "skyblue",
           "violet", "hotpink"]

nombre = input("¿Cómo te llamas? ")
espacio = 40
if len(nombre) > 10:
    espacio = 400 / len(nombre)
inicio = 0 - (len(nombre) - 1) * espacio / 2

for cuadro in range(8):
    clear()
    x = inicio
    for letra in nombre:
        color(random.choice(colores))
        goto(x, random.randint(-20, 20))
        write(letra, align="center",
              font=("Arial", 40, "bold"))
        x = x + espacio
    time.sleep(0.3)

goto(0, -120)
color("white")
write("¡Hola, " + nombre + "!", align="center",
      font=("Arial", 24, "italic"))

# %% Gran proyecto: Flor de lápiz
# escribe: ¿Cuántos pétalos? (p. ej. 8)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))

bgcolor("black")
speed(13)
pensize(2)
colores = ["red", "orange", "gold", "lime",
           "skyblue", "violet"]

def petalo(medida):
    circle(medida, 60)
    left(120)
    circle(medida, 60)
    left(120)

petalos = int(input("¿Cuántos pétalos? (3 a 20) "))
for p in range(petalos):
    color(colores[p % 6])
    petalo(100)
    left(360 / petalos)

color("white")
for anillo in range(36):
    circle(40)
    left(10)

penup()
goto(0, 0)
dot(25, "gold")
hideturtle()

# %% Gran proyecto: Juego de persecución
# escribe: w, a, s o d + Enter, hasta 20 veces
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import random

speed(13)
shape("turtle")
color("green")
penup()

gato = Turtle()
gato.speed(13)
gato.shape("circle")
gato.color("orange")
gato.penup()
gato.goto(200, 140)

estrella = Turtle()
estrella.speed(13)
estrella.shape("triangle")
estrella.color("gold")
estrella.penup()
estrella.goto(120, -80)

puntos = 0
for turno in range(20):
    jugada = input("Muévete con w, a, s o d: ").lower()
    if jugada == "w":
        setheading(90)
    elif jugada == "s":
        setheading(270)
    elif jugada == "a":
        setheading(180)
    elif jugada == "d":
        setheading(0)
    forward(40)
    if xcor() > 220 or xcor() < -220:
        back(40)
    if ycor() > 160 or ycor() < -160:
        back(40)

    if estrella.distance(pos()) < 20:
        puntos = puntos + 1
        print("¡Atrapaste la estrella! Puntos:", puntos)
        x = random.randint(-5, 5) * 40
        y = random.randint(-4, 4) * 40
        estrella.goto(x, y)

    gato.setheading(gato.towards(pos()))
    gato.forward(25)
    if gato.distance(pos()) < 30:
        print("¡El gato te atrapó!")
        break

print("¡Fin del juego! Estrellas:", puntos)

# %% Gran proyecto: Juego de atrapar
# escribe: x de la canasta cinco veces (p. ej. 0, 80, -80, 160, 0)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import random

bgcolor("skyblue")
hideturtle()

canasta = Turtle()
canasta.shape("square")
canasta.color("brown")
canasta.penup()
canasta.goto(0, -150)

manzana = Turtle()
manzana.shape("circle")
manzana.color("red")
manzana.penup()
manzana.speed(13)

puntos = 0
for ronda in range(5):
    x = random.choice([-80, 0, 80])
    viento = random.choice([-20, 0, 20])
    manzana.jumpto(x, 160)
    for paso in range(4):
        manzana.goto(manzana.xcor() + viento,
                     manzana.ycor() - 40)

    lugar = int(input("Canasta x (-240 a 240): "))
    canasta.goto(lugar, -150)

    for paso in range(4):
        manzana.goto(manzana.xcor() + viento,
                     manzana.ycor() - 40)
    if canasta.distance(manzana.pos()) < 50:
        puntos = puntos + 1
        print("¡Atrapada!")
    else:
        print("¡Plaf! Cayó en x =",
              round(manzana.xcor()))

print("Atrapaste", puntos, "de 5 manzanas")

# %% Respuestas: jardín de flores de lápiz (sube de nivel)
# escribe: ¿Cuántos pétalos? (p. ej. 7)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))

bgcolor("black")
speed(13)
pensize(2)
colores = ["red", "orange", "gold", "lime",
           "skyblue", "violet"]

def petalo(medida):
    circle(medida, 60)
    left(120)
    circle(medida, 60)
    left(120)

def flor(x, y):
    penup()
    goto(x, y)
    pendown()
    for p in range(petalos):
        color(colores[p % 6])
        petalo(50)
        left(360 / petalos)

petalos = int(input("¿Cuántos pétalos? (3 a 20) "))
flor(-150, 0)
flor(0, 0)
flor(150, 0)
hideturtle()

# %% Respuestas: jugador computadora en el juego de atrapar (sube de nivel)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import random

bgcolor("skyblue")
hideturtle()

canasta = Turtle()
canasta.shape("square")
canasta.color("brown")
canasta.penup()
canasta.goto(0, -150)

manzana = Turtle()
manzana.shape("circle")
manzana.color("red")
manzana.penup()
manzana.speed(13)

puntos = 0
for ronda in range(5):
    x = random.choice([-80, 0, 80])
    viento = random.choice([-20, 0, 20])
    manzana.jumpto(x, 160)
    for paso in range(4):
        manzana.goto(manzana.xcor() + viento,
                     manzana.ycor() - 40)

    lugar = manzana.xcor() + 4 * viento
    canasta.goto(lugar, -150)

    for paso in range(4):
        manzana.goto(manzana.xcor() + viento,
                     manzana.ycor() - 40)
    if canasta.distance(manzana.pos()) < 50:
        puntos = puntos + 1
        print("¡Atrapada!")
    else:
        print("¡Plaf! Cayó en x =",
              round(manzana.xcor()))

print("Atrapaste", puntos, "de 5 manzanas")
