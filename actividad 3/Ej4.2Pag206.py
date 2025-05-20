from enum import Enum

class Inmueble:
    def __init__(self, identificadorInmobiliario, area, direccion):
        self.identificadorInmobiliario = identificadorInmobiliario
        self.area = area
        self.direccion = direccion
        self.precioVenta = 0.0

    def calcularPrecioVenta(self, valorArea):
        self.precioVenta = self.area * valorArea
        return self.precioVenta

    def imprimir(self):
        print(f"Identificador inmobiliario = {self.identificadorInmobiliario}")
        print(f"Area = {self.area}")
        print(f"Dirección = {self.direccion}")
        print(f"Precio de venta = ${self.precioVenta:.1E}")

class InmuebleVivienda(Inmueble):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos):
        super().__init__(identificadorInmobiliario, area, direccion)
        self.numeroHabitaciones = numeroHabitaciones
        self.numeroBanos = numeroBanos

    def imprimir(self):
        super().imprimir()
        print(f"Número de habitaciones = {self.numeroHabitaciones}")
        print(f"Número de baños = {self.numeroBanos}")

class Apartamento(InmuebleVivienda):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos)

    def imprimir(self):
        super().imprimir()

class ApartamentoFamiliar(Apartamento):
    valorArea = 2000000
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, valorAdministracion):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos)
        self.valorAdministracion = valorAdministracion

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = ${self.valorAdministracion}")
        print()

class Apartaestudio(Apartamento):
    valorArea = 1500000
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos):
        super().__init__(identificadorInmobiliario, area, direccion, 1, 1)

    def imprimir(self):
        super().imprimir()
        print()

class Casa(InmuebleVivienda):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos)
        self.numeroPisos = numeroPisos

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos = {self.numeroPisos}")

class CasaRural(Casa):
    valorArea = 1500000
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos, distanciaCabera, altitud):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos)
        self.distanciaCabera = distanciaCabera
        self.altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Distancia la cabecera municipal = {self.numeroHabitaciones} km.")
        print(f"Altitud sobre el nivel del mar = {self.altitud} metros.")
        print()

class CasaUrbana(Casa):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos)

    def imprimir(self):
        super().imprimir()

class CasaConjuntoCerrado(CasaUrbana):
    valorArea = 2500000
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos, valorAdministracion, tienePiscina, tieneCamposDeportivos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos)
        self.valorAdministracion = valorAdministracion
        self.tienePiscina = tienePiscina
        self.tieneCamposDeportivos = tieneCamposDeportivos

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = {self.valorAdministracion}")
        print(f"Tiene piscina? = {self.tienePiscina}")
        print(f"Tiene campos deportivos? = {self.tieneCamposDeportivos}")
        print()

class CasaIndependiente(CasaUrbana):
    valorArea = 3000000
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos)

    def imprimir(self):
        super().imprimir()
        print("")

class Local(Inmueble):
    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal):
        super().__init__(identificadorInmobiliario, area, direccion)
        self.tipoLocal = tipoLocal

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local = {self.tipoLocal}")

class LocalComercial(Local):
    valorArea = 3000000
    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal, centroComercial):
        super().__init__(identificadorInmobiliario, area, direccion, tipoLocal)
        self.centroComercial = centroComercial

    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial = {self.centroComercial}")
        print()

class Oficina(Local):
    valorArea = 3500000
    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal, esGobierno):
        super().__init__(identificadorInmobiliario, area, direccion, tipoLocal)
        self.esGobierno = esGobierno

    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental = {self.esGobierno}")
        print()

class Tipo(Enum):
    INTERNO = "INTERNO"
    CALLE = "CALLE"

if __name__ == "__main__":
    print("Datos apartamento")
    apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
    apto1.calcularPrecioVenta(ApartamentoFamiliar.valorArea)
    apto1.imprimir()

    print("Datos apartamento")
    aptestudio1 = Apartaestudio(12354, 50, "Avenida Caracas 30-15", 1, 1)
    aptestudio1.calcularPrecioVenta(Apartaestudio.valorArea)
    aptestudio1.imprimir()