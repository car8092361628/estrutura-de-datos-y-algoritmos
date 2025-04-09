import tkinter as tk
from tkinter import messagebox

def enviar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    correo = entry_correo.get()
    
    if nombre and edad.isdigit() and correo:
        mensaje = f"Nombre: {nombre}\nEdad: {edad}\nCorreo: {correo}"
        messagebox.showinfo("Datos ingresados", mensaje)
    else:
        messagebox.showerror("Error", "Por favor, completa todos los campos correctamente.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Datos")
ventana.geometry("300x250")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Edad:").pack(pady=5)
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Label(ventana, text="Correo:").pack(pady=5)
entry_correo = tk.Entry(ventana)
entry_correo.pack()

# Botón para enviar
tk.Button(ventana, text="Enviar", command=enviar_datos).pack(pady=20)

ventana.mainloop()
