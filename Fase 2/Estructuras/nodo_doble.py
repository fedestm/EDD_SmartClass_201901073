class NodoDoble_Anios:
    def __init__(self, anterior, siguiente, anio, semestre, meses):
        self.anio = anio
        self.semestre = semestre
        self.meses = meses
        self.anterior = anterior
        self.siguiente = siguiente

class NodoDoble_Meses:
    def __init__(self, anterior, siguiente, mes, tareas):
        self.mes = mes
        self.tareas = tareas
        self.anterior = anterior
        self.siguiente = siguiente