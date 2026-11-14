# Parte 5: Sensores y decisiones -- programas de dibujo para Colab
# Ejecuta una vez la celda «En el principio» (!pip install ColabTurtlePlus) y luego pega
# cada pieza en su propia celda.

# %% Concepto: tocar una mancha (distancia a un punto)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
dot(20, "red")
penup()
goto(-200, 0)
pendown()
while distance(0, 0) >= 20:
    forward(10)
print("¡La toqué!")

# %% Concepto: tocar otro objeto
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
shape("turtle")
perro = Turtle()
perro.shape("circle")
perro.penup()
perro.goto(150, 0)
while distance(perro.pos()) >= 20:
    forward(10)
print("¡Te atrapé, perro!")

# %% Concepto: ¿tecla presionada? se convierte en turnos con input()
# escribe: p. ej. a, i, a, d, a
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
shape("turtle")
for i in range(5):
    tecla = input("¿a, i o d? ")
    if tecla == "i":
        left(90)
    elif tecla == "d":
        right(90)
    forward(50)

# %% Concepto: si toca un borde, rebotar (hecho en casa)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
speed(13)
setheading(30)
for i in range(300):
    forward(10)
    if xcor() > 230 or xcor() < -230:
        setheading(180 - heading())
    if ycor() > 170 or ycor() < -170:
        setheading(0 - heading())
