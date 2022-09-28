


//Mostrar campos requeridos para la contraseña
function myFocusFunction() {
    document.getElementById("loginEmail").style.backgroundColor = "yellow";
  }



//revisar contraseña que contenga de 6 a 12 caracteres 
function CheckPassword(inputtxt) 
{ 
let passw=  /^[A-Za-z]\w{6,12}$/;
if(inputtxt.value.match(passw)) 
{ 
alert('Correct, try another...')
return true;
}
else
{ 
alert('Wrong...!')
return false;
}
}