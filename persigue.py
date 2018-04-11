# Persigue a la tortuga
import turtle
from turtle import *

setup(850, 650,0,0)

ladron = turtle.Turtle()
policia= turtle.Turtle()
window= turtle.Screen()


colormode (255)

policia.goto(0,0)

ladron.goto( -400,-200)

velocidad=10

def arriba(velocidad=10):
    policia.setheading(90)
    policia.forward(velocidad)
def abajo(velocidad=10):
    policia.setheading(270)
    policia.forward(velocidad)
def derecha(velocidad=10):
    policia.setheading(0)
    policia.forward(velocidad)
def izquierda(velocidad=10):
    policia.setheading(180)
    policia.forward(velocidad)





window.onkeypress(arriba,'Up')
window.onkeypress(abajo,'Down')
window.onkeypress(derecha,'Right')
window.onkeypress(izquierda,'Left')



window.listen()
