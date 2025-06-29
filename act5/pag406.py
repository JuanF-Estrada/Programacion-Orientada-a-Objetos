import tkinter as tk
from tkinter import messagebox

def verificar_edad(edad):
    try:
        edad = int(edad)
        if edad < 18:
            lbl_mensaje.config(text="El vendedor debe ser mayor de 18 años")
        elif edad > 62:
            lbl_mensaje.config(text="La edad no puede ser mayor a 62 años")
        else:
            lbl_mensaje.config(text="La edad es correcta.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa una edad válida.")
        lbl_mensaje.config(text="La edad no puede ser negativa ni mayor a 62.")

def borrar_campos():
    txt_nombre.delete(0, tk.END)
    txt_apellido.delete(0, tk.END)
    txt_edad.delete(0, tk.END)
    lbl_mensaje.config(text="La edad no puede ser negativa ni mayor a 62.")

def mostrar_datos():
    nombre = txt_nombre.get()
    apellido = txt_apellido.get()
    edad = txt_edad.get()
    
    lbl_nombre.config(text=nombre)
    lbl_apellido.config(text=apellido)
    lbl_edad.config(text=edad)
    
    verificar_edad(edad)

ventana = tk.Tk()
ventana.title("Formulario Vendedor")

lbl_nombre = tk.Label(ventana, text="Nombre")
lbl_nombre.grid(row=0, column=0)
txt_nombre = tk.Entry(ventana)
txt_nombre.grid(row=0, column=1)

lbl_apellido = tk.Label(ventana, text="Apellido")
lbl_apellido.grid(row=1, column=0)
txt_apellido = tk.Entry(ventana)
txt_apellido.grid(row=1, column=1)

lbl_edad = tk.Label(ventana, text="Edad")
lbl_edad.grid(row=2, column=0)
txt_edad = tk.Entry(ventana)
txt_edad.grid(row=2, column=1)

btn_mostrar = tk.Button(ventana, text="Mostrar", command=mostrar_datos)
btn_mostrar.grid(row=3, column=0)

btn_borrar = tk.Button(ventana, text="Borrar", command=borrar_campos)
btn_borrar.grid(row=3, column=1)

lbl_nombre_resultado = tk.Label(ventana, text="Nombre:")
lbl_nombre_resultado.grid(row=4, column=0)
lbl_nombre = tk.Label(ventana, text="")
lbl_nombre.grid(row=4, column=1)

lbl_apellido_resultado = tk.Label(ventana, text="Apellido:")
lbl_apellido_resultado.grid(row=5, column=0)
lbl_apellido = tk.Label(ventana, text="")
lbl_apellido.grid(row=5, column=1)

lbl_edad_resultado = tk.Label(ventana, text="Edad:")
lbl_edad_resultado.grid(row=6, column=0)
lbl_edad = tk.Label(ventana, text="")
lbl_edad.grid(row=6, column=1)

lbl_mensaje = tk.Label(ventana, text="La edad no puede ser negativa ni mayor a 62.")
lbl_mensaje.grid(row=7, column=0, columnspan=2)

ventana.mainloop()
