from nodo_interno import NodoInterno

class Lista_Interna:
    def __init__(self):
        self.primero = None
    
    def insertar_posx(self, x, y, cantidad):
        nuevo = NodoInterno(x, y, cantidad)

        if self.primero:
            if nuevo.pos_y < self.primero.pos_y:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            else:
                temp = self.primero
                while temp != None:
                    if nuevo.pos_y < temp.pos_y:
                        nuevo.siguiente = temp
                        nuevo.anterior = temp.anterior
                        temp.anterior.siguiente = nuevo
                        temp.anterior = nuevo
                        break
                    elif nuevo.pos_x == temp.pos_x and nuevo.pos_y == temp.pos_y:
                        #Posicion ocupada
                        break
                    else:
                        if temp.siguiente == None:
                            temp.siguiente = nuevo
                            nuevo.anterior = temp
                            break
                        else:
                            temp = temp.siguiente
        else:
            #Si la lista se guarda el primer nodo
            self.primero = nuevo
    
    def insertar_posy(self, x, y, cantidad):
        nuevo = NodoInterno(x, y, cantidad)

        if self.primero:
            if nuevo.pos_x < self.primero.pos_x:
                nuevo.abajo = self.primero
                self.primero.arriba = nuevo
                self.primero = nuevo