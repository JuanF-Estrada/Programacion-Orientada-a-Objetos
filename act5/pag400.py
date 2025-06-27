import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        numerador = float(entry_numerador.get())
        denominador = float(entry_denominador.get())

        resultado = numerador / denominador

        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, str(resultado))

    except ZeroDivisionError:
        messagebox.showerror("Error", "Division por cero")
        entry_resultado.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Verifique formato de los datos")
        entry_resultado.delete(0, tk.END)

def borrar():
    entry_numerador.delete(0, tk.END)
    entry_denominador.delete(0, tk.END)
    entry_resultado.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Calculadora")

label_numerador = tk.Label(ventana, text="Numerador")
label_numerador.grid(row=0, column=0, padx=10, pady=10)

label_denominador = tk.Label(ventana, text="Denominador")
label_denominador.grid(row=1, column=0, padx=10, pady=10)

label_resultado = tk.Label(ventana, text="Resultado")
label_resultado.grid(row=2, column=0, padx=10, pady=10)

entry_numerador = tk.Entry(ventana)
entry_numerador.grid(row=0, column=1, padx=10, pady=10)

entry_denominador = tk.Entry(ventana)
entry_denominador.grid(row=1, column=1, padx=10, pady=10)

entry_resultado = tk.Entry(ventana)
entry_resultado.grid(row=2, column=1, padx=10, pady=10)

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.grid(row=3, column=0, padx=10, pady=10)

boton_borrar = tk.Button(ventana, text="Borrar", command=borrar)
boton_borrar.grid(row=3, column=1, padx=10, pady=10)

ventana.mainloop()
