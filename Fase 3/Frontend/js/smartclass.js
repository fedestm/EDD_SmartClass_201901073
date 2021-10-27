function storage_usuario(){
    var user = localStorage.getItem("Usuario")
    document.getElementById("txtcarnet").value = user
}