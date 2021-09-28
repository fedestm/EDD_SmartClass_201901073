class ListaCabeceras:
    def __init__(self):
        self.primero = None
    
    def insertar_cabecera(self, nuevo):
        if self.primero:
            if nuevo.posicion < self.primero.posicion:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo