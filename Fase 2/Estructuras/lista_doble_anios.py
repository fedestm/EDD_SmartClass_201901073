from .nodo_doble import NodoDoble_Anios

class ListaDoble_Anios:
    def __init__(self):
        self.primero = self.ultimo = None
    
    def lista_vacia(self):
        return self.primero == None
    
    def insertar(self, anio):
        nuevo = NodoDoble_Anios(None, None, anio)
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
                print(temp.anio, end =" <-> ")
            elif temp == self.ultimo:
                print(temp.anio, end = "")
            else:
                print(temp.anio, end=" <-> ")
            temp = temp.siguiente
    
    def buscar_anio(self, anio):
        if self.lista_vacia():
            print("Lista Vacia")
        else:
            temp = self.primero
            while temp != None:
                if temp.anio == anio:
                    #Si se encuentra el datos retorna el nodo
                    return temp
                else:
                    temp = temp.siguiente
            print("No se encontro el año")
            return None
    
    #Funciones para enlazar lista simple de cursos asignados en el semestre
    def insertar_semestre(self, anio, num_semestres):
        temp = self.buscar_anio(anio)
        if temp != None:
            temp.lista_semestres.insertar(num_semestres)
    
    def insertar_cursos(self, anio, semestre, codigo, nombre, creditos, prerequisitos, obligatorio):
        temp = self.buscar_anio(anio)
        if temp != None:
            temp.lista_semestres.insertar_cursos(semestre, codigo, nombre, creditos, prerequisitos, obligatorio)
    
    def graficar_arbolB(self, anio, semestre):
        temp = self.buscar_anio(anio)
        if temp != None:
            temp.lista_semestres.graficar_arbolB(semestre)
    
    def recorrer_semestre(self, anio):
        temp = self.buscar_anio(anio)
        if temp != None:
            temp.lista_semestres.recorrer()
        else:
            print("No se encontro")
    
    #Funciones para enlazar lista doble de tareas
    def insertar_meses(self, anio, mes):
        temp = self.buscar_anio(anio)
        if temp != None:
            temp.lista_meses.insertar(mes)
    
    def insertar_mes_matriz(self, anio, mes, x, y):
        temp = self.buscar_anio(anio)
        if temp != None:
            temp.lista_meses.insertar_mes(mes, x, y)
    
    def insertar_tareas_matriz(self, anio, mes, x, y, carnet, nombre, desc, materia, fecha, hora, estado):
        temp = self.buscar_anio(anio)
        if temp != None:
            temp.lista_meses.insertar_tareas(mes, x, y, carnet, nombre, desc, materia, fecha, hora, estado)
    
    def graficar_matriz(self, anio, mes):
        temp = self.buscar_anio(anio)
        if temp != None:
            temp.lista_meses.graficar_matriz(mes)
    
    def graficar_lista_tareas(self, anio, mes, x, y):
        temp = self.buscar_anio(anio)
        if temp != None:
            temp.lista_meses.graficar_tareas(mes, x, y)
    
    def eliminar_posicion(self, anio, mes, x, y):
        temp = self.buscar_anio(anio)
        if temp != None:
            temp.lista_meses.eliminar_posicion(mes, x, y)
    
    def mostrar_tarea(self, anio, mes, x, y):
        temp = self.buscar_anio(anio)
        if temp != None:
            return temp.lista_meses.mostrar_tarea(mes, x, y)