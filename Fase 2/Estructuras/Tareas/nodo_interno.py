from .lista_doble_tareas import ListaDoble_Tareas

class NodoInterno:
    def __init__(self, pos_x, pos_y, cantidad):
        self.anterior = None
        self.siguiente = None
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.arriba = None
        self.abajo = None
        self.cantidad = cantidad
        self.lista_tareas = ListaDoble_Tareas()