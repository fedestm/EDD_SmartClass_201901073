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

function storage_usuario_asignar(){
    var user = localStorage.getItem("Usuario")
    document.getElementById("txtcarnet_asignar").value = user
}

function asignar_curso(){
    var carnet = document.getElementById("txtcarnet_asignar").value
    var anio = document.getElementById("txtanio_asignar").value
    var semestre = document.getElementById("txtsemestre_asignar").value
    var codigo = document.getElementById("txtcodigo_asignar").value
    var nombre = document.getElementById("txtnombre_asignar").value
    var creditos = document.getElementById("txtcreditos_asignar").value
    var prereq = document.getElementById("txtprereq_asignar").value
    var obligatorio = document.getElementById("txtobligatorio_asignar").value

    var datos = JSON.stringify({
        "carnet": carnet,
        "anio": anio,
        "semestre": semestre,
        "codigo": codigo,
        "nombre": nombre,
        "creditos": creditos,
        "prerequisitos": prereq,
        "obligatorio": obligatorio
    });

    fetch('http://localhost:3000/insertar_curso', {
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

function reporte_arbolB(){
    var carnet = document.getElementById("txtcarnet_asignar").value
    var anio = document.getElementById("txtanio_asignar").value
    var semestre = document.getElementById("txtsemestre_asignar").value

    fetch('http://localhost:3000/graficar_arbolB/' + carnet + '/' + anio + '/' + semestre, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        img = data.img
        document.getElementById("img").innerHTML = "<img src = \"data:image/png;base64," + img + "\">"
        console.log(img)
    })
}