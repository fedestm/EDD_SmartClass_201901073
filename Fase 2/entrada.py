from Analizador import parser
from Estructuras import avl
from Estructuras import ListaSimple_Pensum
import json

a = avl()
pensum = ListaSimple_Pensum()

class CRUD:
    def cargar_estudiantes(self, ruta):
        entrada = open(ruta)
        data = entrada.read()
        entrada.close()
        analizar = parser.parse(data)

        atrib = ""
        t = ""
        for i in analizar:
            if i["type"] == "user":
                atrib += str(i["atributos"])
                t = atrib.replace("][",",").replace("}, {",",").replace("\"","")
        #Se convierte string a json
        estudiantes = eval(t)

        for i in estudiantes:
            a.insertar(i["Carnet"], i["DPI"], i["Nombre"], i["Carrera"], i["Password"], i["Creditos"], i["Edad"])
    
    def cargar_recordatorios(self, ruta):
        entrada = open(ruta)
        data = entrada.read()
        entrada.close()
        analizar = parser.parse(data)

        atrib = ""
        t = ""
        for i in analizar:
            if i["type"] == "task":
                atrib += str(i["atributos"])
                t = atrib.replace("][",",").replace("}, {",",").replace("\"","")
        tareas = eval(t)

        for i in tareas:
            fecha = i["Fecha"].split("/")
            dia = int(fecha[0])
            mes = int(fecha[1])
            anio = int(fecha[2])
            hora = i["Hora"].split(":")
            a.insertar_anio(i["Carnet"], str(anio))
            a.insertar_meses(i["Carnet"], str(anio), str(mes))
            a.insertar_mes_matriz(i["Carnet"], str(anio), str(mes), int(dia), int(hora[0]))
            a.insertar_tareas_matriz(i["Carnet"], str(anio), str(mes), int(dia), int(hora[0]), i["Carnet"], i["Nombre"], i["Descripcion"], i["Materia"], i["Fecha"], i["Hora"], i["Estado"])
    
    def graficar_avl(self):
        a.graficar()
    
    def graficar_matriz(self, carnet, anio, mes):
        a.graficar_matriz(carnet, anio, mes)
    
    def cursos_estudiantes(self, ruta):
        file = open(ruta, "r")
        datos = json.load(file)

        for i in datos["Estudiantes"]:
            for j in i["AÃ±os"]:
                for k in j["Semestres"]:
                    for l in k["Cursos"]:
                        a.insertar_anio(i["Carnet"], j["AÃ±o"])
                        a.insertar_semestre(i["Carnet"], j["AÃ±o"], k["Semestre"])
                        a.insertar_cursos(i["Carnet"], j["AÃ±o"], k["Semestre"], int(l["Codigo"]), l["Nombre"], l["Creditos"], l["Prerequisitos"], l["Obligatorio"])

    def graficar_arbolB(self, carnet, anio, semestre):
        a.graficar_arbolB(carnet, anio, semestre)
    
    def graficar_lista_tareas(self, carnet, anio, mes, dia, hora):
        a.graficar_lista_tareas(carnet, anio, mes, dia, hora)
    
    def carga_cursosPensum(self, ruta):
        file = open(ruta, "r")
        datos = json.load(file)

        for i in datos["Cursos"]:
            pensum.insertar("pensum")
            pensum.insertar_cursos("pensum",int(i["Codigo"]), i["Nombre"], str(i["Creditos"]), i["Prerequisitos"], str(i["Obligatorio"]))
    
    def graficar_arbolPensum(self):
        pensum.graficar_arbolPensum("pensum")







