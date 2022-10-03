let form = document.getElementById("formPost");
let nombrem = document.getElementById("nombrem");
let especie = document.getElementById("especie");
let raza = document.getElementById("raza");
let sexo = document.getElementById("sexo");
let estado = document.getElementById("estado");
let descripcion = document.getElementById("descripcion");
let msg = document.getElementById("msg");
let posts = document.getElementById("posts");


//VALIDACION DE ESPACIOS EN BLANCO





  let formValidation = () => {
    if (descripcion.value === "") {
        msg.innerHTML = "Post cannot be blank";
        console.log("failure");
    } else {
        console.log("successs");
        msg.innerHTML = "";
        let data = {};
        acceptData();
    }
};

