#Implementaremos una clase llamada Persona que tendrá como atributo (variable) su nombre 
#y dos métodos (funciones), uno de dichos métodos inicializará
#el atributo nombre y el siguiente método mostrará en la pantalla el contenido del mismo.

class Persona:
    def inicializar(self, nombre):
        self.nombre = nombre
        
    def imprimir(self):
        print("Nombre:", self.nombre)
        
 #bloque de código para probar la clase
 
persona1 = Persona()
persona1.inicializar("Juan")
persona1.imprimir()

persona2 = Persona()
persona2.inicializar("Maria")
persona2.imprimir()