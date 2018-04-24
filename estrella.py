# vamos a dibujar una estrella
import turtle
from  random import randint

turtle.setup(640,480,0,0)
pepa=turtle.Turtle()
# n= int(input('¿Cuántos lados tiene la estrella? pon un número impar: '))
longitud=100
def estrella(longitud=100, n=5):
    for i in range(n):
        pepa.forward(longitud)
        pepa.right(180*4/n)
        

for i in range (5,21,2):
    x=randint(-200,200)
    y=randint(-150,150)
    longitud=randint(20,120)
    pepa.penup()
    pepa.goto(x,y)
    pepa.pendown()
    estrella(longitud,i)
    
