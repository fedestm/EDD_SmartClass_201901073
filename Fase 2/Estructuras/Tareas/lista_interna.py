from .nodo_interno import NodoInterno
from .lista_doble_tareas import ListaDoble_Tareas

class Lista_Interna:
    def __init__(self):
        self.primero = None
    
    def insertar_posx(self, x, y, cantidad):
        nuevo = NodoInterno(x, y, cantidad)

        if self.primero:
            if nuevo.pos_y < self.primero.pos_y:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            else:
                temp = self.primero
                while temp != None:
                    if nuevo.pos_y < temp.pos_y:
                        nuevo.siguiente = temp
                        nuevo.anterior = temp.anterior
                        temp.anterior.siguiente = nuevo
                        temp.anterior = nuevo
                        break
                    elif nuevo.pos_x == temp.pos_x and nuevo.pos_y == temp.pos_y:
                        #Posicion ocupada
                        break
                    else:
                        if temp.siguiente == None:
                            temp.siguiente = nuevo
                            nuevo.anterior = temp
                            break
                        else:
                            temp = temp.siguiente
        else:
            #Si la lista esta vacia se guarda el primer nodo
            self.primero = nuevo
    
    def insertar_posy(self, x, y, cantidad):
        nuevo = NodoInterno(x, y, cantidad)

        if self.primero:
            if nuevo.pos_x < self.primero.pos_x:
                nuevo.abajo = self.primero
                self.primero.arriba = nuevo
                self.primero = nuevo
            else:
                temp = self.primero
                while temp != None:
                    if nuevo.pos_x < temp.pos_x:
                        nuevo.abajo = temp
                        nuevo.arriba = temp.anterior
                        temp.arriba.abajo = nuevo
                        temp.arriba = nuevo
                        break
                    elif nuevo.pos_x == temp.pos_x and nuevo.pos_y == temp.pos_y:
                        #Posicion ocupada
                        #Finaliza condicion
                        break
                    else:
                        if temp.abajo == None:
                            temp.abajo = nuevo
                            nuevo.arriba = temp
                            break
                        else:
                            temp = temp.abajo
        else:
            #Si lista esta vacia se guarda el primer nodo
            self.primero = nuevo
    
    def buscar_cantidad(self, x, y):
        temp = self.primero
        while temp != None:
            if temp.pos_x == x and temp.pos_y == y:
                return temp
            else:
                temp = temp.sig
        return None
    
    def insertar_tareas(self, x, y, carnet, nombre, desc, materia, fecha, hora, estado):
        temp = self.buscar_cantidad(x, y)
        if temp != None:
            temp.lista_tareas.insertar(carnet, nombre, desc, materia, fecha, hora, estado)
    
    def cantidad_tareas(self, x, y):
        temp = self.buscar_cantidad(x, y)
        if temp != None:
            return temp.lista_tareas.cantidad_tareas()
    
    def graficar_lista_tareas(self, x, y):
        temp = self.buscar_cantidad(x, y)
        if temp != None:
            temp.lista_tareas.graficar()
    
    def graficar_internos(self):
        dot = ""
        temp = self.primero
        while temp != None:
            dot += "node[label =\"%s\" fillcolor=\"#EB984E\" pos=\"%d,-%d!\" shape = box]\"i%d-%d!\"" % (self.cantidad_tareas(x, y), temp.pos_x, temp.pos_y, temp.pos_x, temp.pos_y)+";\n"
            temp = temp.siguiente
        return dot