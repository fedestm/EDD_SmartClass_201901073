from flask import Flask, request, jsonify
from flask_cors import CORS
from Estructuras import CRUD

crud = CRUD

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)



