from .nodo_doble_anios import NodoDoble_Anios

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
