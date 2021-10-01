from .ArbolB import ArbolB

class NodoSimple_ArbolB:
    def __init__(self, siguiente, cursos):
        self.siguiente = siguiente
        self.cursos = cursos
        self.arbol_pensum = ArbolB()

class ListaSimple_Pensum:
    def __init__(self):
        self.primero = self.ultimo = None
    
    