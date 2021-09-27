from ListaNodos import ListaNodos

class Pagina:
    def __init__(self):
        self.raiz = False
        self.tam = 0
        self.claves_max = 4
        self.claves_min = 2
        self.claves = ListaNodos()
    
    def insertar_pagina(self, nuevo):
        if self.claves.insertar(nuevo):
            self.tam = self.claves.size

            if self.tam < 5:
                return self
        return None
    
    def dividir_pagina(self, pag):
        #Si tamaño de nodos es igual a 5, entra en esta funcion
        temp = pag.claves.primero
        for i in range(2):
            temp = temp.siguiente

        primero = pag.claves.primero
        segundo = pag.claves.primero.siguiente