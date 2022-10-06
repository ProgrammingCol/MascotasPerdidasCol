

// VALIDACION DE LOS REQUISITOS MINIMOS DE LA COSNTRASEÑA

var myInput = document.getElementById("loginpsw");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");

// When the user clicks on the password field, show the message box
myInput.onfocus = function () {
    document.getElementById("message").style.display = "block";
}

// When the user clicks outside of the password field, hide the message box
myInput.onblur = function () {
    document.getElementById("message").style.display = "none";
}

// When the user starts to type something inside the password field
myInput.onkeyup = function () {
    // Validate lowercase letters
    var lowerCaseLetters = /[a-z]/g;
    if (myInput.value.match(lowerCaseLetters)) {
        letter.classList.remove("invalid");
        letter.classList.add("valid");
    } else {
        letter.classList.remove("valid");
        letter.classList.add("invalid");
    }

    // Validate capital letters
    var upperCaseLetters = /[A-Z]/g;
    if (myInput.value.match(upperCaseLetters)) {
        capital.classList.remove("invalid");
        capital.classList.add("valid");
    } else {
        capital.classList.remove("valid");
        capital.classList.add("invalid");
    }

    // Validate numbers
    var numbers = /[0-9]/g;
    if (myInput.value.match(numbers)) {
        number.classList.remove("invalid");
        number.classList.add("valid");
    } else {
        number.classList.remove("valid");
        number.classList.add("invalid");
    }

    // Validate length
    if (myInput.value.length >= 8) {
        length.classList.remove("invalid");
        length.classList.add("valid");
    } else {
        length.classList.remove("valid");
        length.classList.add("invalid");
    }
}


// VALIDACION EMAIL


let emailId = document.getElementById("loginEmail");
let errorMsg = document.getElementById("error-msg");
let icon = document.getElementById("icon");
let mailRegex = /^[a-zA-Z][a-zA-Z0-9\-\_\.]+@[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}$/;

function checker(){
    icon.style.display="inline-block";
// If your input email ID matches mailRegex then the codes below will be valid. 
// This means that an icon will be found here whose color will be green. 
//The error message cannot be viewed. 
//The border of the input space will be green.
    if(emailId.value.match(mailRegex)){
        icon.innerHTML = '<i class="fas fa-check-circle"></i>';
        icon.style.color = '#2ecc71';
        errorMsg.style.display = 'none';
        emailId.style.border = '2px solid #2ecc71';
    }
// Now I bet what kind of change can happen if you don't input anything instead of input.
// The icon will not be visible if you do not input anything. 
//Error message cannot be seen. 
//The border of the input will remain normal.
    else if(emailId.value == ""){
        icon.style.display = 'none';
        errorMsg.style.display = 'none';
        emailId.style.border = '2px solid #d1d3d4';
    }
//Now I have said what will change if the above two conditions do not work. 
//This means that if you input something and input it incorrectly, the following codes will work. 
//Here I have added the 'exclamation' icon and set the color of the icon to red. 
//The error message can be seen. 
//I have also instructed that the color of the border of the input should be red.
    else{
        icon.innerHTML = '<i class="fas fa-exclamation-circle"></i>';
        icon.style.color = '#ff2851';
        errorMsg.style.display = 'block';
        emailId.style.border = '2px solid #ff2851';
    }

}




// VALIDACION 3 INTETOS DE INGRESO

let attempt = 3;

function validate() {
    var usuar = document.getElementById("loginEmail").value;
    var password = document.getElementById("loginpsw").value;
    if (usuar == "admin@gamil.com" && password == "Pa123456") {
        alert("Ingreso exitososo");

        window.location = "../index.html";
        return 0;
    }
    if (usuar == "cliente@hotmail.com" && password == "accesoCL1") {
        alert("Ingreso exitososo");
        window.location = "../index.html?user=cliente";
        return 0;
    } else {
        attempt--;
    }
    if(attempt>0){
    alert(" Usuario o contraseña incorrecta. Te quedan " + attempt + " intentos mas ")}
    if (attempt <= 0) {
        alert('Espera 5 minutos para volver a intentarlo');
        document.getElementById("loginEmail").setAttribute('disabled', 'disabled');
        document.getElementById("loginpsw").setAttribute('disabled', 'disabled');
        document.getElementById("btnIngresar").setAttribute('disabled', 'disabled');
        setTimeout(function () {

            document.getElementById("loginEmail").removeAttribute('disabled');
            document.getElementById("loginpsw").removeAttribute('disabled');
            document.getElementById("btnIngresar").removeAttribute('disabled');

        }, 50000);

        attempt = 3;
    }
}