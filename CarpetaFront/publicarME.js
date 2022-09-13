

const user = "vane"
const pw = 123456

function verificar() {
    let usuario = document.getElementById("usuario").value;
    let clave = document.getElementById("clave").value;
    let clave = document.getElementById("clave").value;
    let clave = document.getElementById("clave").value;
    let clave = document.getElementById("clave").value;
    let clave = document.getElementById("clave").value;
    if (usuario == user && clave == pw) {
        alert("loggin exitoso")
    } else {
        alert("Revise los datos ingresados")
    }
}