class ListaNodos:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
    
    def insertar(self, nuevo):
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
            self.size += 1
            return True
        else:
            if self.primero == self.ultimo:
                if nuevo.codigo < self.primero.codigo:
                    nuevo.siguiente = self.primero
                    self.primero.anterior = nuevo
                    self.primero.izquierda = nuevo.derecha
                    self.primero = nuevo
                    self.size += 1
                    return True
                elif nuevo.codigo > self.ultimo.codigo:
                    self.ultimo.siguiente = nuevo
                    nuevo.anterior = self.ultimo
                    self.ultimo.derecha = nuevo.izquierda
                    self.ultimo = nuevo
                    self.size += 1
                    return True
                else:
                    #Retorna False porque ya se encuentra el codigo que se ingreso
                    return False

