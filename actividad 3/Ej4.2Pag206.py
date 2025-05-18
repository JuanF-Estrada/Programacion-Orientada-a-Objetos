class Inmueble:
    def __init__(self, identificador_inmobiliario, area, direccion):
        self._identificador_inmobiliario = identificador_inmobiliario  # protegido
        self._area = area
        self._direccion = direccion
        self._precio_venta = 0

    def calcular_precio_venta(self, valor_area):
        self._precio_venta = self._area * valor_area
        return self._precio_venta

    def imprimir(self):
        print(f"Identificador inmobiliario = {self._identificador_inmobiliario}")
        print(f"Area = {self._area}")
        print(f"Dirección = {self._direccion}")
        print(f"Precio de venta = ${self._precio_venta:,.0f}")

class InmuebleVivienda(Inmueble):
    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_baños):
        super().__init__(identificador_inmobiliario, area, direccion)
        self._numero_habitaciones = numero_habitaciones
        self._numero_baños = numero_baños

    def imprimir(self):
        super().imprimir()
        print(f"Número de habitaciones = {self._numero_habitaciones}")
        print(f"Número de baños = {self._numero_baños}")

class CasaRural(InmuebleVivienda):
    valor_area = 1500000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_baños, numero_pisos, distancia_cabecera, altitud):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_baños)
        self._numero_pisos = numero_pisos
        self._distancia_cabecera = distancia_cabecera
        self._altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos = {self._numero_pisos}")
        print(f"Distancia a cabecera municipal = {self._distancia_cabecera} km")
        print(f"Altitud sobre el nivel del mar = {self._altitud} metros")
        print()

class CasaConjuntoCerrado(InmuebleVivienda):
    valor_area = 2500000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_baños, numero_pisos, valor_administracion, tiene_piscina, tiene_campos_deportivos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_baños)
        self._numero_pisos = numero_pisos
        self._valor_administracion = valor_administracion
        self._tiene_piscina = tiene_piscina
        self._tiene_campos_deportivos = tiene_campos_deportivos

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos = {self._numero_pisos}")
        print(f"Valor de la administración = ${self._valor_administracion}")
        print(f"Tiene piscina? {'Sí' if self._tiene_piscina else 'No'}")
        print(f"Tiene campos deportivos? {'Sí' if self._tiene_campos_deportivos else 'No'}")
        print()

class CasaIndependiente(InmuebleVivienda):
    valor_area = 3000000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_baños, numero_pisos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_baños)
        self._numero_pisos = numero_pisos

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos = {self._numero_pisos}")
        print()

class Apartaestudio(InmuebleVivienda):
    valor_area = 1500000

    def __init__(self, identificador_inmobiliario, area, direccion):
        # Apartaestudio siempre 1 hab y 1 baño
        super().__init__(identificador_inmobiliario, area, direccion, 1, 1)

    def imprimir(self):
        super().imprimir()
        print()

class ApartamentoFamiliar(InmuebleVivienda):
    valor_area = 2000000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_baños, valor_administracion):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_baños)
        self._valor_administracion = valor_administracion

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = ${self._valor_administracion}")
        print()

class Local:
    valor_area = None  # Se define en subclases

    def __init__(self, identificador_inmobiliario, area, direccion, tipo):
        self._identificador_inmobiliario = identificador_inmobiliario
        self._area = area
        self._direccion = direccion
        self._tipo = tipo  # Interno o Calle
        self._precio_venta = 0

    def calcular_precio_venta(self, valor_area):
        self._precio_venta = self._area * valor_area
        return self._precio_venta

    def imprimir(self):
        print(f"Identificador inmobiliario = {self._identificador_inmobiliario}")
        print(f"Area = {self._area}")
        print(f"Dirección = {self._direccion}")
        print(f"Tipo de local = {self._tipo}")
        print(f"Precio de venta = ${self._precio_venta:,.0f}")

class LocalComercial(Local):
    valor_area = 3000000

    def __init__(self, identificador_inmobiliario, area, direccion, tipo, centro_comercial):
        super().__init__(identificador_inmobiliario, area, direccion, tipo)
        self._centro_comercial = centro_comercial

    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial = {self._centro_comercial}")
        print()

class Oficina(Local):
    valor_area = 3500000

    def __init__(self, identificador_inmobiliario, area, direccion, tipo, es_gobierno):
        super().__init__(identificador_inmobiliario, area, direccion, tipo)
        self._es_gobierno = es_gobierno

    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental = {'Sí' if self._es_gobierno else 'No'}")
        print()

# Ejemplo de uso
if __name__ == "__main__":
    apto_familiar = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
    apto_familiar.calcular_precio_venta(ApartamentoFamiliar.valor_area)
    print("Datos apartamento familiar:")
    apto_familiar.imprimir()

    apta_estudio = Apartaestudio(12354, 50, "Avenida Caracas 30-15")
    apta_estudio.calcular_precio_venta(Apartaestudio.valor_area)
    print("Datos apartaestudio:")
    apta_estudio.imprimir()

    casa_rural = CasaRural(98765, 150, "Camino Rural 12-34", 4, 3, 2, 20, 1500)
    casa_rural.calcular_precio_venta(CasaRural.valor_area)
    print("Datos casa rural:")
    casa_rural.imprimir()

    casa_conjunto = CasaConjuntoCerrado(11223, 100, "Conjunto Cerrado 56-78", 3, 2, 2, 350000, True, True)
    casa_conjunto.calcular_precio_venta(CasaConjuntoCerrado.valor_area)
    print("Datos casa conjunto cerrado:")
    casa_conjunto.imprimir()

    casa_indep = CasaIndependiente(44556, 130, "Independiente 90-12", 4, 3, 3)
    casa_indep.calcular_precio_venta(CasaIndependiente.valor_area)
    print("Datos casa independiente:")
    casa_indep.imprimir()

    local_comercial = LocalComercial(77889, 80, "Centro Comercial 5-10", "INTERNO", "Mall Plaza")
    local_comercial.calcular_precio_venta(LocalComercial.valor_area)
    print("Datos local comercial:")
    local_comercial.imprimir()

    oficina = Oficina(33445, 60, "Edificio Gobierno 3-5", "CALLE", True)
    oficina.calcular_precio_venta(Oficina.valor_area)
    print("Datos oficina:")
    oficina.imprimir()