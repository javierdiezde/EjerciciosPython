#Averigua si un número es primo

while True:
	a = input('Introduce un número entero')
	try:
		a = int(a)
		break
	except ValueError:
		print ("debes introducir un número entero")

mitad = int(a/2) +1
for divisor in range(2,mitad):
    if a%divisor==0:
        print(' no es primo, es divisible por: ')
        print (divisor)
        esprimo = 0
        break
    else:
        esprimo=1
    
if esprimo !=0:
    print ('Efectivamente es un número primo')
