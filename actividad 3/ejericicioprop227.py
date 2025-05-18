class Mascota:
    def __init__(self, nombre, edad, color, raza):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.raza = raza

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Color: {self.color}")
        print(f"Raza: {self.raza}")


class Perro(Mascota):
    def __init__(self, nombre, edad, color, peso, muerde, raza):
        super().__init__(nombre, edad, color, raza)
        self.peso = peso
        self.muerde = muerde

    @staticmethod
    def sonido():
        print("Los perros ladran")

    def imprimir(self):
        super().imprimir()
        print(f"Peso: {self.peso} kg")
        print(f"Muerde: {'Sí' if self.muerde else 'No'}")

class PerroPequeno(Perro):
    pass

class PerroMediano(Perro):
    pass

class PerroGrande(Perro):
    pass

class Caniche(PerroPequeno):
    pass

class YorkshireTerrier(PerroPequeno):
    pass

class Schnauzer(PerroPequeno):
    pass

class Chihuahua(PerroPequeno):
    pass


class Collie(PerroMediano):
    pass

class Dalmata(PerroMediano):
    pass

class Bulldog(PerroMediano):
    pass

class Galgo(PerroMediano):
    pass

class Sabueso(PerroMediano):
    pass


class PastorAleman(PerroGrande):
    pass

class Doberman(PerroGrande):
    pass

class Rotweiller(PerroGrande):
    pass



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


class GatoSinPelo(Gato):
    pass

class GatoPeloLargo(Gato):
    pass

class GatoPeloCorto(Gato):
    pass


class Esfinge(GatoSinPelo):
    pass

class Elfo(GatoSinPelo):
    pass

class Donskoy(GatoSinPelo):
    pass


class Angora(GatoPeloLargo):
    pass

class Himalayo(GatoPeloLargo):
    pass

class Balines(GatoPeloLargo):
    pass

class Somali(GatoPeloLargo):
    pass


class AzulRuso(GatoPeloCorto):
    pass

class Britanico(GatoPeloCorto):
    pass

class Manx(GatoPeloCorto):
    pass

class DevonRex(GatoPeloCorto):
    pass


if __name__ == "__main__":
    perros_pequenos = [
        Caniche("Fido", 3, "Blanco", 8, True, "Caniche"),
        YorkshireTerrier("Max", 2, "Negro", 7, False, "Yorkshire Terrier"),
        Schnauzer("Rocky", 4, "Gris", 9, True, "Schnauzer"),
        Chihuahua("Toby", 1, "Marrón", 3, False, "Chihuahua")
    ]

    perros_medianos = [
        Collie("Lassie", 5, "Marrón", 20, False, "Collie"),
        Dalmata("Spot", 3, "Blanco y Negro", 18, True, "Dálmata"),
        Bulldog("Bruno", 6, "Beige", 25, False, "Bulldog"),
        Galgo("Flash", 4, "Marrón", 22, False, "Galgo"),
        Sabueso("Hunter", 7, "Marrón oscuro", 24, True, "Sabueso")
    ]

    perros_grandes = [
        PastorAleman("Rex", 6, "Negro y Marrón", 35, True, "Pastor Alemán"),
        Doberman("Zeus", 5, "Negro", 40, True, "Doberman"),
        Rotweiller("Thor", 4, "Negro y Marrón", 45, True, "Rotweiller")
    ]

    gatos_sin_pelo = [
        Esfinge("Luna", 3, "Beige", 0.6, 1.0, "Esfinge"),
        Elfo("Nina", 2, "Gris", 0.5, 0.9, "Elfo"),
        Donskoy("Milo", 1, "Negro", 0.4, 0.8, "Donskoy")
    ]

    gatos_pelo_largo = [
        Angora("Simba", 4, "Blanco", 0.7, 1.1, "Angora"),
        Himalayo("Maya", 5, "Gris", 0.6, 1.2, "Himalayo"),
        Balines("Coco", 3, "Marrón", 0.5, 1.0, "Balinés"),
        Somali("Leo", 6, "Naranja", 0.8, 1.3, "Somalí")
    ]

    gatos_pelo_corto = [
        AzulRuso("Lilly", 2, "Azul", 0.5, 1.0, "Azul Ruso"),
        Britanico("Oscar", 3, "Beige", 0.4, 0.9, "Británico"),
        Manx("Zoe", 4, "Blanco", 0.6, 1.1, "Manx"),
        DevonRex("Kira", 5, "Gris", 0.7, 1.2, "Devon Rex")
    ]

    print("Datos de Perros Pequeños:")
    for perro in perros_pequenos:
        perro.imprimir()
        perro.sonido()
        print()

    print("Datos de Perros Medianos:")
    for perro in perros_medianos:
        perro.imprimir()
        perro.sonido()
        print()

    print("Datos de Perros Grandes:")
    for perro in perros_grandes:
        perro.imprimir()
        perro.sonido()
        print()

    print("Datos de Gatos Sin Pelo:")
    for gato in gatos_sin_pelo:
        gato.imprimir()
        gato.sonido()
        print()

    print("Datos de Gatos Pelo Largo:")
    for gato in gatos_pelo_largo:
        gato.imprimir()
        gato.sonido()
        print()

    print("Datos de Gatos Pelo Corto:")
    for gato in gatos_pelo_corto:
        gato.imprimir()
        gato.sonido()
        print()