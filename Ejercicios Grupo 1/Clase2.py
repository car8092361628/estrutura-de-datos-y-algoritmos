#Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. 
#Definir los métodos para inicializar sus atributos,
#imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)

class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)
    def Mostrar_estado(self):
        if self.nota >= 4:
            print("El alumno está regular")
        else:
            print("El alumno no está regular")
    
    #bloque de código para probar la clase    
alumno1 = Alumno()
alumno1.inicializar("Juan", 5)  
alumno1.imprimir()
alumno1.Mostrar_estado()

alumno2 = Alumno()
alumno2.inicializar("Maria", 3) 
alumno2.imprimir()
alumno2.Mostrar_estado()

        
