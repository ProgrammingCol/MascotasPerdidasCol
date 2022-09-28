

// 


function login() {
    let correo = document.getElementById("loginEmail").value;
    let password = document.getElementById("loginpsw").value;
    
    if (correo == "" || password == "") {
        alert("Por favor ingrese un usuario y una contraseña");
    } else if ((correo == "admin" || correo == "ADMIN") && password == "US@123") {
        exitoso()      
    }
}


function exitoso() {
    const open = document.getElementById('open');
    const modal_container = document.getElementById('modal_container');
    const close = document.getElementById('close');

    open.addEventListener('click', () => {
        modal_container.classList.add('show');
    });

    close.addEventListener('click', () => {
        modal_container.classList.remove('show');
    });
}
