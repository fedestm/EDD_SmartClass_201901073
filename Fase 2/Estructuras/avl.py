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
    def f_equilibrio(self, nodo_avl):
        #Se verifica si existe el nodo
        if nodo_avl:
            return nodo_avl.altura
        else:
            #De lo contrario se retorna -1
            return -1
        

