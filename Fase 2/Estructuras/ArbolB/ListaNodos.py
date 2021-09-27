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

