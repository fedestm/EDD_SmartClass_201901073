from .lista_simple import ListaSimple
from .lista_doble_meses import ListaDoble_Meses

class NodoDoble_Anios:
    def __init__(self, anterior, siguiente, anio):
        self.anio = anio
        self.anterior = anterior
        self.siguiente = siguiente
        self.lista_semestres = ListaSimple()
        self.lista_meses = ListaDoble_Meses()