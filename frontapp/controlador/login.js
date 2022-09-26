
function login(){
    let user = document.loginform.user_name.value;
    let password = document.loginform.pass_word.value;
if(user == "" || pass == ""){
      alert("Por favor ingrese un usuario y contraseña");
 }else{
if((user == "ustut" || user == "USTUT") && password == "US@123"){
      document.loginform.submit();
}else{
     alert("Please Enter Correct Credentials");
}
   }
       }