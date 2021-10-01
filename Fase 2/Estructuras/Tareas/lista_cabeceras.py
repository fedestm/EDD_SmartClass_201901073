class ListaCabeceras:
    def __init__(self):
        self.primero = None
    
    def insertar_cabecera(self, nuevo):
        if self.primero:
            if nuevo.posicion < self.primero.posicion:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            else:
                temp = self.primero
                while temp != None:
                    if nuevo.posicion < temp.posicion:
                        nuevo.siguiente = temp
                        nuevo.anterior = temp.anterior
                        temp.anterior.siguiente = nuevo
                        temp.anterior = nuevo
                        break
                    else:
                        if temp.siguiente == None:
                            temp.siguiente = nuevo
                            nuevo.anterior = temp
                            break
                        else:
                            temp = temp.siguiente
        else:
            #Si lista esta vacia se guarda el primer nodo
            self.primero = nuevo
    
    def buscar_cabecera(self, posicion):
        temp = self.primero
        while temp != None:
            if temp.posicion == posicion:
                return temp
            else:
                temp = temp.siguiente
        return None
    
    def eliminar_cabecera(self, posicion):
        if self.primero:
            temp = self.primero
            if self.primero.posicion == posicion:
                if temp.siguiente:
                    temp.siguiente.anterior = None
                self.primero = temp.siguiente
            else:
                while temp != None:
                    if temp.posicion == posicion:
                        temp.anterior.siguiente = temp.siguiente
                        if temp.siguiente:
                            temp.siguiente.anterior = temp.anterior
                        break
                    else:
                        temp = temp.siguiente