function reporte_hash(){
    fetch('http://localhost:3000/graficar_hash', {
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

function reporte_grafo(){
    fetch('http://localhost:3000/graficar_grafo', {
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

function crear_cursoPensum(){
    var codigo = document.getElementById("txtcodigo_asignar").value
    var nombre = document.getElementById("txtnombre_asignar").value
    var creditos = document.getElementById("txtcreditos_asignar").value
    var prereq = document.getElementById("txtprereq_asignar").value
    var obligatorio = document.getElementById("txtobligatorio_asignar").value

    var datos = JSON.stringify({
        "codigo": codigo,
        "nombre": nombre,
        "creditos": creditos,
        "prerequisitos": prereq,
        "obligatorio": obligatorio
    });

    fetch('http://localhost:3000/insertar_cursoPensum', {
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

function reporte_arbolPensum(){
    fetch('http://localhost:3000/graficar_arbolPensum', {
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