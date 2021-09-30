from Tareas import Matriz

class NodoDoble_Meses:
    def __init__(self, anterior, siguiente, mes, tareas):
        self.mes = mes
        self.tareas = tareas
        self.anterior = anterior
        self.siguiente = siguiente
        self.lista_matrices = Matriz()