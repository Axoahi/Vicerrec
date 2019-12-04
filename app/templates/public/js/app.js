// Adjunta el token en todas las llamadas AJAX si está presente en localStorage
$.ajaxSetup({
    beforeSend: function (xhr) {
        if (localStorage.getItem("token")) {
            xhr.setRequestHeader("Authorization", "Bearer " + localStorage.getItem("token"));
            //console.log("entra");
        }
    }
});

  function valida(){
    var xmlhttp = new XMLHttpRequest();
    //Configuramos la conexion, variable.open("METODO", "URL","TIPO DE CONEXION" )
    xmlhttp.open("GET", "http://localhost:8080/users/valida/" + $('#user').val() , false);
    //Enviamos la peticion
    xmlhttp.send();
    var existe = JSON.parse(xmlhttp.responseText);

    return existe;
  };
  //Crea un usuario en el servidor
  function signup(){

      if(!valida())
      {
        let user = {
          "username": $('#user').val(),
          "password": $('#pass').val()
        			 };
        $.ajax({
            type: "POST",
            url: "/users/sign-up",
            contentType: "application/json",
            data: JSON.stringify(user),
            dataType: "json",
            success: function () {
                 window.location.href = "http://localhost:8080/entrarUsuario.html";
            },
            error: function () {
                 window.location.href = "http://localhost:8080/entrarUsuario.html";

            }
        });
      }else{
        alert ("Noooooooooooooooo puedes pasaaaaaaaaaaaaaaaaarr (By Gandalf). El usuario ya existe :( prueba con otro.");
      }

  }

// Obtiene el token JWT
// Si las credenciales son correctas, el servidor devuelve el token en un objeto JSON
function login() {
    let user = {
                  "username": $('#user').val(),
                  "password": $('#pass').val()
              };
    $.ajax({
        type: "POST",
        url: "/login",
        contentType: "application/json",
        data: JSON.stringify(user),
        dataType: "json",
        success: function (data) {
            let token = data.token;
            localStorage.setItem("token", token);
            console.log('Got a token from the server! Token: ' + token);
            window.location.href = "http://localhost:8080/index.html";
        },
        error: function () {
              alert ("Noooooooooooooooo puedes pasaaaaaaaaaaaaaaaaarr (By Gandalf). El usuario y/o contraseña son incorrectos.");
              console.log("Login Failed");
        }
    });
}

// Elimina el token de localStorage
function logout() {
    localStorage.removeItem('token');
    if (localStorage.getItem("token")) {
      console.log("explota");
    }
    console.log("User logged out, token deleted");
}

// Intenta acceder a un servicio protegido con autentificación
// Sólo lo conseguirá si el token JWT está en localStorage,
//    $.ajaxSetup se encarga de adjuntarlo en la petición
function getTasks() {
    $.ajax({
        type: "GET",
        url: "/peliculas/all",
        dataType: "json",
        success: function (data) {
            console.log(data);
        },
        error: function () {
            console.log('Error while retrieving data');
        }
    });
}

$(document).ready(function () {
    $('#signup').click(signup);
    $('#login').click(login);
    $('#logout').click(logout);
    $('#tasks').click(getTasks);

});
