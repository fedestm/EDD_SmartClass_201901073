from .lista_cabeceras import ListaCabeceras
from .nodo_cabeceras import NodoCabeceras
import os

class Matriz:
    def __init__(self):
        self.cabeceras_x = ListaCabeceras()
        self.cabeceras_y = ListaCabeceras()
    
    def insertar(self, x, y):
        nodo_cabecera_x = None
        nodo_cabecera_y = None

        if self.cabeceras_x and self.cabeceras_y:
            nodo_cabecera_x = self.cabeceras_x.buscar_cabecera(x)
            nodo_cabecera_y = self.cabeceras_y.buscar_cabecera(y)
        
        if nodo_cabecera_x == None:
            nodo_cabecera_x = NodoCabeceras(x)
            self.cabeceras_x.insertar_cabecera(nodo_cabecera_x)
        
        if nodo_cabecera_y == None:
            nodo_cabecera_y = NodoCabeceras(y)
            self.cabeceras_y.insertar_cabecera(nodo_cabecera_y)
        
        nodo_cabecera_x.lista_interna.insertar_posx(x, y)
        nodo_cabecera_y.lista_interna.insertar_posy(x, y)

    def graficar(self):
        dot = ""
        file = open("matriz_dispersa.dot","w")
        dot += "digraph G{\n rankdir = TB\n"
        dot += "node[shape = box,width=0.7,height=0.7,fillcolor=\"azure2\" color=\"white\" style=\"filled\"];\n"
        dot += "edge[style = \"bold\"];\n"
        dot += "node[label = \"Mes: 5\" fillcolor=\" darkolivegreen1\" pos = \"-1,1!\"]principal;\n"

        #Cabeceras en X
        temp_cx = self.cabeceras_x.primero
        cont = 0
        while temp_cx != None:
            tempx = temp_cx.lista_interna.primero
            dot += "\n\tnode[label = \"X: %d\" fillcolor=\"#58D68D\" pos = \"%d,1!\" shape = box]x%d;" % (tempx.pos_x ,tempx.pos_x, cont)
            cont += 1
            temp_cx = temp_cx.siguiente
        
        #Cabeceras en Y
        temp_cy = self.cabeceras_y.primero
        cont2 = 0
        while temp_cy != None:
            tempy = temp_cy.lista_interna.primero
            dot += "\n\tnode[label = \"Y: %d\" fillcolor=\"#3498DB\" pos = \"-1,-%d!\" shape = box]y%d;" % (tempy.pos_y, tempy.pos_y, cont2)
            cont2 += 1
            temp_cy = temp_cy.siguiente
        
        for i in range(cont - 1):
            dot += "\nx"+str(i)+" -> x"+str(i+1)+";"
            dot += "\nx"+str(i+1)+" -> x"+str(i)+";"
        
        for i in range(cont2 - 1):
            dot += "\ny"+str(i)+" -> y"+str(i+1)+";"
            dot += "\ny"+str(i+1)+" -> y"+str(i)+";"
        
        #Valores interno de matriz
        temp = self.cabeceras_x.primero
        while temp != None:
            aux = temp.lista_interna
            dot += aux.graficar_internos()
            temp = temp.siguiente

        dot += "\n}\n"

        file.write(dot)
        file.close()
        os.system("neato -Tsvg matriz_dispersa.dot -o matriz_dispersa.svg")
        os.startfile("matriz_dispersa.svg")
    
    def insertar_tareas(self, x, y, carnet, nombre, desc, materia, fecha, hora, estado):
        temp = self.cabeceras_x.primero
        while temp != None:
            temp2 = temp.lista_interna
            temp2.insertar_tareas(x, y, carnet, nombre, desc, materia, fecha, hora, estado)
            temp = temp.siguiente
    
    def graficar_tareas(self, x, y):
        temp = self.cabeceras_x.primero
        while temp != None:
            temp2 = temp.lista_interna
            temp2.graficar_lista_tareas(x, y)
            temp = temp.siguiente
    
    def eliminar(self, x, y):
        cabecerax = self.cabeceras_x.buscar_cabecera(x)
        cabeceray = self.cabeceras_y.buscar_cabecera(y)

        if cabecerax != None and cabeceray != None:
            cabecerax.lista_interna.eliminar_posx(y)
            if cabecerax.lista_interna.primero == None:
                self.cabeceras_x.eliminar_cabecera(cabecerax.posicion)
            
            cabeceray.lista_interna.eliminar_posy(x)
            if cabeceray.lista_interna.primero == None:
                self.cabeceras_y.eliminar_cabecera(cabeceray.posicion)
        else:
            print("No se encuentra dicha posicion")
    
    def mostrar_tarea(self, x, y):
        temp = self.cabeceras_x.primero
        while temp != None:
            temp2 = temp.lista_interna
            return temp2.mostrar_tarea(x, y)
            temp = temp.siguiente
    
    def modificar_tarea(self, x, y, nombre, desc, materia, estado):
        temp = self.cabeceras_x.primero
        while temp != None:
            temp2 = temp.lista_interna
            temp2.modificar_tarea(x, y, nombre, desc, materia, estado)
            temp = temp.siguiente