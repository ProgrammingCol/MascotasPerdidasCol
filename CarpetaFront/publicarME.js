
const condbase = 0;

function revisar() {
    let condiciones = document.getElementById("condiciones").value;

    if (condiciones !== condbase) {
        alert("Revisa que tus datos sean correctos antes de dar click en Enviar");
    }
    else if(document.getElementById('condiciones').checked==true){
        alert("Revisa que tus datos sean correctos antes de dar click en Enviar");
    }} 
