from .Hash import Hash
from .Grafo import Grafo
from .Hash import ListaSimple_Pensum
import json

e = Hash()
g = Grafo()
pensum = ListaSimple_Pensum()

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
        return e.detalles_apuntes(int(carnet), int(cod))
    
    def carga_masiva_pensum(self, ruta):
        file = open(ruta, 'r')
        datos = json.load(file)

        for i in datos["Cursos"]:
            if i["Codigo"] == "0101":
                g.insertar(i["Codigo"], i["Nombre"], str(i["Creditos"]), i["Prerequisitos"], str(i["Obligatorio"]))
            else:
                preq = i["Prerequisitos"].split(",")
                for j in preq:
                    g.insertar_adyacente(j, i["Codigo"], i["Nombre"], str(i["Creditos"]), i["Prerequisitos"], str(i["Obligatorio"]))
    
    def graficar_grafo(self):
        g.graficar()
    
    def carga_masiva_estudiante(self, ruta):
        file = open(ruta, 'r')
        datos = json.load(file)

        for i in datos["estudiantes"]:
            e.insertar(i["carnet"], i["DPI"], i["nombre"], i["carrera"], i["correo"], i["password"], i["edad"])
    
    def carga_masiva_apuntes(self, ruta):
        file = open(ruta, 'r')
        datos = json.load(file)

        for i in datos["usuarios"]:
            for j in i["apuntes"]:
                e.insertar_apunte(i["carnet"], j["Titulo"], j["Contenido"])
    
    def cursos_estudiantes(self, ruta):
        file = open(ruta, "r")
        datos = json.load(file)

        for i in datos["Estudiantes"]:
            for j in i["AÃ±os"]:
                for k in j["Semestres"]:
                    for l in k["Cursos"]:
                        e.insertar_anio(i["Carnet"], j["AÃ±o"])
                        e.insertar_semestre(i["Carnet"], j["AÃ±o"], k["Semestre"])
                        e.insertar_cursos(i["Carnet"], j["AÃ±o"], k["Semestre"], int(l["Codigo"]), l["Nombre"], l["Creditos"], l["Prerequisitos"], l["Obligatorio"])
    
    def graficar_arbolB(self, carnet, anio, semestre):
        e.graficar_arbolB(carnet, anio, semestre)
    
    def crear_cursosEstudiante(self, carnet, anio, semestre, codigo, nombre, creditos, prerequisitos, obligatorio):
        e.insertar_anio(carnet, anio)
        e.insertar_semestre(carnet, anio, semestre)
        e.insertar_cursos(carnet, anio, semestre, codigo, nombre, creditos, prerequisitos, obligatorio)
    
    def carga_cursosPensum(self, ruta):
        file = open(ruta, "r")
        datos = json.load(file)

        for i in datos["Cursos"]:
            pensum.insertar("pensum")
            pensum.insertar_cursos("pensum",int(i["Codigo"]), i["Nombre"], str(i["Creditos"]), i["Prerequisitos"], str(i["Obligatorio"]))
    
    def crear_cursosPensum(self, codigo, nombre, creditos, prerequisitos, obligatorio):
        pensum.insertar("pensum")
        pensum.insertar_cursos("pensum",codigo, nombre, creditos, prerequisitos, obligatorio)
    
    def graficar_arbolPensum(self):
        pensum.graficar_arbolPensum("pensum")