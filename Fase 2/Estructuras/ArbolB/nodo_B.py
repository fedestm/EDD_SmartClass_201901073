class NodoB:
    def __init__(self, codigo, nombre, creditos, prerequisitos, obligatorio):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.prerequisitos = prerequisitos
        self.obligatorio = obligatorio
        self.siguiente = None
        self.anterior = None
        self.izquierda = None
        self.derecha = None