$( "form" ).submit(function( event ) {
  event.preventDefault();
  var form = $(this);
  $.ajax({
    url: form.attr("action"),
    data: form.serialize(),
    type: form.attr("method"),
    success: function (Persona) {
      $("#formularioIngreso")[0].reset();
      obtenerRegistros();
    },
    error:function(Persona) {
        console.log("No se ha podido obtener la información");
    }
  });
});

function obtenerRegistros () {
  $.ajax({
  url:"/motrarPersonas/",
  data: {csrfmiddlewaretoken: csrftoken },
  type: "POST",
  success: function (data) {
    var bodyTabla="";
    var date=new Date();
      for (var index = 0; index < data.length; index++) {
            var fechaDeNacimiento=new Date(data[index].fields.fechaNacimiento);
            var edad=date.getFullYear()-fechaDeNacimiento.getFullYear();
            bodyTabla+=`<tr>
                  <th>`+data[index].fields.nombre+`</th>
                  <th>`+data[index].fields.apellido+`</th>
                  <th>`+data[index].fields.correo+`</th>
                  <th>`+edad+`</th>
                  <th><button class="ui green button" onclick="editarPersona(`+data[index].pk+`);">Editar</button>
                    <button class="ui red button" onclick="eliminarPersona(`+data[index].pk+`);">Borrar</button></th>
                </tr>`;
  }
  $("#insertarPersonaTabla").html(bodyTabla);
  },
  error:function(data) {
      console.log("No se ha podido obtener la información");
  }
});
}

function editarPersona(idPersona) {
  $.ajax({
  url:"/obtenerPersona/",
  data: {'id':idPersona,csrfmiddlewaretoken: csrftoken },
  type: "POST",
  success: function (Persona) {
    $("#idPersona").val(Persona[0].pk);
    $("#editarNombre").val(Persona[0].fields.nombre);
    $("#editarApellido").val(Persona[0].fields.apellido);
    $("#editarEmail").val(Persona[0].fields.correo);
    $("#editarFechaNacimiento").val(Persona[0].fields.fechaNacimiento);
    $('.ui.modal')
      .modal('show')
    ;
  },
  error:function(data) {
      console.log("No se ha podido obtener la información");
  }
});

}



function guardarCambios() {
  var formulario= $("#formularioEditar");
  $.ajax({
  url:formulario.attr('action'),
  data:formulario.serialize(),
  type: formulario.attr('method'),
  success: function (Persona) {
  obtenerRegistros();
  },
  error:function(Persona) {
      console.log("No se ha podido obtener la información");
  }
});

}


function eliminarPersona(idPersona) {
  $.ajax({
  url:"/eliminarDatosPersonales/",
  data: {'id':idPersona,csrfmiddlewaretoken: csrftoken },
  type: "POST",
  success: function (Persona) {
  obtenerRegistros();
  },
  error:function(Persona) {
      console.log("No se ha podido obtener la información");
  }
  });

}



