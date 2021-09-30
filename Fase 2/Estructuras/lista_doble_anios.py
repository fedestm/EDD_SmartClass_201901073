from nodo_doble import NodoDoble_Anios

class ListaDoble_Anios:
    def __init__(self):
        self.primero = self.ultimo = None
    
    def lista_vacia(self):
        return self.primero == None
    
    def insertar(self, anio, semestre, meses):
        nuevo = NodoDoble_Anios(None, None, anio, semestre, meses)
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
    
    def insertar_semestre(self, anio, num_semestres, cursos):
        temp = self.buscar_anio(anio)
        if temp != None:
            temp.lista_semestres.insertar(num_semestres, cursos)
    
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
    
    def recorrer_meses(self, anio):
        temp = self.buscar_anio(anio)
        if temp != None:
            temp.lista_meses.recorrer()
        else:
            print("No se encontro")
