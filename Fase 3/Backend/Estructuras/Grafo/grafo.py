class NodoGrafo:
    def __init__(self, codigo, curso, creditos, prerequisitos, obligatorio):
        self.codigo = codigo
        self.curso = curso
        self.creditos = creditos
        self.prerequisitos = prerequisitos
        self.obligatorio = obligatorio
        self.siguiente = None
    
    