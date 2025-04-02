##Definir una lista que almacene 5 enteros.
# Sumar todos sus elementos y mostrar dicha suma

#lista=[10,20,30,40,50]
#sumar todos lo elementos de la lista
#sumatotal=sum(lista)
#print("La suma de los elemento de la lista es:",sumatotal)

lista=[10,20,30,40,50]
suma=0
x=0
while x<len(lista):
    suma=suma+lista[x]
    x+=1
    print("Los elementos de la lista son: ")
    print(lista)
    print("La suma de todos sus elemento es: ")
    print(suma)
