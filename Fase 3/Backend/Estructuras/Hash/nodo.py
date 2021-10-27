from .Lista_Simple import ListaSimple

class Nodo:
    def __init__(self, carnet, dpi, nombre, carrera, correo, password, edad):
        self.carnet = carnet
        self.dpi = dpi
        self.nombre = nombre
        self.carrera = carrera
        self.correo = correo
        self.password = password
        self.edad = edad
        self.lista_apuntes = ListaSimple()