from .Hash import Hash

e = Hash()

class CRUD():
    def registrar_estudiante(self, carnet, dpi, nombre, carrera, correo, password, edad):
        e.insertar(int(carnet), dpi, nombre, carrera, correo, password, edad)
    
    def buscar_usuario(self, carnet, password):
        return e.buscar_usuario(int(carnet), password)
    
    def insertar_apunte(self, carnet, titulo, contenido):
        e.insertar_apunte(int(carnet), titulo, contenido)
    
    def graficar_hash(self):
        e.graficar()
    
    def vista_apuntes(self, carnet):
        return e.vista_apuntes(int(carnet))
    
    def detalles_apuntes(self, carnet, cod):
        return e.detalles_apunte(carnet, cod)
    
    