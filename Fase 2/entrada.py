from Analizador.Sintactico import parser
import json

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

    for i in datos["Estudiantes"]:
        print(i["Carnet"],end="\n")
        for j in i["AÃ±os"]:
            print(j["AÃ±o"])
            for k in j["Semestres"]:
                print("Semestre: ",end=k["Semestre"] + "\n")
                for l in k["Cursos"]:
                    print(l)
        
        print("\n")
    
    file.close()