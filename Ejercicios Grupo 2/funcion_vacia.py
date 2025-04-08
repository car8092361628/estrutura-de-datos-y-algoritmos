def mostrar_mensaje(mensaje):
    print("**********************************")
    print(mensaje)
    print("**********************************")
    
def Cargar_suma():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el segundo valor: "))
    suma=valor1+valor2
    mostrar_mensaje("La suma es: " + str(suma))
    
#programa principal
mostrar_mensaje("El programa ha comenzado")
Cargar_suma()
mostrar_mensaje("Gracias por usar el programa")
mostrar_mensaje("El programa ha terminado")

    