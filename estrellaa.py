# estrella de puntas agudas
import turtle
from turtle import *
from random import randint

setup(640, 480, 0, 0)
bgcolor('blue')
pepe=turtle.Turtle()

colormode(255)


def estrella (n,long):
    pepe.begin_fill()
    azul=randint(0,255)
    rojo=randint(0,255)
    verde=randint(0,255)
    for i in range (n):
        #angulo_interior=(180*(n-2))/(n-3)
        angulo_interior=180 - 180/n
        
        pepe.forward(long)
        pepe.right(angulo_interior)
        pepe.fillcolor(rojo,azul,verde)
    pepe.end_fill()   
for i in range(5,21,2):
    x=randint(-300,300)
    y=randint(-200,200)
    long=randint(40,60)
    
    
    pepe.penup()
    pepe.goto(x,y)
    pepe.pendown()
    estrella(i,long)


        
