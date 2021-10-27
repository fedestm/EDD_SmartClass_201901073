from .nodo_simple import NodoSimple

class ListaSimple:
    def __init__(self):
        self.primero = self.ultimo = None
        self.cont = 0
    
    def lista_vacia(self):
        return self.primero == None
    
    def insertar(self, titulo, apunte):
        self.cont += 1
        nuevo = NodoSimple(self.cont, titulo, apunte)
        if self.lista_vacia():
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
    


