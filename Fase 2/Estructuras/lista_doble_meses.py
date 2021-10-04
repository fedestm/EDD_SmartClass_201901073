from .nodo_doble_meses import NodoDoble_Meses

class ListaDoble_Meses:
    def __init__(self):
        self.primero = self.ultimo = None
    
    def lista_vacia(self):
        return self.primero == None

    def insertar(self, mes):
        nuevo = NodoDoble_Meses(None, None, mes)
        if self.lista_vacia():
            self.primero = self.ultimo = nuevo
        else:
            if self.primero == self.ultimo:
                self.primero.siguiente = nuevo
                nuevo.anterior = self.primero
                self.ultimo = nuevo
            else:
                nuevo.anterior = self.ultimo
                self.ultimo.siguiente = nuevo
                self.ultimo = nuevo
    
    def recorrer(self):
        temp = self.primero
        
        while temp != None:
            if temp == self.primero:
                print(temp.mes, end =" <-> ")
            elif temp == self.ultimo:
                print(temp.mes, end = "")
            else:
                print(temp.mes, end=" <-> ")
            temp = temp.siguiente
    
    def buscar(self, mes):
        if self.lista_vacia():
            print("Lista Vacia")
        else:
            temp = self.primero
            while temp != None:
                if temp.mes == mes:
                    return temp
                else:
                    temp = temp.siguiente
            return None

    #Se inserta mes, dia y hora en matriz dispersa
    def insertar_mes(self, mes, dia, hora):
        temp = self.buscar(mes)
        if temp != None:
            temp.lista_matrices.insertar(dia, hora)
    
    # x -> Dia
    # y -> Hora
    def insertar_tareas(self, mes, x, y, carnet, nombre, desc, materia, fecha, hora, estado):
        temp = self.buscar(mes)
        if temp != None:
            temp.lista_matrices.insertar_tareas(x, y, carnet, nombre, desc, materia, fecha, hora, estado)
    
    def graficar_matriz(self, mes):
        temp = self.buscar(mes)
        if temp != None:
            temp.lista_matrices.graficar()
    
    def graficar_tareas(self, mes, x, y):
        temp = self.buscar(mes)
        if temp != None:
            temp.lista_matrices.graficar_tareas(x, y)
    
    def eliminar_posicion(self, mes, x, y):
        temp = self.buscar(mes)
        if temp != None:
            temp.lista_matrices.eliminar(x, y)
    
    def mostrar_tarea(self, mes, x, y):
        temp = self.buscar(mes)
        if temp != None:
            return temp.lista_matrices.mostrar_tarea(x, y)
    
    def modificar_tarea(self, mes, x, y, nombre, desc, materia, estado):
        temp = self.buscar(mes)
        if temp != None:
            temp.lista_matrices.modificar_tarea(x, y, nombre, desc, materia, estado)