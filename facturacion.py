import tkinter as tk
from tkinter import messagebox

def registrar_cliente():
    nombre = entry_nombre.get()
    if nombre:
        lista_clientes.insert(tk.END, nombre)
        entry_nombre.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Ingrese un nombre válido")

def agregar_producto():
    producto = entry_producto.get()
    precio = entry_precio.get()
    if producto and precio.isdigit():
        lista_productos.insert(tk.END, f"{producto} - ${precio}")
        entry_producto.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Ingrese datos válidos")

def calcular_total():
    total = 0
    for item in lista_productos.get(0, tk.END):
        precio = int(item.split("$")[-1])
        total += precio
    label_total.config(text=f"Total: ${total}")

def cobrar():
    if lista_productos.size() > 0:
        messagebox.showinfo("Cobro Exitoso", "El pago ha sido realizado")
        lista_productos.delete(0, tk.END)
        label_total.config(text="Total: $0")
    else:
        messagebox.showwarning("Error", "No hay productos para cobrar")

root = tk.Tk()
root.title("Sistema de Ventas")
root.geometry("400x500")

# Registro de Clientes
tk.Label(root, text="Registrar Cliente").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()
tk.Button(root, text="Registrar", command=registrar_cliente).pack()
lista_clientes = tk.Listbox(root)
lista_clientes.pack()

# Agregar Productos
tk.Label(root, text="Producto").pack()
entry_producto = tk.Entry(root)
entry_producto.pack()
tk.Label(root, text="Precio").pack()
entry_precio = tk.Entry(root)
entry_precio.pack()
tk.Button(root, text="Agregar", command=agregar_producto).pack()
lista_productos = tk.Listbox(root)
lista_productos.pack()

# Total y Cobro
label_total = tk.Label(root, text="Total: $0")
label_total.pack()
tk.Button(root, text="Calcular Total", command=calcular_total).pack()
tk.Button(root, text="Cobrar", command=cobrar).pack()

root.mainloop()
