#CLASE PADRE
import tkinter as tk #importamo la biblioteca tkinter como tk
from tkinter import messagebox #importamos el modulo messagebox de tkinter

def saludar():#definimos la funcion saludar
    messagebox.showinfo("Saludo", "¡Hola, Mundo!") #mostramos un mensaje de saludo en una ventana emergente
    #messagebox es un modulo de tkinter que permite mostrar mensajes emergentes
 
 #CLASE HIJA
# Crear la ventana principal
ventana=tk.Tk() #creamos una ventana principal
ventana.title("Mi primera GUI")
ventana.geometry("300x200") #definimos el tamaño de la ventana

#crear un boton

boton =tk.Button(ventana, text="Saludar", command=saludar)
#creamos un boton con el texto "Saludar" y le asignamos la funcion saludar como comando
boton.pack(pady=20) #colocamos el boton en la ventana y le damos un margen vertical de 20 pixeles

#iniciar aplicacion
ventana.mainloop() #iniciamos el bucle principal de la aplicacion, lo que permite que la ventana permanezca abierta y responda a eventos



    
    