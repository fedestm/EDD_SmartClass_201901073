from Analizador import parser
from Estructuras import avl
import json

a = avl()

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
            

