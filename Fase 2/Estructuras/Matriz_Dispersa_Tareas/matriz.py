from lista_cabeceras import ListaCabeceras
from nodo_cabeceras import NodoCabeceras

class Matriz:
    def __init__(self):
        self.cabeceras_x = ListaCabeceras()
        self.cabeceras_y = ListaCabeceras()
    
    def insertar(self, x, y, cantidad):
        nodo_cabecera_x = None
        nodo_cabecera_y = None

        if self.cabeceras_x and self.cabeceras_y:
            nodo_cabecera_x = self.cabeceras_x.buscar_cabecera(x)
            nodo_cabecera_y = self.cabeceras_y.buscar_cabecera(y)
        
        if nodo_cabecera_x == None:
            nodo_cabecera_x = NodoCabeceras(x)
            self.cabeceras_x.insertar_cabecera(nodo_cabecera_x)
        
        if nodo_cabecera_y == None:
            nodo_cabecera_y = NodoCabeceras(y)
            self.cabeceras_y.insertar_cabecera(nodo_cabecera_y)
        
        nodo_cabecera_x.lista_interna.insertar_posx(x, y, cantidad)
        nodo_cabecera_y.lista_interna.insertar_posy(x, y, cantidad)
