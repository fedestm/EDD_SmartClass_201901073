from Analizador.Sintactico import parser

if __name__=="__main__":
    """
    entrada = open("C:/Users/User/Documents/GitHub/EDD_SmartClass_201901073/Fase 2/Estudiantes.txt","r")
    #print(entrada.read())
    mensaje=entrada.read()
    entrada.close()
    
    analizar = parser.parse(mensaje)
    """
    file = open("C:/Users/User/Documents/GitHub/EDD_SmartClass_201901073/Fase 2/CursosEstudiante.json","r")
    datos = json.load(file)