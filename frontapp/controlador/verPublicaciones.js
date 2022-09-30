
//CODIGO PARA EL ZOOM DE LA IMAGEN
// Get the modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("myImg");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}




//CODIGO PARA MOSTRAR INFORMACION
function seeMore() {
  let publicacion1 = document.getElementById("myDIV");
  let publicacion2 = document.getElementById("myDIV2");
  let publicacion3 = document.getElementById("myDIV3");

  if (publicacion1.style.display === "block") {
    publicacion1.style.display = "none";
  } else {
    publicacion1.style.display = "block";
  }

  if (publicacion2.style.display === "block") {
    publicacion2.style.display = "none";
  } else {
    publicacion2.style.display = "block";
  }

  if (publicacion3.style.display === "block") {
    publicacion3.style.display = "none";
  } else {
    publicacion3.style.display = "block";
  }
}


//CODIGO PARA EDITAR INFORMACION
//function editar() {}




//CODIGO PARA ELIMINAR INFORMACION
//function eliminar() {}





//CODIGO PARA EL FILTRO

