

//evento de carga de la página
//codigo para recorre mascotas y consumir api
document.addEventListener("DOMContentLoaded",() => {

  const mascotasContainer = document.querySelector("#mascotasContainer");


fetch('./data/Mascotas.json')

.then(response => response.json())

.then(data => {
  data.array.forEach(mascota => {
  mascotasContainer.innerHTML +=`
  <div class="col-md-3 publicacion" id="mascotasContainer">
  <div class="card text-center flip-card">
      <img id="myImg" src="./Assets/${mascota.id}" alt="Contacto: 3107729052" class="card-img-top imgpublication">

      <div class="card-body bg-opacity-10 bg-black">

          <button title="ver más información" id="btnInformacion" class="btnpublicacion" onclick="seeMore()"><img
                  src="img/informacionPubli.png" class=" card-footer iconosFoto" ></button>

          <button title="Editar publicación" id="btnEditar" class="btnpublicacion"onClick="editPost(this)" ><img
                  src="img/editarPubli.png" class=" card-footer iconosFoto " ></button>

          <button title="Eliminar publicación" id="btnEliminar" class="btnpublicacion" onClick="deletePost(this)"><span><img
                      src="img/eliminarPubli.png" class=" card-footer iconosFoto" ></span></button>
      </div>
      <!-- The Modal to zoom image -->
      <div id="myModal" class="modal">

          <!-- The Close Button -->
          <span class="close">&times;</span>

          <!-- Modal Content (The Image) -->
          <img class="modal-content" id="img01">

          <!-- Modal Caption (Image Text) -->
          <div id="caption"></div>
      </div>
      <div id="myDIV1" class="moreInfo">
          <h6 class="title">${mascota.nombreMascota}</h6>
          <p class="caracteristica">Raza: <span class="mascotaDatos" id="razaInfo">${mascota.raza}</span></p>
          <p class="caracteristica">Sexo: <span class="mascotaDatos" id="sexoInfo">${mascota.sexo}</span></p>
          <p class="caracteristica">Estado: <span class="mascotaDatos" id="ciudadInfo">${mascota.estado}</span></p>
          <p class="caracteristica" id="parrafo">Especie<span class="mascotaDatos" id="especieInfo">${mascota.descripcion}</span></p>
      </div>
  </div>
  `
    
  });
  console.log(data);
})
})






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
function seeMore(idElemento) {
  let myDIV = document.getElementById(idElemento);

  if (myDIV.style.display === "block") {
    myDIV.style.display = "none";
  } else {
    myDIV.style.display = "block";
  }
}


//CODIGO PARA EDITAR INFORMACION
//function editar() {}




//CODIGO PARA ELIMINAR INFORMACION
//function eliminar() {}





//CODIGO PARA EL FILTRO



//codigo para la peticion

