class NodoDoble_Tareas:
    def __init__(self, anterior, siguiente, carnet, nombre, desc, materia, fecha, hora, estado):
        self.carnet = carnet
        self.nombre = nombre
        self.desc = desc
        self.materia = materia
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.anterior = anterior
        self.siguiente = siguiente