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