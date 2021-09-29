from lista_interna import Lista_Interna

class NodoCabeceras:
    def __init__(self, posicion):
        self.siguiente = None
        self.anterior = None
        self.posicion = posicion
        self.lista_interna = Lista_Interna()
