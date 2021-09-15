from nodo_avl import nodo_avl

class avl:
    def __init__(self):
        self.raiz=None

    #Retornar fase de equilibrio mayor
    #Se cuentan la cantidad de saltos a la derecha y el mas grande es el que retorna
    def maximo(self,a1,a2):
        if a1>a2:
            return a1
        else:
            return a2
    
    #Retorna fase de equilibrio de nodo
    #O altura
    def f_equilibrio(self, nodo_avl):
        #Se verifica si existe el nodo
        if nodo_avl:
            return nodo_avl.altura
        else:
            #De lo contrario se retorna -1
            return -1

    #Rotaciones
    #Simple Izquierda
    def R_izquierda(self, nodo_avl):
        aux = nodo_avl.izquierda
        nodo_avl.izquierda = aux.derecha
        aux.derecha = nodo_avl
        nodo_avl.altura = self.maximo(self.f_equilibrio(nodo_avl.derecha) , self.f_equilibrio(nodo_avl.izquierda)) + 1
        aux.altura = self.maximo(nodo_avl.altura, self.f_equilibrio(nodo_avl.izquierda)) + 1
        return aux




