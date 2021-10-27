function storage_usuario(){
    var user = localStorage.getItem("Usuario")
    document.getElementById("txtcarnet").value = user
}

function insertar_apunte(){
    var carnet = document.getElementById("txtcarnet").value
    var titulo = document.getElementById("txttitulo").value
    var contenido = document.getElementById("txtcontenido").value

    var datos = JSON.stringify({
        "carnet": carnet,
        "titulo": titulo,
        "contenido": contenido
    });

    fetch('http://localhost:3000/insertar_apunte', {
        method: 'post',
        headers:{
            'Content-Type': 'application/json'
        },
        body: datos
    })
    .then(response => response.json())
    .then(datos => {
        console.log(datos)
    alert(datos.response)
    })
}