#CRUD
#c=CREAR
#r=REMOVER  
#u=ACTUALIZAR
#d=DESPLEGAR

#creando un diccionario
diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid",
}

#accediendo a un valor
print(diccionario["nombre"])  # Salida: Juan

#modificando un valor
diccionario["edad"]=35

#agregando un nuevo par clave-valor
diccionario["profesion"] = "Ingeniero"

#eliminando un par clave-valor
del diccionario["ciudad"]
del diccionario["edad"]  # Eliminar la clave "edad"

print(diccionario)  # Salida: {'nombre': 'Juan', 'edad': 35, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}


