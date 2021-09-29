from nodo_doble_tareas import NodoDoble_Tareas

class ListaDoble_Tareas:
    def __init__(self):
        self.primero = self.ultimo = None
    
    def lista_vacia(self):
        return self.primero == None
    
    def insertar(self, carnet, nombre, desc, materia, fecha, hora, estado):
        nuevo = NodoDoble_Tareas(None, None, carnet, nombre, desc, materia, fecha, hora, estado)
        if self.lista_vacia():
            self.primero = self.ultimo = nuevo
        else:
            if self.primero == self.ultimo:
                self.primero.siguiente = nuevo
                nuevo.anterior = nuevo
                self.ultimo = nuevo
            else:
                nuevo.anterior = self.ultimo
                self.ultimo.siguiente = nuevo
                self.ultimo = nuevo
    
    def recorrer(self):
        temp = self.primero
        while temp != None:
            if temp == self.primero:
                print(temp.materia, end =" <-> ")
            elif temp == self.ultimo:
                print(temp.materia, end = "")
            else:
                print(temp.materia, end=" <-> ")
    
    def cantidad_tareas(self):
        temp = self.primero
        cont = 0
        while temp != None:
            cont += 1
            temp = temp.siguiente
        return cont