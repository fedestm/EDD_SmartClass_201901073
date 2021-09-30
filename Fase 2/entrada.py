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