from .nodo_simple import Nodo_Simple

class ListaSimple:
    def __init__(self):
        self.primero = self.ultimo = None
    
    def lista_vacia(self):
        return self.primero == None
    
    def insertar(self, semestre):
        nuevo = Nodo_Simple(None, semestre)
        if self.lista_vacia():
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo

    def recorrer(self):
        temp = self.primero
        while temp!= None:
            print(temp.semestre + " -> ")
            temp = temp.siguiente
    
    def buscar(self, semestre):
        if self.lista_vacia():
            print("Lista Vacia")
        else:
            temp = self.primero
            while temp != None:
                if temp.semestre == semestre:
                    return temp
                else:
                    temp = temp.siguiente
            return None
    
    def insertar_cursos(self, semestre, codigo, nombre, creditos, prerequisitos, obligatorio):
        temp = self.buscar(semestre)
        if temp != None:
            temp.arbol_cursos.insertar_nodo(codigo, nombre, creditos, prerequisitos, obligatorio)
    
    def graficar_arbolB(self, semestre):
        temp = self.buscar(semestre)
        if temp != None:
            temp.arbol_cursos.graficar()
