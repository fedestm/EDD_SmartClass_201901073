from .nodo_avl import nodo_avl
import os

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
        nodo_avl.derecha = aux.izquierda
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
        aux = self.R_derecha(nodo_avl)
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
        if self.raiz != None:
            dot += self.recorrer(self.raiz)
            dot += "\n"
            dot += self.enlazar(self.raiz)
        dot += "}"
        #w+ Escritura en un archivo, se le agrega contenido extra sin eliminar contenido anterior
        file = open("avl.dot","w+")
        file.write(dot)
        file.close()
        os.system("dot -Tsvg avl.dot -o avl.svg")
        os.startfile("avl.svg")

    
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
    
    def enlazar(self, raiz_actual):
        dot = ""
        if raiz_actual:
            if raiz_actual.izquierda:
                #Se conecta raiz de carnet a nodo de la izquierda
                dot += "n" + str(raiz_actual.carnet) + ":C0 -> n" + str(raiz_actual.izquierda.carnet) + ":value\n"
            if raiz_actual.derecha:
                dot += "n" + str(raiz_actual.carnet) + ":C1 -> n" + str(raiz_actual.derecha.carnet) + ":value\n"

            dot += self.enlazar(raiz_actual.izquierda)
            dot += self.enlazar(raiz_actual.derecha)
        
        return dot
    
    #Recorrer arbol para buscar carnet
    def rec(self, raiz_actual, carnet):
        if raiz_actual:
            #Se recorre raiz por la izquierda
            if self.rec(raiz_actual.izquierda, carnet):
                #Se verifica si el carnet se encuentra en el nodo izquierdo
                if raiz_actual.izquierda.carnet == carnet:
                    return raiz_actual.izquierda
                else:
                    #Si no se encuentra se busca el siguiente
                    return self.rec(raiz_actual.izquierda, carnet)
            elif self.rec(raiz_actual.derecha, carnet):
                #Se verifica si el carnet se encuentra en el nodo derecho
                if raiz_actual.derecha.carnet == carnet:
                    return raiz_actual.derecha
                else:
                    #Se busca en el siguiente
                    return self.rec(raiz_actual.derecha, carnet)
            else:
                #Si el carnet no esta en derecha o izquierda, se encuentra en la primera raiz
                if raiz_actual.carnet == carnet:
                    return raiz_actual
    
    def recorrer_modificar(self, raiz_actual, carnet, dpi, nombre, carrera, password, creditos, edad):
        if raiz_actual:
            if self.recorrer_modificar(raiz_actual.izquierda, carnet, dpi, nombre, carrera, password, creditos, edad):
                if raiz_actual.izquierda.carnet == carnet:
                    raiz_actual.izquierda.dpi == dpi
                    raiz_actual.izquierda.nombre == nombre
                    raiz_actual.izquierda.carrera == carrera
                    raiz_actual.izquierda.password == password
                    raiz_actual.izquierda.creditos == creditos
                    raiz_actual.izquierda.edad == edad
                    return raiz_actual.izquierda
                else:
                    return self.recorrer_modificar(raiz_actual.izquierda, carnet, dpi, nombre, carrera, password, creditos, edad)
            elif self.recorrer_modificar(raiz_actual.derecha, carnet, dpi, nombre, carrera, password, creditos, edad):
                if raiz_actual.derecha.carnet == carnet:
                    raiz_actual.derecha.dpi == dpi
                    raiz_actual.derecha.nombre == nombre
                    raiz_actual.derecha.carrera == carrera
                    raiz_actual.derecha.password == password
                    raiz_actual.derecha.creditos == creditos
                    raiz_actual.derecha.edad == edad
                    return raiz_actual.derecha
                else:
                    return self.recorrer_modificar(raiz_actual.derecha, carnet, dpi, nombre, carrera, password, creditos, edad)
            else:
                if raiz_actual.carnet == carnet:
                    raiz_actual.dpi == dpi
                    raiz_actual.nombre == nombre
                    raiz_actual.carrera == carrera
                    raiz_actual.password == password
                    raiz_actual.creditos == creditos
                    return raiz_actual
    
    def buscar(self, carnet):
        raiz_actual = self.raiz
        if raiz_actual != None:
            return self.rec(raiz_actual, carnet)
    
    def modificar_estudiante(self, carnet, dpi, nombre, carrera, password, creditos, edad):
        raiz_actual = self.raiz
        if raiz_actual != None:
            return self.modificar_estudiante(carnet, dpi, nombre, carrera, password, creditos, edad)
    
    def insertar_anio(self, carnet, anio):
        temp = self.buscar(carnet)
        if temp != None:
            temp.lista_anios.insertar(anio)
    
    #Operaciones de Cursos de Semestre
    def insertar_semestre(self, carnet, anio, semestre):
        temp = self.buscar(carnet)
        if temp != None:
            temp.lista_anios.insertar_semestre(anio, semestre)
    
    def insertar_cursos(self, carnet, anio, semestre, codigo, nombre, creditos, prerequisitos, obligatorio):
        temp = self.buscar(carnet)
        if temp != None:
            temp.lista_anios.insertar_cursos(anio, semestre, codigo, nombre, creditos, prerequisitos, obligatorio)
    
    def graficar_arbolB(self, carnet, anio, semestre):
        temp = self.buscar(carnet)
        if temp != None:
            temp.lista_anios.graficar_arbolB(anio, semestre)
    
    #Operaciones de Recordatorio de Tareas
    def insertar_meses(self, carnet, anio, mes):
        temp = self.buscar(carnet)
        if temp != None:
            temp.lista_anios.insertar_meses(anio, mes)
    
    def insertar_mes_matriz(self, carnet, anio, mes, dia, hora):
        temp = self.buscar(carnet)
        if temp != None:
            temp.lista_anios.insertar_mes_matriz(anio, mes, dia, hora)
    
    def insertar_tareas_matriz(self, carnet, anio, mes, dia_y, hora_y, carnet_t, nombre, desc, materia, fecha, hora, estado):
        temp = self.buscar(carnet)
        if temp != None:
            temp.lista_anios.insertar_tareas_matriz(anio, mes, dia_y, hora_y, carnet_t, nombre, desc, materia, fecha, hora, estado)
    
    def graficar_matriz(self, carnet, anio, mes):
        temp = self.buscar(carnet)
        if temp != None:
            temp.lista_anios.graficar_matriz(anio, mes)
    
    def graficar_lista_tareas(self, carnet, anio, mes, dia, hora):
        temp = self.buscar(carnet)
        if temp != None:
            temp.lista_anios.graficar_lista_tareas(anio, mes, dia, hora)
    
    def eliminar_posicion(self, carnet, anio, mes, dia, hora):
        temp = self.buscar(carnet)
        if temp != None:
            temp.lista_anios.eliminar_posicion(anio, mes, dia, hora)