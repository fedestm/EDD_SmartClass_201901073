from nodo_doble import NodoDoble_Meses

class ListaDoble_Meses:
    def __init__(self):
        self.primero = self.ultimo = None
    
    def lista_vacia(self):
        return self.primero == None

    def insertar(self, mes, tareas):
        nuevo = NodoDoble_Meses(None, None, mes, tareas)
        if self.lista_vacia():
            self.primero = self.ultimo = nuevo