from .nodo_B import NodoB
from .Pagina import Pagina
import os

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
            else:
                respuesta_insertar = self.recorrer_insertar(nuevo, self.raiz)
                if isinstance(respuesta_insertar, NodoB):
                    #Se retorna nodo a la raiz
                    self.altura += 1
                    self.raiz = Pagina()
                    self.raiz.insertar_pagina(respuesta_insertar)
                else:
                    #Se retorna una pagina a la raiz
                    self.raiz = respuesta_insertar

    def recorrer_insertar(self, nuevo, raiz_actual):
        if raiz_actual.hoja(raiz_actual):
            #Se valida que es hoja
            respuesta_insertar = raiz_actual.insertar_pagina(nuevo)
            return respuesta_insertar
        else:
            #De lo contrario no es hoja
            if nuevo.codigo < raiz_actual.claves.primero.codigo:
                #Ingresa por la izquierda
                respuesta_insertar = self.recorrer_insertar(nuevo, raiz_actual.claves.primero.izquierda)
                if isinstance(respuesta_insertar, NodoB):
                    #Se retorna nodo
                    return raiz_actual.insertar_pagina(respuesta_insertar)
                else:
                    #Se retorna una pagina
                    raiz_actual.claves.primero.izquierda = respuesta_insertar
                    return raiz_actual
            elif nuevo.codigo > raiz_actual.claves.ultimo.codigo:
                #Ingresa el ultimo nodo
                respuesta_insertar = self.recorrer_insertar(nuevo, raiz_actual.claves.ultimo.derecha)
                if isinstance(respuesta_insertar, NodoB):
                    #Retorna un nodo
                    return raiz_actual.insertar_pagina(respuesta_insertar)
                else:
                    #Retorna una pagina
                    raiz_actual.claves.ultimo.derecha = respuesta_insertar
                    return raiz_actual
            else:
                pivote = raiz_actual.claves.primero

                while pivote != None:
                    if nuevo.codigo < pivote.codigo:
                        respuesta_insertar = self.recorrer_insertar(nuevo, pivote.izquierda)
                        if isinstance(respuesta_insertar, NodoB):
                            return raiz_actual.insertar_pagina(respuesta_insertar)
                        else:
                            pivote.izquierda = respuesta_insertar
                            pivote.anterior.derecha = respuesta_insertar
                            return raiz_actual
                    elif nuevo.codigo == pivote.codigo:
                        return raiz_actual
                    else:
                        pivote = pivote.siguiente
        return self
    
    def graficar(self):
        file = open("arbolB.dot", "w")
        dot = "digraph arbolB{\n"
        dot += "rankdir=TB;\n"
        dot += "node [shape = box, fillcolor=\"#F2F3F4\" color=\"black\" style=\"filled\"];\n"
        dot += self.graficar_nodos(self.raiz)
        dot += self.graficar_enlaces(self.raiz)
        dot += "\n}\n"
        file.write(dot)
        file.close()
        os.system("dot -Tsvg arbolB.dot -o arbolB.svg")
        os.startfile("arbolB.svg")
    
    def graficar_nodos(self, raiz_actual):
        dot = ""
        if raiz_actual.hoja(raiz_actual):
            dot += "node[shape=record label= \"<p0>"
            cont = 0
            pivote = raiz_actual.claves.primero
            while pivote != None:
                cont += 1
                dot += "|{" + str(pivote.codigo) + "}|<p" + str(cont) + "> "
                pivote = pivote.siguiente
            dot += "\"]" + str(raiz_actual.claves.primero.codigo) + "; \n"
            return dot
        else:
            dot += "node[shape=record label= \"<p0>"
            cont = 0
            pivote = raiz_actual.claves.primero
            while pivote != None:
                cont += 1
                dot += "|{" + str(pivote.codigo) + "}|<p" + str(cont) + "> "
                pivote = pivote.siguiente
            dot += "\"]" + str(raiz_actual.claves.primero.codigo) + "; \n"

            pivote = raiz_actual.claves.primero
            cont = 0
            while pivote != None:
                dot += self.graficar_nodos(pivote.izquierda)
                cont += 1
                pivote = pivote.siguiente
            dot += self.graficar_nodos(raiz_actual.claves.ultimo.derecha)
            return dot
    
    def graficar_enlaces(self, raiz_actual):
        dot = ""
        if raiz_actual.hoja(raiz_actual):
            return str(raiz_actual.claves.primero.codigo) + ";"
        else:
            dot += str(raiz_actual.claves.primero.codigo) + ";"
            pivote = raiz_actual.claves.primero
            cont = 0
            r_actual = str(raiz_actual.claves.primero.codigo)
            while pivote != None:
                dot += "\n" + r_actual + ":p" + str(cont) + "->" + str(self.graficar_enlaces(pivote.izquierda))
                cont += 1
                pivote = pivote.siguiente
            dot += "\n" + r_actual + ":p" + str(cont) + "->" + str(self.graficar_enlaces(raiz_actual.claves.ultimo.derecha))
            return dot
