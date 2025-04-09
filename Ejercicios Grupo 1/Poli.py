# Clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} hace un sonido.")

# Clase hija
class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")

# Clase hija
class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Miau!")

# Uso
perro = Perro("Firulais")
gato = Gato("Michi")

perro.hablar()
gato.hablar()

#polimorfismo
animales = [Perro("Bobby"), Gato("Luna")]

for animal in animales:
    animal.hablar()  # Cada objeto ejecuta su propia versión de hablar()