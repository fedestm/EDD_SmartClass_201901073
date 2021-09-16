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
    
    def insertar(self, carnet, dpi, nombre, carrera, password, creditos, edad):
        nuevo = nodo_avl(carnet, dpi, nombre, carrera, password, creditos, edad)

        if self.raiz == None:
            self.raiz = nuevo
        else:
            self.raiz = self.insertar_nodo(nuevo, self.raiz)
    
    def graficar(self):
        dot = "digraph avl {\n"
        dot += "node[shape=plaintext];\nrankdir=TR;\n"
        dot += "}"

        file = open("avl.dot","w+")
        file.write(dot)
        file.close()
    
    def recorrer(self, raiz_actual):
        if raiz_actual:
            dot = "\nn"+str(raiz_actual.carnet)+"[label= <<TABLE BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\">"
            dot += "\n\t<TR><TD BGCOLOR=\"orange\" PORT=\"C0\">  I  <br/>  Z  <br/>  Q  "   
            dot += "</TD>\n\t<TD PORT=\"value\">"
            dot += "Carnet: "+str(raiz_actual.carnet)+"<br/>DPI: "+str(raiz_actual.nombre)+"<br/>Nombre: "+str(raiz_actual.dpi)
            dot += "<br/>Carrera: "+str(raiz_actual.carrera)+"  <br/>Password: "+str(raiz_actual.password)
            dot += "<br/>Creditos: "+str(raiz_actual.creditos)+"<br/>Edad: "+str(raiz_actual.edad)
            dot += "</TD>"
            dot += "\n\t<TD BGCOLOR=\"#33A8FF\" PORT=\"C1\">  D  <br/>  E  <br/>  R  </TD></TR>\n</TABLE>>];\n"
            dot += self.recorrer(raiz_actual.izquierda)
            dot += self.recorrer(raiz_actual.derecha)
            return dot
        else:
            return ""




