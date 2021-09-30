from .ArbolB import ArbolB

class Nodo_Simple:
    def __init__(self,siguiente, semestre):
        self.siguiente = siguiente
        self.semestre = semestre
        self.arbol_cursos = ArbolB()