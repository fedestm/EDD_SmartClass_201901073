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

        tercero = temp.siguiente
        cuarto = pag.claves.ultimo

        primero.siguiente = None
        primero.anterior = None

        segundo.siguiente = None
        segundo.anterior = None

        tercero.siguiente = None
        cuarto.anterior = None

        temp.siguiente = None
        temp.anterior = None

        izquierda = Pagina()
        izquierda.insertar_pagina(primero)
        izquierda.insertar_pagina(segundo)

        derecha = Pagina()
        derecha.insertar_pagina(tercero)
        derecha.insertar_pagina(cuarto)

        temp.izquierda = izquierda
        temp.derecha = derecha

        #Temporal retorna el nodo central temp.codigo
        return temp