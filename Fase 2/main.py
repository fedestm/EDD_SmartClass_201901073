from flask import Flask, make_response, jsonify, request
from entrada import CRUD
crud = CRUD()

app = Flask(__name__)


@app.route("/carga", methods = ["POST"])
def carga_masiva():
    if request.method == "POST":
        carga = request.get_json()
        tipo = carga["tipo"]
        path = carga["path"]

        try:
            if tipo == "estudiante":
                crud.cargar_estudiantes(path)
                return {
                    "Estado": 200,
                    "Mensaje": "Se insertaron los estudiantes"
                }
            elif tipo == "recordatorio":
                crud.cargar_recordatorios(path)
                return {
                    "Estado": 200,
                    "Mensaje": "Se insertaron las tareas"
                }
            elif tipo == "curso":
                crud.cursos_estudiantes(path)
                return {
                    "Estado": 200,
                    "Mensaje": "Se insertaron cursos de estudiante"
                }
            elif tipo == "curso_pensum":
                crud.carga_cursosPensum(path)
                return {
                    "Estado": 200,
                    "Mensaje": "Se insertaron curso de pensum"
                }
        except:
            return {
                "Estado": 404,
                "Mensaje": "Error al insertar"
            }

@app.route("/reporte", methods = ["POST"])
def reportes():
    if request.method == "POST":
        reportes = request.get_json()
        tipo = reportes["tipo"]

        try:
            if tipo == 0:
                crud.graficar_avl()
                return {
                    "Estado": 200,
                    "Mensaje": "Se cargo arbol avl"
                }
            elif tipo == 1:
                carnet = str(reportes["carnet"])
                anio = str(reportes["año"])
                mes = str(reportes["mes"])
                crud.graficar_matriz(carnet, anio, mes)
                return {
                    "Estado": 200,
                    "Mensaje": "Se grafico matriz dispersa"
                }
            elif tipo == 2:
                carnet = str(reportes["carnet"])
                anio = str(reportes["año"])
                mes = str(reportes["mes"])
                dia = int(reportes["dia"])
                hora = int(reportes["hora"])
                crud.graficar_lista_tareas(carnet, anio, mes, dia, hora)
                return {
                    "Estado": 200,
                    "Mensaje": "Se grafico lista de tareas"
                }
            elif tipo == 3:
                crud.graficar_arbolPensum()
                return {
                    "Estado": 200,
                    "Mensaje": "Se grafico Arbol B de pensum de cursos"
                }
            elif tipo == 4:
                carnet = str(reportes["carnet"])
                anio = str(reportes["año"])
                semestre = str(reportes["semestre"])
                crud.graficar_arbolB(carnet, anio, semestre)
                return {
                    "Estado": 200,
                    "Mensaje": "Se grafico Arbol B"
                }
        except:
            return {
                "Estado": 404,
                "Mensaje": "Error al graficar"
            }

@app.route("/recordatorios", methods = ["POST", "GET", "UPDATE", "DELETE"])
def recordatorios():
    if request.method == "DELETE":
        try:
            recordatorios = request.get_json()
            carnet = recordatorios["Carnet"]
            fecha = recordatorios["Fecha"]
            hora = recordatorios["Hora"]
            crud.eliminar_recordatorio(carnet, fecha, hora)
            return {
                "Estado": 200,
                "Mensaje": "Se elimino el recordatorio"
            }
        except:
            return {
                "Estado": 404,
                "Mensaje": "Error al eliminar"
            }
    elif request.method == "POST":
        try:
            recordatorios = request.get_json()
            carnet = recordatorios["Carnet"]
            nombre = recordatorios["Nombre"]
            desc = recordatorios["Descripcion"]
            materia = recordatorios["Materia"]
            fecha = recordatorios["Fecha"]
            hora = recordatorios["Hora"]
            estado = recordatorios["Estado"]

@app.route("/")
def index():
    return "Ruta principal"

if __name__ == "__main__":
    app.run(debug = True, port = 3000, threaded = True)