class NodoInterno:
    def __init__(self, anterior, siguiente, pos_x, pos_y, cantidad):
        self.anterior = anterior
        self.siguiente = siguiente
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.arriba = None
        self.abajo = None
        self.cantidad = cantidad