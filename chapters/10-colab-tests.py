# Fragmentos de dibujo del diccionario de bloques y de la hoja de ayuda (Parte 10).
# Cada fragmento está completo, con las tres líneas de inicio.

# %% Diccionario: filas de Movimiento
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import random
gato = Turtle()
gato.penup()
gato.goto(-100, 50)
forward(10)
back(10)
right(15)
left(15)
x = random.randint(
    -240, 240)
y = random.randint(
    -180, 180)
goto(x, y)
goto(gato.pos())
goto(0, 0)
home()
speed(2)
goto(50, 50)
speed(1)
goto(0, 0)
setheading(0)
setheading(90 - 180)
p = gato.pos()
d = towards(p)
setheading(d)
setx(xcor() + 10)
setx(0)
sety(ycor() + 10)
sety(0)
for i in range(60):
    forward(10)
    h = heading()
    if abs(xcor()) > 240:
        setheading(180-h)
    if abs(ycor()) > 180:
        setheading(-h)
shape("circle")
print(round(xcor()), round(ycor()), 90 - heading())

# %% Diccionario: filas de Apariencia
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
import time
print("¡Hola!")
time.sleep(2)
write("¡Hola!")
print("(Umm...)")
shape("turtle")
disfraces = ["turtle", "circle", "square", "arrow"]
n = 0
for i in range(4):
    n = (n + 1) % 4
    shape(disfraces[n])
    time.sleep(0.5)
cielos = ["white", "skyblue", "gold"]
b = 0
b = (b + 1) % 3
bgcolor(cielos[b])
bgcolor("skyblue")
medida = 100
medida = medida + 10
shapesize(medida / 100)
shapesize(2)
fillcolor("gold")
color("gold")
fillcolor("pink")
color("black")
hideturtle()
showturtle()
print(n + 1, shape(), b + 1, bgcolor(), medida)

# %% Diccionario: filas de clones y Sensores
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
estrella = Turtle()
estrellas = []
for i in range(3):
    s = Turtle()
    s.shape("circle")
    s.goto(-100 + 100 * i, 100)
    estrellas.append(s)
s.hideturtle()
estrellas.remove(s)
gato = Turtle()
gato.goto(10, 0)
p = gato.pos()
print(distance(p) < 20, distance(gato.pos()), gato.xcor(), gato.ycor(), gato.heading())
print(ycor() < -100, abs(xcor()) > 240)

# %% Diccionario: filas de Lápiz
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
speed(13)
pendown()
pencolor("red")
forward(50)
stamp()
clearstamps()
arcoiris = ["red", "gold", "green"]
c = 0
for i in range(6):
    c = (c + 1) % 3
    pencolor(arcoiris[c])
    forward(20)
    right(60)
pencolor("cyan")
pencolor("darkred")
pencolor("pink")
g = pensize() + 1
pensize(g)
pensize(5)
penup()
goto(-100, -100)
pendown()
fillcolor("gold")
begin_fill()
circle(50)
end_fill()
clear()

# %% Hoja de ayuda: todos los recuadros de dibujo juntos
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
speed(13)
def cuadrado(lado):
    for i in range(4):
        forward(lado)
        right(90)
cuadrado(50)
def doble(n):
    return n * 2
print(doble(4))
gato = Turtle()
gato.shape("turtle")
gato.goto(-100, 0)
gato.forward(50)
print(gato.distance(pos()) < 20)
