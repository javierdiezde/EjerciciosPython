# Persigue a la tortuga
# https://www.programoergosum.com/cursos-online/raspberry-pi/245-turtle-graphics-en-python-con-raspberry-pi/mi-primer-juego

import turtle
from turtle import *
#from random import randint
import random
import math

setup(850, 650,0,0)

ladron = turtle.Turtle()
policia= turtle.Turtle()
window = turtle.Screen()


colormode (255)

policia.goto(-300,-200)

# ladron.goto( -400,-200)

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
def estrella (n,long):
    policia.begin_fill()
    azul=random.randint(0,255)
    rojo=random.randint(0,255)
    verde=random.randint(0,255)
    for i in range (n):
        #angulo_interior=(180*(n-2))/(n-3)
        angulo_interior=180 - 180/n
        
        policia.forward(long)
        policia.right(angulo_interior)
        policia.fillcolor(rojo,azul,verde)
    policia.end_fill()


window.onkeypress(arriba,'Up')
window.onkeypress(abajo,'Down')
window.onkeypress(derecha,'Right')
window.onkeypress(izquierda,'Left')

# Movimiento del ladrón


distancia = 1000


while distancia>30:
    movimiento = random.randrange(1,4)
    longitud = random.randrange(10,70)
    angulo=random.randrange(360)
    # print(movimiento, longitud)
    window.listen()
    if movimiento ==1: # círculo
        ladron.circle(longitud)
    elif movimiento==2:  # recta
        ladron.seth(angulo)
        ladron.forward(longitud)
    elif movimiento==3: 
        ladron.circle(longitud/3)
        ladron.forward (longitud/3)

    coord_ladron=ladron.pos()
    coord_poli=policia.pos()
    distancia = ( (coord_ladron[1]-coord_poli[1])**2 +(coord_ladron[0]-coord_poli[0])**2)**.5
    print(distancia)
    
estrella(7,50)
   
        
        




