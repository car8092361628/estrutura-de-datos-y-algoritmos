#clase padre
class Animal:
    def __init__(self,nombre):
        self.nombre=nombre
    def hablar(self):
        print(f"{self.nombre} hace un sonido.")
        
#clase hija
class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")
 
class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Miau!")
        
#uso polimorfismo
perro=Perro("Firulais")    
gato=Gato("Michi")   
perro.hablar() 
gato.hablar()

animales=[Perro("Bobby"),Gato("Luna")]
for animal in animales:
    animal.hablar() #cada objeto ejecuta su propia version de hablar()