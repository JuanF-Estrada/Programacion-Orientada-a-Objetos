class Persona:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion

    def getNombre(self) -> str:
        return self.nombre

    def getDireccion(self) -> str:
        return self.direccion

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def setDireccion(self, direccion: str):
        self.direccion = direccion


class Estudiante(Persona):
    def __init__(self, nombre: str, direccion: str, carrera: str, semestre: int):
        super().__init__(nombre, direccion)
        self.carrera = carrera
        self.semestre = semestre

    def getCarrera(self) -> str:
        return self.carrera

    def getSemestre(self) -> int:
        return self.semestre

    def setCarrera(self, carrera: str):
        self.carrera = carrera

    def setSemestre(self, semestre: int):
        self.semestre = semestre


class Profesor(Persona):
    def __init__(self, nombre: str, direccion: str, departamento: str, categoria: str):
        super().__init__(nombre, direccion)
        self.departamento = departamento
        self.categoria = categoria

    def getDepartamento(self) -> str:
        return self.departamento

    def getCategoria(self) -> str:
        return self.categoria

    def setDepartamento(self, departamento: str):
        self.departamento = departamento

    def setCategoria(self, categoria: str):
        self.categoria = categoria


def ingresar_datos_estudiante():
    print("Ingrese datos del estudiante:")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    carrera = input("Carrera: ")
    semestre = int(input("Semestre: "))
    return Estudiante(nombre, direccion, carrera, semestre)


def ingresar_datos_profesor():
    print("Ingrese datos del profesor:")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    departamento = input("Departamento: ")
    categoria = input("Categoría: ")
    return Profesor(nombre, direccion, departamento, categoria)


def imprimir_estudiante(estudiante: Estudiante):
    print("\nDatos del Estudiante:")
    print(f"Nombre: {estudiante.getNombre()}")
    print(f"Dirección: {estudiante.getDireccion()}")
    print(f"Carrera: {estudiante.getCarrera()}")
    print(f"Semestre: {estudiante.getSemestre()}")


def imprimir_profesor(profesor: Profesor):
    print("\nDatos del Profesor:")
    print(f"Nombre: {profesor.getNombre()}")
    print(f"Dirección: {profesor.getDireccion()}")
    print(f"Departamento: {profesor.getDepartamento()}")
    print(f"Categoría: {profesor.getCategoria()}")


if __name__ == "__main__":
    estudiante = ingresar_datos_estudiante()
    profesor = ingresar_datos_profesor()

    imprimir_estudiante(estudiante)
    imprimir_profesor(profesor)