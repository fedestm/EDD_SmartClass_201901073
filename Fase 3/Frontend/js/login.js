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
                alert("Bienvenido")
                window.location.href = 'admin.html'
            }else if(datos.response == 0){
                alert("Bienvenido")
                localStorage.setItem("Usuario", usuario)
                window.location.href = 'smartclass.html'
            }else{
                alert("Error en usuario o contraseña")
            }
        })
    }
}