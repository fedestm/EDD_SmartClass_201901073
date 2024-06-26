from .nodo_simple import NodoSimple
import json

class ListaSimple:
    def __init__(self):
        self.primero = self.ultimo = None
        self.cont = 0
    
    def lista_vacia(self):
        return self.primero == None
    
    def insertar(self, titulo, apunte):
        self.cont += 1
        nuevo = NodoSimple(self.cont, titulo, apunte)
        if self.lista_vacia():
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
    
    def graficar(self, indice):
        dot = ""
        temp = self.primero

        while temp != None:
            if temp == self.primero:
                dot += "\"" + "n_" + str(temp) + "\"" + "[label=\"" +"Titulo: " + temp.titulo + "\\nApunte: " + temp.apunte + "\", shape = ellipse, fillcolor = \"#FFFF00\"""];\n"
            elif temp == self.ultimo:
                dot += "\"" + "n_" + str(temp) + "\"" + "[label=\"" +"Titulo: " + temp.titulo + "\\nApunte: " + temp.apunte + "\", shape = ellipse, fillcolor = \"#FFFF00\"""];\n"
            else:
                dot += "\"" + "n_" + str(temp) + "\"" + "[label=\"" +"Titulo: " + temp.apunte + "\\nApunte: " + temp.apunte + "\", shape = ellipse, fillcolor = \"#FFFF00\"""];\n"
            
            if temp.siguiente != None:
                dot += "\"" + "n_" + str(temp) + "\"" + " -> " +  "\"" + "n_" + str(temp.siguiente) + "\"" + ";\n"
            temp = temp.siguiente
        
        enlace = self.primero

        while enlace != None:
            if enlace == self.primero:
                dot += indice + " -> " + "\"" + "n_" + str(enlace) + "\"" + ";\n"
            enlace = enlace.siguiente
        
        return dot
    
    def lista_apuntes(self):
        temp = self.primero
        obj = {}
        lista = []

        while temp != None:
            obj = {
                'id': temp.id,
                'titulo': temp.titulo,
                'contenido': temp.apunte
            }
            lista.append(obj)
            temp = temp.siguiente
        return json.dumps(lista)
    
    def detalles_apuntes(self, cod):
        obj = {}
        vacio = {}
        res = {}
        if self.lista_vacia():
            vacio = {
                'response': 'No hay datos en la lista'
            }
            return vacio
        else:
            temp = self.primero
            while temp != None:
                if temp.id == cod:
                    obj = {
                        'id': temp.id,
                        'titulo': temp.titulo,
                        'contenido': temp.apunte
                    }
                    return obj
                else:
                    temp = temp.siguiente
            res = {
                'response': 'No se encontro'
            }
            return res
    
    