from typing import List


class NodoGrafo:
    def __init__(self, codigo, curso, creditos, prerequisitos, obligatorio):
        self.codigo = codigo
        self.curso = curso
        self.creditos = creditos
        self.prerequisitos = prerequisitos
        self.obligatorio = obligatorio
        self.siguiente = None
        self.lista_simple = Lista()
    
class Lista:
    def __init__(self):
        self.primero = self.ultimo = None
    
    def insertar(self, codigo, curso, creditos, prerequisitos, obligatorio):
        nuevo = NodoGrafo(codigo, curso, creditos, prerequisitos, obligatorio)

        if self.primero == None:
            self.ultimo = nuevo
            self.primero = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
    
