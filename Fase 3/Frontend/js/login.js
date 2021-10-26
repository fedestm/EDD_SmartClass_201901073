function login(){
    var usuario = document.getElementById("txtusuario").value
    var pass = document.getElementById("txtpassword").value

    if(usuario == "admin" && pass == "admin"){
        alert("Accedio como  administrador");
    }else{
        alert("Accedio como estudiante")
    }
}