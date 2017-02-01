# Genera un número aleatorio y tenemos que averiguarlo
# El Ordenador sólo responde si el número que introducimos en menor o mayor
import random
secreto = random.randrange(10000)
print('El número a adivinar es: ',secreto)
intento= int(input('Introduce un número de 4 cifras: '))
contador = 0
while secreto != intento:
    if secreto < intento:
        intento = int(input(' Es más grande, intenta otro: '))
        contador =contador +1
    elif secreto > intento:
        intento = int(input(' Es más pequeño, intenta otro: '))
        contador = contador +1

print('acertaste, el número es: ',intento)
print('Sólo has necesitado ',contador, 'intentos')



