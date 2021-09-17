from nodo_simple import Nodo_Simple

class ListaSimple:
    def __init__(self):
        self.primero = self.ultimo = None
    
    def lista_vacia(self):
        return self.primero == None
    
    def insertar(self, semestre, cursos):
        if lista_vacia():
            self.primero = self.ultimo = Nodo_Simple(None, semestre, cursos)
    