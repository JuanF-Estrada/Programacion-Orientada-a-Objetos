class Mascota:
    def __init__(self, nombre, edad, color, raza):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.raza = raza

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Color: {self.color}")
        print(f"Raza: {self.raza}")


class Perro(Mascota):
    def __init__(self, nombre, edad, color, peso, muerde, raza, tamaño):
        super().__init__(nombre, edad, color, raza)
        self.peso = peso
        self.muerde = muerde
        self.tamaño = tamaño

    @staticmethod
    def sonido():
        print("Los perros ladran")

    def imprimir(self):
        super().imprimir()
        print(f"Tamaño: {self.tamaño}")
        print(f"Peso: {self.peso} kg")
        print(f"Muerde: {'Sí' if self.muerde else 'No'}")


class Gato(Mascota):
    def __init__(self, nombre, edad, color, altura_salto, longitud_salto, raza):
        super().__init__(nombre, edad, color, raza)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto

    @staticmethod
    def sonido():
        print("Los gatos maúllan y ronronean")

    def imprimir(self):
        super().imprimir()
        print(f"Altura de salto: {self.altura_salto} m")
        print(f"Longitud de salto: {self.longitud_salto} m")


# Diccionarios de razas y tamaños
razas_perro = {
    "Caniche": "Pequeño",
    "Yorkshire Terrier": "Pequeño",
    "Schnauzer": "Pequeño",
    "Chihuahua": "Pequeño",
    "Collie": "Mediano",
    "Dálmata": "Mediano",
    "Bulldog": "Mediano",
    "Galgo": "Mediano",
    "Sabueso": "Mediano",
    "Pastor Alemán": "Grande",
    "Doberman": "Grande",
    "Rotweiller": "Grande"
}

razas_gato = [
    "Esfinge", "Elfo", "Donskoy",
    "Angora", "Himalayo", "Balinés", "Somalí",
    "Azul Ruso", "Británico", "Manx", "Devon Rex"
]


def seleccionar_raza_perro():
    print("\nSeleccione una raza de perro:")
    razas = list(razas_perro.keys())
    for idx, raza in enumerate(razas, start=1):
        print(f"{idx}. {raza}")
    while True:
        try:
            opcion = int(input("Ingrese el número de la raza: "))
            if 1 <= opcion <= len(razas):
                raza = razas[opcion - 1]
                tamaño = razas_perro[raza]
                return raza, tamaño
            else:
                print("Número fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")


def seleccionar_raza_gato():
    print("\nSeleccione una raza de gato:")
    for idx, raza in enumerate(razas_gato, start=1):
        print(f"{idx}. {raza}")
    while True:
        try:
            opcion = int(input("Ingrese el número de la raza: "))
            if 1 <= opcion <= len(razas_gato):
                return razas_gato[opcion - 1]
            else:
                print("Número fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")


def crear_perro():
    print("\n--- Ingreso de datos para un Perro ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    color = input("Color: ")
    raza, tamaño = seleccionar_raza_perro()
    peso = float(input("Peso (kg): "))
    muerde_input = input("¿Muerde? (s/n): ").lower()
    muerde = muerde_input == 's'
    perro = Perro(nombre, edad, color, peso, muerde, raza, tamaño)
    print("\n--- Información del Perro ---")
    perro.imprimir()
    perro.sonido()


def crear_gato():
    print("\n--- Ingreso de datos para un Gato ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    color = input("Color: ")
    raza = seleccionar_raza_gato()
    altura_salto = float(input("Altura de salto (m): "))
    longitud_salto = float(input("Longitud de salto (m): "))
    gato = Gato(nombre, edad, color, altura_salto, longitud_salto, raza)
    print("\n--- Información del Gato ---")
    gato.imprimir()
    gato.sonido()


if __name__ == "__main__":
    while True:
        print("\n¿Qué tipo de mascota deseas ingresar?")
        print("1. Perro")
        print("2. Gato")
        print("3. Salir")

        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            crear_perro()
        elif opcion == "2":
            crear_gato()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
