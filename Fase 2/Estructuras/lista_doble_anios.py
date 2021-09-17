from nodo_doble import NodoDoble_Anios

class ListaDoble_Anios:
    def __init__(self):
        self.primero = self.ultimo = None
    
    def lista_vacia(self):
        return self.primero == None
    
    def insertar(self, anio, semestre, meses):
        nuevo = NodoDoble_Anios(None, None, anio, semestre, meses)
        if lista_vacia():
            self.primero = self.ultimo = nuevo