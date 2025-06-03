import tkinter as tk
from tkinter import messagebox
import math

class Notas:
    def __init__(self, lista_notas):
        self.lista_notas = lista_notas
    
    def calcular_promedio(self):
        return sum(self.lista_notas) / len(self.lista_notas)
    
    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma = sum((x - prom) ** 2 for x in self.lista_notas)
        return math.sqrt(suma / len(self.lista_notas))
    
    def calcular_menor(self):
        return min(self.lista_notas)
    
    def calcular_mayor(self):
        return max(self.lista_notas)


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.geometry("300x300")
        self.resizable(False, False)

        self.campos_notas = []
        for i in range(5):
            etiqueta = tk.Label(self, text=f"Nota {i+1}:")
            etiqueta.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entrada = tk.Entry(self, width=10)
            entrada.grid(row=i, column=1, padx=10, pady=5)
            self.campos_notas.append(entrada)
        
        boton_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        boton_calcular.grid(row=5, column=0, pady=10)
        
        boton_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
        boton_limpiar.grid(row=5, column=1, pady=10)

   
        self.label_promedio = tk.Label(self, text="Promedio = ")
        self.label_promedio.grid(row=6, column=0, columnspan=2, sticky="w", padx=10)

        self.label_desviacion = tk.Label(self, text="Desviación estándar = ")
        self.label_desviacion.grid(row=7, column=0, columnspan=2, sticky="w", padx=10)

        self.label_mayor = tk.Label(self, text="Valor mayor = ")
        self.label_mayor.grid(row=8, column=0, columnspan=2, sticky="w", padx=10)

        self.label_menor = tk.Label(self, text="Valor menor = ")
        self.label_menor.grid(row=9, column=0, columnspan=2, sticky="w", padx=10)

    def calcular(self):
        try:
            notas = [float(campo.get()) for campo in self.campos_notas]
            vector = Notas(notas)
            promedio = vector.calcular_promedio()
            desviacion = vector.calcular_desviacion()
            mayor = vector.calcular_mayor()
            menor = vector.calcular_menor()

            self.label_promedio.config(text=f"Promedio = {promedio:.2f}")
            self.label_desviacion.config(text=f"Desviación estándar = {desviacion:.2f}")
            self.label_mayor.config(text=f"Valor mayor = {mayor}")
            self.label_menor.config(text=f"Valor menor = {menor}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos en todas las notas.")

    def limpiar(self):
        for campo in self.campos_notas:
            campo.delete(0, tk.END)
        self.label_promedio.config(text="Promedio = ")
        self.label_desviacion.config(text="Desviación estándar = ")
        self.label_mayor.config(text="Valor mayor = ")
        self.label_menor.config(text="Valor menor = ")


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
