from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.wrappers import response
from Estructuras import CRUD

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

if __name__ == "__main__":
    app.run(debug = True, port = 3000, threaded = True)
