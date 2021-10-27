from .nodo_simple import NodoSimple

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
        