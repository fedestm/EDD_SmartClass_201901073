from .ArbolB import ArbolB

class NodoSimple_ArbolB:
    def __init__(self, siguiente, cursos):
        self.siguiente = siguiente
        self.cursos = cursos
        self.arbol_pensum = ArbolB()

class ListaSimple_Pensum:
    def __init__(self):
        self.primero = self.ultimo = None
    
    def lista_vacia(self):
        return self.primero == None
    
    def insertar(self, cursos):
        nuevo = NodoSimple_ArbolB(None, cursos)
        if self.lista_vacia():
            print("Lista Vacia")
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
    
    