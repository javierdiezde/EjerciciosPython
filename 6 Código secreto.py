import random
from time import sleep

def frase_rayitas(longitud):
    a = ("_" * longitud)
    return a


def sustituir_rayita(texto, posicion_sustituir, letra_sustituir):
    texto_sustituido = ""
    for posicion in range(0, len(texto)):
        if posicion == posicion_sustituir:
            texto_sustituido += letra_sustituir
        else:
            texto_sustituido += texto[posicion]
    return texto_sustituido


def adivinar_codigo(texto):

    frase_correcta = False
    frase_adivinada = frase_rayitas(len(texto))
    print(frase_adivinada)

    while not frase_correcta:
        posicion_adivinar = random.randint(0, (len(texto) - 1))
        intento = 0

        while ord(texto[posicion_adivinar]) != intento:
            if random.randint(1, 20) in range(3, 21):
                intento = random.randint(97, 122)
            else:
                intento = 32

        frase_adivinada = sustituir_rayita(frase_adivinada, posicion_adivinar, chr(intento))
        print(frase_adivinada)
        sleep(0.5)

        if not ("_" in frase_adivinada):
            frase_correcta = True


frase = input("Intruduce la frase\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
input()
adivinar_codigo(frase)
