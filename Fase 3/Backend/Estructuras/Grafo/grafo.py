import os

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
    
class Grafo:
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
    
    def buscar(self, codigo):
        temp = self.primero

        while temp != None:
            if temp.codigo == codigo:
                return temp
            else:
                temp = temp.siguiente
        return None
    
    def insertar_adyacente(self, codigo, adyacente, curso, creditos, prerequisitos, obligatorio):
        nodo_origen = self.buscar(codigo)
        nodo_adyacente = self.buscar(adyacente)

        if nodo_adyacente == None:
            self.insertar(adyacente, curso, creditos, prerequisitos, obligatorio)
        if nodo_origen != None:
            lista_adyacente = nodo_origen.lista_simple
            lista_adyacente.insertar(adyacente, curso, creditos, prerequisitos, obligatorio)
        else:
            return "No se encontro nodo origen"
    
    def graficar(self):
        dot = ""
        dot += "digraph grafo {\n"
        dot += "rankdir = \"LR\""

        temp = self.primero

        while temp != None:
            dot += "n_" + str(temp.codigo) + "[label = \"" + str(temp.codigo) + "\n" + str(temp.curso) + "\"];\n"
            temp = temp.siguiente
        
        dot += "\n}"
        file = open("grafo.dot", "w+")
        file.write(dot)
        file.close()
        os.system("dot -Tpng grafo.dot -o grafo.png")
    
    def graficar_enlaces(self):
        dot = ""
        temp = self.primero

        while temp != None:
            aux = temp.lista_simple.primero
            while aux != None:
                dot += "n_" + str(temp.codigo) + " -> n_" + str(aux.codigo) + "[dir = \"none\" label = \"" + str(temp.creditos) + "\"]\n"
                aux = aux.siguiente
            temp = temp.siguiente
        return dot
    


