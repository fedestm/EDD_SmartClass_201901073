from ListaNodos import ListaNodos

class Pagina:
    def __init__(self):
        self.raiz = False
        self.tam = 0
        self.claves_max = 4
        self.claves_min = 2
        self.claves = ListaNodos()