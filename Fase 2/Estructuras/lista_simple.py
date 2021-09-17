from nodo_simple import Nodo_Simple

class ListaSimple:
    def __init__(self):
        self.primero = self.ultimo = None
    
    def lista_vacia(self):
        return self.primero == None
    
    def insertar(self, semestre, cursos):
        nuevo = Nodo_Simple(None, semestre, cursos)
        if self.lista_vacia():
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo