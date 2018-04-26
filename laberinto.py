# Persigue a la tortuga
# https://www.programoergosum.com/cursos-online/raspberry-pi/245-turtle-graphics-en-python-con-raspberry-pi/mi-primer-juego

import turtle
from turtle import *
#from random import randint
import random
import math

perseo = turtle.Turtle()
window = turtle.Screen()
setup(850, 650,0,0)
colormode (255)
perseo.penup()
perseo.goto(-200,-100)
perseo.pendown()

def ira(x,y):
    perseo.goto(x,y)
    print(x,y)
    restricciones(x,y)
def arriba():
    perseo.setheading(90)
    perseo.forward(10)
def muere():
    perseo.penup()
    perseo.goto(-200,-199)
    perseo.pendown()

    
def restricciones(x,y):
    # círculo central de radio 10
    if x**2+y**2<100:
        perseo.penup()
        pereseo.goto(0,0)
        perseo.pendown()
        perseo.circle(10)
        muere()
    elif x<2 and x>-100 and -10<y and y<10: # rectángulo -100<x<2 -10<y<10
        perseo.penup()
        perseo.goto (-100,-10)
        perseo.pendown()
        
        
        
        
    
        
    
window.listen()

window.onkeypress(arriba,'Up')
window.onclick(ira)


    
