#Confeccionar una clase que represente un empleado. Definir como atributos su nombre y su sueldo.
#En el método __init__ cargar los atributos por teclado y luego en otro método imprimir sus datos
#y por último uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a $3000).add()

class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))
    
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Sueldo:", self.sueldo)
        
    def pagar_impuesto(self):
        if self.sueldo > 3000:
            print("El empleado debe pagar impuestos")
        else:
            print("El empleado no debe pagar impuestos")
            
#bloque de código para probar la clase
empleado1 = Empleado()
empleado1.imprimir()
empleado1.pagar_impuesto()    

empreado2 = Empleado()
empreado2.imprimir()    
empreado2.pagar_impuesto()
