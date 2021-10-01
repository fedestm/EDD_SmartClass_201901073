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

@app.route("/")
def index():
    return "Ruta principal"

if __name__ == "__main__":
    app.run(debug = True, port = 3000, threaded = True)