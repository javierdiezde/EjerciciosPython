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

def ira(x,y):
    perseo.goto(x,y)
    print(x,y)
def arriba():
    perseo.setheading(90)
    perseo.forward(10)
def muere():
    
def restricciones(x,y):
    # círculo central
    if x^2+y^2<100:
        muere()
        
    
window.listen()

while True:
    window.onkeypress(arriba,'Up')
    window.onclick(ira)
   
    
        




