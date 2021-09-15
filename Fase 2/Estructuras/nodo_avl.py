class nodo_avl:
    def __init__(self,carnet,dpi,nombre,carrera,password,creditos,edad):
        self.carnet=carnet
        self.dpi=dpi
        self.nombre=nombre
        self.carrera=carrera
        self.password=password
        self.creditos=creditos
        self.edad=edad
        self.izquierda=None
        self.derecha=None
        self.altura=0