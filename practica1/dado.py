import random as rd

dado1=rd.randint(1,6)
dado2=rd.randint(1,6)

print("Primer dado: ",dado1)
print("Segundo dado: ",dado2)

suma=dado1+dado2

if suma==8  & suma==12 :
    print("El cliente es tuyo.")
else:
    print("El cliente es mio.")