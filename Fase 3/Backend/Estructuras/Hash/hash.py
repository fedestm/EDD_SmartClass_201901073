from .nodo import Nodo
import os

class Hash:
    def __init__(self):
        self.claves = []
        self.size = 7
        self.claves_usadas = 0
        for i in range(self.size):
            self.claves.append(None)
    
    def calcular_hash(self, carnet):
        resultado = 0
        resultado = carnet % self.size
        return resultado
    
    def solucionar_colisiones(self, indice):
        nuevo_indice = 0
        i = 0
        disponible = False

        while disponible == False:
            nuevo_indice = indice + int(i**2)

            if nuevo_indice >= self.size:
                nuevo_indice = nuevo_indice - self.size
            if self.claves[nuevo_indice] == None:
                disponible = True
            i += 1
        return nuevo_indice
    
    def insertar(self, carnet, dpi, nombre, carrera, correo, password, edad):
        nuevo = Nodo(carnet, dpi, nombre, carrera, correo, password, edad)

        indice_hash = self.calcular_hash(carnet)

        if self.claves[indice_hash] == None:
            self.claves[indice_hash] = nuevo
            self.claves_usadas += 1
        else:
            indice_hash = self.solucionar_colisiones(indice_hash)
            self.claves[indice_hash] = nuevo
            self.claves_usadas += 1
        
        P_uso = 0
        P_uso = float(float(self.claves_usadas) / float(self.size))

        if P_uso >= 0.5:
            self.rehash()

    def rehash(self):
        es_primo = False
        new_tam = self.size

        while es_primo == False:
            new_tam += 1
            cont = 0
            for i in range(new_tam, 0, -1):
                if new_tam % i == 0:
                    cont += 1
            if cont == 2:
                es_primo = True
        
        aux = []
        for i in range(self.size):
            aux.append(None)
        aux = self.claves
        self.size = new_tam

        new_claves = []
        for i in range(new_tam):
            new_claves.append(None)
        self.claves = new_claves
        self.claves_usadas = 0

        for i in range(len(aux)):
            if aux[i] != None:
                self.insertar(aux[i].carnet, aux[i].dpi, aux[i].nombre, aux[i].carrera, aux[i].correo, aux[i].password, aux[i].edad)
    
    def generar_nodos(self):
        dot = ""
        for i in range(len(self.claves) - 1, -1, -1):
            if self.claves[i] != None:
                dot += "node[shape = record label = \"{" + str(i) + "| - Carnet: " + str(self.claves[i].carnet) + "|}\";]v" + str(i) + "\n"
                dot += str(self.enlazar_lista(self.claves[i].carnet, "v" + str(i)))
            else:
                dot += "node[shape = record label = \"{" + str(i) + "| -      Vacio       -}\";]v" + str(i) + "\n"
        return dot
    
    def graficar(self):
        file = open("hash.dot", "w")
        dot = "digraph Hash{\n"
        dot += "rankdir=LR;\n"
        dot += "nodesep=0;\n"
        dot += "node [shape = box,fillcolor=\"#5DADE2\" color=\"black\" style=\"filled\"];\n"
        dot += self.generar_nodos()
        dot += "}\n"
        file.write(dot)
        file.close()
        os.system("dot -Tpng hash.dot -o hash.png")
    
    def buscar_usuario(self, carnet, password):
        for i in range(self.size):
            if self.claves[i] != None:
                if self.claves[i].carnet == carnet and self.claves[i].password == password:
                    return True
        return False
    
    def buscar(self, carnet):
        for i in range(self.size):
            if self.claves[i] != None:
                if self.claves[i].carnet == carnet:
                    return self.claves[i]
        return None
    
    def insertar_apunte(self, carnet, titulo, apunte):
        temp = self.buscar(carnet)
        if temp != None:
            temp.lista_apuntes.insertar(titulo, apunte)
    
    def enlazar_lista(self, carnet, indice):
        temp = self.buscar(carnet)
        if temp != None:
            return temp.lista_apuntes.graficar(indice)
    
    def vista_apuntes(self, carnet):
        temp = self.buscar(carnet)
        if temp != None:
            return temp.lista_apuntes.lista_apuntes()
    
    def detalles_apuntes(self, carnet, cod):
        temp = self.buscar(carnet)
        if temp != None:
            return temp.lista_apuntes.detalles_apuntes(cod)
    
    def insertar_anio(self, carnet, anio):
        temp = self.buscar(carnet)
        if temp != None:
            temp.lista_anios.insertar(anio)
    
    def insertar_semestre(self, carnet, anio, semestre):
        temp = self.buscar(carnet)
        if temp != None:
            temp.lista_anios.insertar_semestre(anio, semestre)
    
    