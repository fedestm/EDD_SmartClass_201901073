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
        

@app.route("/")
def index():
    return "Ruta principal"

if __name__ == "__main__":
    app.run(debug = True, port = 3000, threaded = True)