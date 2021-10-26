from Hash import Hash

e = Hash()

class CRUD():
    def registrar_estudiante(self, carnet, dpi, nombre, carrera, correo, password, edad):
        e.insertar(carnet, dpi, nombre, carrera, correo, password, edad)
    
    