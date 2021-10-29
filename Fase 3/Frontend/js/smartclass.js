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

function vista_apuntes(){
    var user = localStorage.getItem("Usuario")
    document.getElementById("txtcarnet").value = user

    fetch('http://localhost:3000/vista_apuntes/' + user, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .catch(err => {
        console.log(err)
    }).then(response => {
        var apuntes = response;
        var tabla = document.querySelector("#tabla_vista_apunte")

        apuntes.forEach(apuntes => {
            tabla.innerHTML += `<tr><td>${apuntes.titulo}</td><td>${apuntes.titulo}</td>
            <td><a href = "ver_apunte.html?id=${apuntes.id}"><button class = "btn_verapunte" type = "button">Ver Apunte</button></a>
            </td></tr>`
        })
    })
}

function ver_apunte(){
    var queryString = window.location.search;
    var urlParams = new URLSearchParams(queryString)
    var id = urlParams.get('id')

    var user = localStorage.getItem("Usuario")
    document.getElementById("txtcarnet").value = user

    fetch('http://localhost:3000/detalles_apunte/' + user + '/' + id, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .catch(err => {
        console.log("Error al mostrar detalle de apunte")
    }).then(apunte => {
        console.log(apunte.titulo)
        console.log(apunte.contenido)
        document.getElementById("txttitulo").value = apunte.titulo
        document.getElementById("txtcontenido").value = apunte.contenido
    })
}