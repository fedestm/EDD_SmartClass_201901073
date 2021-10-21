from nodo import Nodo

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
            