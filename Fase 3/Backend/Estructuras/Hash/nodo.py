from typing import List
from .Lista_Simple import ListaSimple
from .lista_doble_anios import ListaDoble_Anios

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
        self.lista_anios = ListaDoble_Anios()