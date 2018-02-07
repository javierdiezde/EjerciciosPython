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
    
    if sumamonstruos >= sumasoldados:
        ganamonstruos = ganamonstruos + 1
    else:
        ganasoldados = ganasoldados + 1
    print(sumamonstruos,sumasoldados,ganamonstruos,ganasoldados)
relativamonstruos = ganamonstruos / veces
relativasoldados = ganasoldados / veces

print('Con %d combates 2 monstruos contra %e soldados sale que los mosntruos tienen una frecuencia relativa de: ',veces,numerosoldados,relativamonstruos)

    
