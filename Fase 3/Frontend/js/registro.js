function registrar(){
    var carnet = document.getElementById("txtcarnet_registro").value
    var dpi = document.getElementById("txtdpi_registro").value
    var nombre = document.getElementById("txtnombre_registro").value
    var carrera = document.getElementById("txtcarrera_registro").value
    var correo = document.getElementById("txtcorreo_registro").value
    var password = document.getElementById("txtpassword_registro").value
    var edad = document.getElementById("txtedad_registro").value

    var datos = JSON.stringify({
        "carnet": carnet,
        "dpi": dpi,
        "nombre": nombre,
        "carrera": carrera,
        "correo": correo,
        "password": password,
        "edad": edad
    })


}