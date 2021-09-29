from ArbolB.ArbolB import ArbolB

class Nodo_Simple:
    def __init__(self,siguiente, semestre, cursos):
        self.siguiente = siguiente
        self.semestre = semestre
        self.cursos = cursos
        self.arbol_cursos = ArbolB()