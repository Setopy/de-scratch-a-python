# Parte 3: Variables y listas. Programas que dibujan, uno por celda.
# Ejecuta la celda «En el principio» una vez por sesión: !pip install ColabTurtlePlus

# %% Página de conceptos: Las variables también dibujan (dos cuadrados)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
medida = 50
for i in range(4):
    forward(medida)
    right(90)
medida = medida + 50
for i in range(4):
    forward(medida)
    right(90)

# %% Misión: Espiral que crece
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
speed(13)
pencolor("purple")
medida = 5
for i in range(40):
    forward(medida)
    right(90)
    medida = medida + 5

# %% Misión: Espiral que crece, reto (girar 91)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
speed(13)
pencolor("purple")
medida = 5
for i in range(40):
    forward(medida)
    right(91)
    medida = medida + 5

# %% Misión: Arcoíris con una lista de colores
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
speed(13)
pensize(15)
colores = ["red", "orange", "yellow",
           "green", "blue", "purple"]
y = 60
for color in colores:
    pencolor(color)
    penup()
    goto(-150, y)
    pendown()
    forward(300)
    y = y - 15
hideturtle()

# %% Respuestas: Arcoíris, reto (append "pink", huecos más grandes)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
speed(13)
pensize(15)
colores = ["red", "orange", "yellow",
           "green", "blue", "purple"]
colores.append("pink")
y = 60
for color in colores:
    pencolor(color)
    penup()
    goto(-150, y)
    pendown()
    forward(300)
    y = y - 20
hideturtle()

# %% Respuestas: Espiral que crece, más abierta (+ 8)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
speed(13)
pencolor("purple")
medida = 5
for i in range(40):
    forward(medida)
    right(90)
    medida = medida + 8

# %% Respuestas: Espiral que crece, lápiz más grueso
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
speed(13)
pencolor("purple")
medida = 5
grueso = 1
for i in range(40):
    pensize(grueso)
    forward(medida)
    right(90)
    medida = medida + 5
    grueso = grueso + 0.2

# %% Respuestas: Espiral que se encoge
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
speed(13)
pencolor("purple")
penup()
goto(-100, 100)
pendown()
medida = 200
for i in range(40):
    forward(medida)
    right(90)
    medida = medida - 5

# %% Respuestas: Arcoíris, superreto (franjas más cortas)
from ColabTurtlePlus.Turtle import *
clearscreen()
initializeTurtle((480, 360))
speed(13)
pensize(15)
colores = ["red", "orange", "yellow",
           "green", "blue", "purple"]
y = 60
largo = 300
for color in colores:
    pencolor(color)
    penup()
    goto(-150, y)
    pendown()
    forward(largo)
    y = y - 15
    largo = largo - 30
hideturtle()

