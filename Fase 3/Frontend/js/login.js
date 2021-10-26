function login(){
    var usuario = document.getElementById("txtusuario").value
    var pass = document.getElementById("txtpassword").value

    datos = JSON.stringify({
        'usuario': usuario,
        'pass': pass
    })

    if(usuario != '' && pass != ''){
        fetch('http://localhost:3000/login', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: datos
        })
        .then(response => response.json())
        .then(datos => {
            console.log(datos)
            if(datos.response == 1){
                window.location.href = 'admin.html'
            }else{
                window.location.href = 'smartclass.html'
            }
        })
    }
}