# Adivina un refrán
from random import randint
import time
refran='tonto el que lo lea'
adivino=''
for i in range(len(refran)):
    adivino +=' '
# print(refran)
print (adivino)
caracteres=len(refran)
print (caracteres)
while adivino!=refran:
    asci=randint(65,122) # caracterees ascii
    time.sleep(.3)
    for i in range(len(refran)):
        
        
        #  print(i, adivino)
        # print (refran[i],chr(asci))
        # print (i,refran[i],chr(asci))
        if refran[i]== chr(asci):
            
            #print(i,adivino[:i])
            #print(chr(asci))
            #print(adivino[i:len(refran)])
            adivino=adivino[:i]+chr(asci)+adivino[i+1:len(refran)]
            #caracteres -=1
    print(adivino,chr(asci))
        #print (i, asci, chr(asci),adivino[i])
    #print (adivino,caracteres)

    
