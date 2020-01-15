//onInit()
var idStudy
var study
var items = {}
var prueba 

$(document).ready(function () {
    var pathname = window.location.pathname;
    idStudy = pathname.split("/")[2]
    prueba = '{"id": "'+ idStudy + '"}'
    console.log(prueba)


    // var datos = JSON.parse(idStudy)
    // console.log(datos)

    $.ajax({
        type: 'GET',
        url: "/verDetalles",
        data: prueba,
        contentType: "application/json",
        encode: true,
        success: function rellena(data) {
            console.log(data)
        },
        error: function (data) {
            alert("Algo ha fallado!!! :( ");
            console.log(data)
        }
    });


});
