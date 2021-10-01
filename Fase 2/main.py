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
            elif tipo == 4:
                carnet = str(reportes["carnet"])
                anio = str(reportes["anio"])
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

@app.route("/")
def index():
    return "Ruta principal"

if __name__ == "__main__":
    app.run(debug = True, port = 3000, threaded = True)