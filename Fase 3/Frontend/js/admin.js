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