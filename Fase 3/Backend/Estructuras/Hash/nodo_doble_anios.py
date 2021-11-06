from .lista_simple_semestre import ListaSimple

class NodoDoble_Anios:
    def __init__(self, anterior, siguiente, anio):
        self.anio = anio
        self.anterior = anterior
        self.siguiente = siguiente
        self.lista_semestres = ListaSimple()