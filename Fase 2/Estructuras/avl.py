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
    
    #Rotacion Simple derecha
    def R_derecha(self, nodo_avl):
        aux = nodo_avl.derecha
        nodo_avl.derecha = nodo_avl.izquierda
        aux.izquierda = nodo_avl
        nodo_avl.altura = self.maximo(self.f_equilibrio(nodo_avl.derecha) , self.f_equilibrio(nodo_avl.izquierda)) + 1
        aux.altura = self.maximo(nodo_avl.altura, self.f_equilibrio(nodo_avl.derecha)) + 1
        return aux
    
    #Rotacion Izquierda -> Derecha
    def R_izq_der(self, nodo_avl):
        nodo_avl.izquierda = self.R_derecha(nodo_avl.izquierda)
        aux = self.R_izquierda(nodo_avl)
        return aux
    
    #Rotacion Derecha -> Izquierda
    def R_der_izq(self, nodo_avl):
        nodo_avl.derecha = self.R_izquierda(nodo_avl.derecha)
        aux = self.R_izquierda(nodo_avl)
        return aux
    
    def insertar_nodo(self, nuevo, raiz_actual):
        #Se valida si existe una raiz
        if raiz_actual:
            #Se utiliza carnet para comparar la raiz
            if raiz_actual.carnet > nuevo.carnet:
                raiz_actual.izquierda = self.insertar_nodo(nuevo, raiz_actual.izquierda)
                #Se verifica si necesita rotaciones
                if (self.f_equilibrio(raiz_actual.derecha) - self.f_equilibrio(raiz_actual.izquierda) == -2):
                    if nuevo.carnet < raiz_actual.izquierda.carnet:
                        raiz_actual = self.R_izquierda(raiz_actual)
                    else:
                        raiz_actual = self.R_izq_der(raiz_actual)
            
            elif raiz_actual.carnet < nuevo.carnet:
                raiz_actual.derecha = self.insertar_nodo(nuevo,raiz_actual.derecha)
                if (self.f_equilibrio(raiz_actual.derecha) - self.f_equilibrio(raiz_actual.izquierda) == 2):
                    if nuevo.carnet > raiz_actual.derecha.carnet:
                        raiz_actual = self.R_derecha(raiz_actual)
                    else:
                        raiz_actual = self.R_der_izq(raiz_actual)

            #Se calcula nueva altua
            #Fase de equilibrio
            raiz_actual.altura = self.maximo(self.f_equilibrio(raiz_actual.derecha), self.f_equilibrio(raiz_actual.izquierda)) + 1
            return raiz_actual
        else:
            raiz_actual = nuevo
            return raiz_actual






