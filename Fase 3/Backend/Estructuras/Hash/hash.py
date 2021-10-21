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
    
    