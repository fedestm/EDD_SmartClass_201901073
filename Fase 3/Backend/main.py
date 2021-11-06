from flask import Flask, request, jsonify
from flask_cors import CORS
from Estructuras import CRUD
import base64

crud = CRUD()

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

@app.route("/insertar_estudiante", methods = ['POST'])
def insertar_estudiante():
    if request.method == 'POST':
        carnet = request.json['carnet']
        dpi = request.json['dpi']
        nombre = request.json['nombre']
        carrera = request.json['carrera']
        correo = request.json['correo']
        password = request.json['password']
        edad = request.json['edad']
        crud.registrar_estudiante(carnet, dpi, nombre, carrera, correo, password, edad)
        response = jsonify({'response': 'Se registro estudiante'})
        return response

@app.route("/login", methods = ['POST'])
def login():
    if request.method == 'POST':
        usuario = request.json['usuario']
        password = request.json['pass']

        if usuario == 'admin' and password == 'admin':
            response = jsonify({'response': 1})
            return response
        else:
            estudiante = crud.buscar_usuario(usuario, password)
            if estudiante is not False:
                #Retorna 0 si el carnet esta registrado
                response = jsonify({'response': 0})
                return response
            else:
                #Retorna 2 si no existe usuario registrado
                response = jsonify({'response': 2})
                return response

@app.route("/insertar_apunte", methods = ['POST'])
def insertar_apunte():
    if request.method == 'POST':
        carnet = request.json['carnet']
        titulo = request.json['titulo']
        contenido = request.json['contenido']
        crud.insertar_apunte(carnet, titulo, contenido)
        response = jsonify({'response': 'Se registro apunte'})
        return response

@app.route("/graficar_hash", methods = ['GET'])
def graficar_hash():
    if request.method == 'GET':
        crud.graficar_hash()
        b64_str = ""
        with open("hash.png", "rb") as img:
            b64_str = base64.b64encode(img.read())
        response = jsonify({'response': 'Se grafico Tabla', 'img': str(b64_str.decode('utf-8'))})
        return response

@app.route("/vista_apuntes/<carnet>", methods = ['GET'])
def vista_apuntes(carnet):
    if request.method == 'GET':
        return crud.vista_apuntes(carnet)

@app.route("/detalles_apunte/<carnet>/<cod>", methods = ['GET'])
def detalles_apunte(carnet, cod):
    if request.method == 'GET':
        return crud.detalles_apuntes(carnet, cod)

@app.route("/carga_masiva", methods = ['POST'])
def carga_masiva():
    if request.method == 'POST':
        tipo = request.json["tipo"]
        path = request.json["path"]

        try:
            if tipo == "curso":
                crud.carga_masiva_pensum(path)
                return {
                    "Estado": 200,
                    "Mensaje": "Se insertaron los cursos"
                }
            elif tipo == "estudiantes":
                crud.carga_masiva_estudiante(path)
                return {
                    "Estado": 200,
                    "Mensaje": "Se insertaron los estudiantes"
                }
            elif tipo == "apuntes":
                crud.carga_masiva_apuntes(path)
                return {
                    "Estado": 200,
                    "Mensaje": "Se insertaron apuntes"
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

@app.route("/graficar_grafo", methods = ['GET'])
def graficar_grafo():
    if request.method == 'GET':
        crud.graficar_grafo()
        b64_str = ""
        with open("grafo.png", "rb") as img:
            b64_str = base64.b64encode(img.read())
        response = jsonify({'response': 'Se grafico Grafo', 'img': str(b64_str.decode('utf-8'))})
        return response

@app.route("/insertar_curso", methods = ['POST'])
def insertar_curso():
    if request.method == 'POST':
        carnet = request.json['carnet']
        anio = request.json['anio']
        semestre = request.json['semestre']
        codigo = request.json['codigo']
        nombre = request.json['nombre']
        creditos = request.json['creditos']
        prerequisitos = request.json['prerequisitos']
        obligatorio = request.json['obligatorio']
        crud.crear_cursosEstudiante(carnet, anio, semestre, codigo, nombre, creditos, prerequisitos, obligatorio)
        response = jsonify({'response': 'Se registro el curso'})
        return response

@app.route("/graficar_arbolB/<carnet>/<anio>/<semestre>", methods = ['GET'])
def graficar_arbolB(carnet, anio, semestre):
    if request.method == 'GET':
        crud.graficar_arbolB(carnet, anio, semestre)
        b64_str = ""
        with open("arbolB.png", "rb") as img:
            b64_str = base64.b64encode(img.read())
        response = jsonify({'response': 'Se grafico Arbol B', 'img': str(b64_str.decode('utf-8'))})
        return response

if __name__ == "__main__":
    app.run(debug = True, port = 3000, threaded = True)
