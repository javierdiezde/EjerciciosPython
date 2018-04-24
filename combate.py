# Establecemos un programa para estudiar un ejercicio de probabilidad
import random
ganamonstruos=0
ganasoldados = 0
veces = int(input('Cuantos combates hago'))
numerosoldados = int(input('cuantos soldados? '))

for i in range(1,veces):
    monstruogrande= random.randrange(20)
    monstruomediano= random.randrange(12)
    sumasoldados=0
    for j in range(1,numerosoldados):
        sumasoldados = sumasoldados + random.randrange(6)

    
    sumamonstruos = monstruogrande + monstruomediano
    
    if sumamonstruos > sumasoldados:
        ganamonstruos = ganamonstruos + 1
    elif sumamonstruos < sumasoldados:
        ganasoldados = ganasoldados + 1
    else:
        ganasoldados += .5
        ganamonstruos += .5
    print(sumamonstruos,sumasoldados,ganamonstruos,ganasoldados)
relativamonstruos = ganamonstruos / veces
relativasoldados = ganasoldados / veces

print('Con ',veces,' combates 2 monstruos contra ',numerosoldados, ' soldados sale que los monstruos tienen una frecuencia relativa de:  ',relativamonstruos)
print( 'Los soldados ganan con una frecuencia de: ', relativasoldados)


    
