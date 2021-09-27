from nodo_B import NodoB
from Pagina import Pagina

class ArbolB:
    def __init__(self):
        self.raiz = None
        self.orden = 5
        self.altura = 0
    
    def insertar_nodo(self, codigo, nombre, creditos, prerequisitos, obligatorio):
        nuevo = NodoB(codigo, nombre, creditos, prerequisitos, obligatorio)
        if self.raiz == None:
            self.raiz = Pagina()
            self.raiz.raiz = True
            self.raiz = self.raiz.insertar_pagina(nuevo)
            #Se inserta datos nuevo.codigo
        else:
            if self.altura == 0:
                respuesta_insertar = self.raiz.insertar_pagina(nuevo)
                if isinstance(respuesta_insertar, Pagina):
                    self.raiz = respuesta_insertar
                    #Se inserta nodo
                elif isinstance(respuesta_insertar, NodoB):
                    self.altura += 1
                    self.raiz = Pagina()
                    nuevo_raiz = respuesta_insertar
                    self.raiz = self.raiz.insertar_pagina(nuevo_raiz)


