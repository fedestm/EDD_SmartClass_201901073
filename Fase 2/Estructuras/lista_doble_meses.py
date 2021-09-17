from nodo_doble import NodoDoble_Meses

class ListaDoble_Meses:
    def __init__(self):
        self.primero = self.ultimo = None
    
    def lista_vacia(self):
        return self.primero == None