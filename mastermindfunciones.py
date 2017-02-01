# Introducimos un código de 4 cifras
# El programa nos pide que lo averigüemos introduciendo sucesivamente códigos.
# El programa sólo responde cuantos números aparecen y cuántos están en su posición correcta.
import random
secreto = str(random.randrange(999))
print (secreto)
# secreto = input('Introduce el código de 3 cifras: ')
contador = 0
def introduce_numero_correcto():
    intento = input('Averigua el código: ')
    while  len(intento)!=3 or intento.isdigit()!= True:
        if len(intento)<3:
            print('pocas cifras')
        elif len(intento)>3:
            print('muchas cifras')
        elif intento.digit()!= True:
            print('Tiene que tener sólo 3 números enteros')
        intento = input ('Vuelve a introducir tu código: ')
    return  intento
    print ('por fin lo has escrito bien...')
intento = introduce_numero_correcto()
contador += 1
while secreto != intento:
    # contamos cuántos números coinciden
    numeros = 0
    for i in intento:
        if i in secreto:
            numeros += 1
    print('Coinciden ', numeros, ' números')
    posiciones = 0
    for i in range(len(secreto)):
        if intento[i] == secreto[i]:
            posiciones += 1
    print('posiciones correctas:', posiciones)
    print('Prueba otro número: ')
    intento = introduce_numero_correcto()
    contador += 1
print('Felicidades sólo has usado ', contador, ' intentos')
