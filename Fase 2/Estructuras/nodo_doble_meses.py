from Tareas import Matriz

class NodoDoble_Meses:
    def __init__(self, anterior, siguiente, mes):
        self.mes = mes
        self.anterior = anterior
        self.siguiente = siguiente
        self.lista_matrices = Matriz()