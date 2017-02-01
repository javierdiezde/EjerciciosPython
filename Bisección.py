# Resuelve la ecuación x·sen(x)= ln(x) en el intervalo [2,3]
import math
print(' Resuelve la ecuación x·sen(x)= ln(x) en el intervalo [2,3]')
decimal = int (input('Hasta qué decimal quieres que aproxime? '))
tolerancia = 10**((-1)*decimal)
print (tolerancia)
a=2.0
b=3.0
distancia = b-a
print(distancia)
c=(a+b)/2
while tolerancia < distancia:
    input('pasa')
    fa =a*math.sin(a)-math.log(a)
    fb = b*math.sin(b)-math.log(b)
    fc = c*math.sin(c) - math.log(c)
    print ('la raíz está en el intervalo: ')
    print (a,b)
    print('Evaluamos en el punto medio: ', fc )
    if fa*fc < 0: # La raíz está entre a y c
        b=c
        c= (a+b)/2
        distancia=b-a
    elif fb *fc < 0: # La raíz está entre c y b
        a=c
        c=(a+b)/2
        distancia=b-a
    else:
        print( 'La solución es: ',c )
print ( 'La solución de la ecuación es aproximadamente: ', c)





