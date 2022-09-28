

const pnombre = document.getElementById("pnombre");
const snombre = document.getElementById("snombre");
const papellido = document.getElementById("papellido");
const sapellido = document.getElementById("sapellido");
const email = document.getElementById("correo");
const phone = document.getElementById("telefono");
const ciudad = document.getElementById("ciudad");
const dpto = document.getElementById("departamento");
const user = document.getElementById("idusuario");
const password = document.getElementById("crearClave");
const form = document.getElementById("form");
const msg = document.getElementById("msg");

// Function to validate the email
const validateEmail = (inputEmail) => inputEmail.value.match(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);

// Function to validate password
const validatePassword = (inputPassword) => inputPassword.value.match(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);

// Function to validate names
const validateName = (inputNames) => inputNames.value.match(/^[A-Za-z]+/);

// Function to validate userId
const validateUser = (inputUser) => inputUser.value.match(/^\w+/)

// Function to validate phone
const validatephone = (inputPhone) => inputPhone.value.match(/^\\(?([0-9]{3})\\)?[-.\\s]?([0-9]{3})[-.\\s]?([0-9]{4})$/);


// Function used to display errors
const generateError = (errorName, errorMsg) => {
  const emailError = document.getElementById("emailError");
  const passwordError = document.getElementById("passwordError");
  if (errorName == "email") {
    emailError.innerText = errorMsg;
  } else if (errorName == "password") {
    passwordError.innerText = errorMsg;
  }
}

const formValidate = (inputEmail, inputPassword,inputNames,inputUser,inputPhone) => {
  if (!validateName(inputNames)) {
    passwordError = "Por favor ingrese un nombre valido";
    generateError(generateError("pnombre", pnombreError));
    return;
  }
  if (!validateName(inputNames)) {
    passwordError = "Por favor ingrese un nombre valido";
    generateError(generateError("snombre", snombreError));
    return;
  }
  if (!validateName(inputNames)) {
    passwordError = "Por favor ingrese un apellido valido";
    generateError(generateError("papellido", papellidoError));
    return;
  }
  if (!validateName(inputNames)) {
    passwordError = "Por favor ingrese un apellido valido";
    generateError(generateError("sapellido", sapellidoError));
    return;
  }
  if (!validateEmail(inputEmail)) {
    emailError = "please enter a valid email address";
    generateError("email", emailError);
    return;
  }
  if (!validatephone(inputPhone)) {
    passwordError = "Por favor ingrese un número de teléfono valido";
    generateError(generateError("phone", telefonoError));
    return;
  }
  if (!validateName(inputNames)) {
    passwordError = "please enter correct password";
    generateError(generateError("ciudad", ciudadError));
    return;
  }
  if (!validateName(inputNames)) {
    passwordError = "please enter correct password";
    generateError(generateError("dpto", dptoError));
    return;
  }
  if (!validateUser(inputUser)) {
    passwordError = "please enter correct password";
    generateError(generateError("user", passwordError));
    return;
  }
  if (!validatePassword(inputPassword)) {
    passwordError = "please enter correct password";
    generateError(generateError("password", idUsuarioError));
    return;
  }

}

//triggers when user submits the form
form.addEventListener("submit", (e) => {
  e.preventDefault();
  formValidate(email, password, pnombre, snombre, papellido, sapellido, phone, ciudad, dpto, user);
});


// Focusout event listener. Triggers when the user clicks anywhere else besides the input
email.addEventListener("focusout", (e) => {
  if (!validateName(email)) {
    email.style.borderColor = "red";
    generateError("email", "Please enter a valid email");
    email.parentElement.classList.add("error");
  }
});

// Focusout event listener. Triggers when the user clicks anywhere else besides the input
email.addEventListener("focusout", (e) => {
  if (!validateName(email)) {
    email.style.borderColor = "red";
    generateError("email", "Please enter a valid email");
    email.parentElement.classList.add("error");
  }
});
// Focusout event listener. Triggers when the user clicks anywhere else besides the input
email.addEventListener("focusout", (e) => {
  if (!validateName(email)) {
    email.style.borderColor = "red";
    generateError("email", "Please enter a valid email");
    email.parentElement.classList.add("error");
  }
});
// Focusout event listener. Triggers when the user clicks anywhere else besides the input
email.addEventListener("focusout", (e) => {
  if (!validateName(email)) {
    email.style.borderColor = "red";
    generateError("email", "Please enter a valid email");
    email.parentElement.classList.add("error");
  }
});
// Focusout event listener. Triggers when the user clicks anywhere else besides the input
email.addEventListener("focusout", (e) => {
  if (!validateEmail(email)) {
    email.style.borderColor = "red";
    generateError("email", "Please enter a valid email");
    email.parentElement.classList.add("error");
  }
});
// Focusout event listener. Triggers when the user clicks anywhere else besides the input
email.addEventListener("focusout", (e) => {
  if (!validatephone(email)) {
    email.style.borderColor = "red";
    generateError("email", "Please enter a valid email");
    email.parentElement.classList.add("error");
  }
});
// Focusout event listener. Triggers when the user clicks anywhere else besides the input
email.addEventListener("focusout", (e) => {
  if (!validateName(email)) {
    email.style.borderColor = "red";
    generateError("email", "Please enter a valid email");
    email.parentElement.classList.add("error");
  }
});

// Focusout event listener. Triggers when the user clicks anywhere else besides the input
email.addEventListener("focusout", (e) => {
  if (!validateName(email)) {
    email.style.borderColor = "red";
    generateError("email", "Please enter a valid email");
    email.parentElement.classList.add("error");
  }
});
// Focusout event listener. Triggers when the user clicks anywhere else besides the input
email.addEventListener("focusout", (e) => {
  if (!validateUser(email)) {
    email.style.borderColor = "red";
    generateError("email", "Please enter a valid email");
    email.parentElement.classList.add("error");
  }
});
// Focusout event listener. Triggers when the user clicks anywhere else besides the input
password.addEventListener("focusout", (e) => {
  if (!validatePassword(password)) {
    password.style.borderColor = "red";
    generateError("password", "Please enter a valid password");
    password.parentElement.classList.add("error");
  }
});