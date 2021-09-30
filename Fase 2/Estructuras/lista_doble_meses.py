from nodo_doble_meses import NodoDoble_Meses

class ListaDoble_Meses:
    def __init__(self):
        self.primero = self.ultimo = None
    
    def lista_vacia(self):
        return self.primero == None

    def insertar(self, mes, tareas):
        nuevo = NodoDoble_Meses(None, None, mes, tareas)
        if self.lista_vacia():
            self.primero = self.ultimo = nuevo
        else:
            if self.primero == self.ultimo:
                self.primero.siguiente = nuevo
                nuevo.anterior = self.primero
                self.ultimo = nuevo
            else:
                nuevo.anterior = self.ultimo
                self.ultimo.siguiente = nuevo
                self.ultimo = nuevo
    
    def recorrer(self):
        temp = self.primero
        
        while temp != None:
            if temp == self.primero:
                print(temp.mes, end =" <-> ")
            elif temp == self.ultimo:
                print(temp.mes, end = "")
            else:
                print(temp.mes, end=" <-> ")
            temp = temp.siguiente