from flask import Flask,make_response,jsonify,request

app=Flask(__name__)

@app.route("/carga",methods=["POST"])
def carga_masiva():
    if request.method=="POST":
        tipo=request.form.get('tipo')
        path=request.form.get('path')

        return tipo +" "+ path

@app.route("/")
def index():
    return "Ruta principal"

if __name__=="__main__":
    app.run(debug=True,port=3000,threaded=True)