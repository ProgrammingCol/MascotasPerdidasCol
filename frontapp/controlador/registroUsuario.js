const pnombre = document.getElementById("pnombre");
const snombre = document.getElementById("snombre");
const papellido = document.getElementById("papellido");
const sapellido = document.getElementById("sapellido");
const email = document.getElementById("correo");
const telefono = document.getElementById("telefono");
const ciudad = document.getElementById("ciudad");
const dpto = document.getElementById("dpto");
const user = document.getElementById("user");
const password = document.getElementById("crearClave");
const form = document.getElementById("form");
const msg = document.getElementById("msg");


// Function to validate the email
const validateEmail = (inputEmail)=> inputEmail.value.match(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);;
// Function to validate password
const validatePassword = (inputPassword)=> inputPassword.value.match(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
// Function to validate names
const validateName = (inputName)=> inputName.value.match(/^[a-zA-Z]{4,15}+$/);
// Function to validate userId
const validateUser = (inputUser)=> inputUser.value.match(/^w{4,8}$/);
// Function to validate phone
const validatePhone = (inputPhone)=> inputPhone.value.match(/^\d{3}-\d{3}-\d{4}$/);



// Function used to display errors
const generateError = (errorName, errorMsg) =>{
    const emailError = document.getElementById("emailError");
    const passwordError = document.getElementById("passwordError");
    const pnombreError = document.getElementById("pnombreError");
    const snombreError = document.getElementById("snombreError");
    const papellidoError = document.getElementById("papellidoError");
    const sapellidoError = document.getElementById("sapellidoError");
    const telefonoError = document.getElementById("telefonoError");
    const ciudadError = document.getElementById("ciudadError");
    const dptoError = document.getElementById("dptoError");
    const userError = document.getElementById("userError");


    if(errorName == "email"){
        emailError.innerText = errorMsg;    
    }else if(errorName == "password"){
        passwordError.innerText = errorMsg;
    }else if(errorName == "pnombre") {
      pnombreError.innerText = errorMsg;
    }else if (errorName == "snombre") {
      snombreError.innerText = errorMsg;
    }    else if (errorName == "papellido") {
      papellidoError.innerText = errorMsg;
    }else if (errorName == "sapellido") {
      sapellidoError.innerText = errorMsg;
    }else if (errorName == "telefono") {
      telefonoError.innerText = errorMsg;
    }else if (errorName == "ciudad") {
      ciudadError.innerText = errorMsg;
    }else if (errorName == "dpto") {
      dptoError.innerText = errorMsg;
    }else if (errorName == "user") {
      userError.innerText = errorMsg;
    }
    
}

const formValidate = (inputEmail, inputPassword, inputName) =>{
    if(!validateEmail(inputEmail)){
        emailError = "please enter a valid email address";
        generateError("email",emailError);
        return;
    }
    if(!validatePassword(inputPassword)){
        passwordError = "please enter correct password";
        generateError(generateError("password",passwordError));
        return;
    }    
    if (!validateName(inputName)) {
      pnombreError = "Por favor ingrese un nombre valido";
      generateError(generateError("pnombre", pnombreError));
      return;
    }
    if (!validateName(inputName)) {
      snombreError = "Por favor ingrese un nombre valido";
      generateError(generateError("snombre", snombreError));
      return;
    }
    if (!validateName(inputName)) {
      papellidoError = "Por favor ingrese un apellido valido";
      generateError(generateError("papellido", papellidoError));
      return;
    }
    if (!validateName(inputName)) {
      sapellidoError = "Por favor ingrese un apellido valido";
      generateError(generateError("sapellido", sapellidoError));
      return;
    }
  
    if (!validatePhone(inputPhone)) {
      telefonoError = "Por favor ingrese un número de teléfono valido";
      generateError(generateError("telefono", telefonoError));
      return;
    }
    if (!validateName(inputName)) {
      ciudadError = "Por favor ingrese una Ciudad valid";
      generateError(generateError("ciudad", ciudadError));
      return;
    }
    if (!validateName(inputName)) {
      dptoError = "Por favor ingrese un Departamento valid";
      generateError(generateError("dpto", dptoError));
      return;
    }
    if (!validateUser(inputUser)) {
      userError = "Por favor ingrese un Id de usuario valido";
      generateError(generateError("user", userError));
      return;
    }
  
}

//triggers when user submits the form
form.addEventListener("submit",(e) => {
    e.preventDefault();
    formValidate(email, password, pnombre, snombre, papellido, sapellido, telefono, ciudad, dpto, user);
});

// Focusout event listener. Triggers when the user clicks anywhere else besides the input
email.addEventListener("focusout", (e)=>{
    if(!validateEmail(email)){
        email.style.borderColor = "red";
        generateError("email", "Por favor ingrese un nombre valido");
        email.parentElement.classList.add("error");
    }
});

// Focusout event listener triggers when the user clicks anywhere else besides the input
password.addEventListener("focusout", (e)=>{
    if(!validatePassword(password)){
        password.style.borderColor = "red";
        generateError("password", "Por favor ingrese una clave valida");
        password.parentElement.classList.add("error");
    }
});

// Focusout event listener. Triggers when the user clicks anywhere else besides the input
pnombre.addEventListener("focusout", (e) => {
  if (!validateName(pnombre )) {
    pnombre.style.borderColor = "red";
    generateError("pnombre", "Por favor ingrese un nombre valido");
    pnombre.parentElement.classList.add("error");
  }
});

// Focusout event listener. Triggers when the user clicks anywhere else besides the input
snombre.addEventListener("focusout", (e) => {
  if (!validateName(snombre)) {
    snombre.style.borderColor = "red";
    generateError("snombre", "Por favor ingrese un nombre valido");
    snombre.parentElement.classList.add("error");
  }
});

// Focusout event listener. Triggers when the user clicks anywhere else besides the input
papellido.addEventListener("focusout", (e) => {
  if (!validateName(papellido)) {
    papellido.style.borderColor = "red";
    generateError("papellido", "Por favor ingrese un apellido valido");
    papellido.parentElement.classList.add("error");
  }
});
// Focusout event listener. Triggers when the user clicks anywhere else besides the input
sapellido.addEventListener("focusout", (e) => {
  if (!validateName(sapellido)) {
    sapellido.style.borderColor = "red";
    generateError("sapellido", "Por favor ingrese un apellido valido");
    sapellido.parentElement.classList.add("error");
  }
});

// Focusout event listener. Triggers when the user clicks anywhere else besides the input
telefono.addEventListener("focusout", (e) => {
  if (!validatetelefono(telefono)) {
    telefono.style.borderColor = "red";
    generateError("telefono", "Por favor ingrese un número de teléfono valido");
    telefono.parentElement.classList.add("error");
  }
});
// Focusout event listener. Triggers when the user clicks anywhere else besides the input
ciudad.addEventListener("focusout", (e) => {
  if (!validateName(ciudad)) {
    ciudad.style.borderColor = "red";
    generateError("ciudad", "Por favor ingrese una ciudad valida");
    ciudad.parentElement.classList.add("error");
  }
});

// Focusout event listener. Triggers when the user clicks anywhere else besides the input
dpto.addEventListener("focusout", (e) => {
  if (!validateName(dpto)) {
    dpto.style.borderColor = "red";
    generateError("dpto", "Por favor ingrese un departamento valido");
    dpto.parentElement.classList.add("error");
  }
});
// Focusout event listener. Triggers when the user clicks anywhere else besides the input
user.addEventListener("focusout", (e) => {
  if (!validateUser(user)) {
    user.style.borderColor = "red";
    generateError("user", "Por favor ingrese un id de usuario valido");
    user.parentElement.classList.add("error");
  }
});