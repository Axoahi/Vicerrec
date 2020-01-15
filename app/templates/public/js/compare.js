var idStudy
var study

//onInit()
$(document).ready(function () {
    var pathname = window.location.pathname;
    idStudy = pathname.split("/")[2]
    study = '{"id": "'+ idStudy + '"}'

    $.ajax({
        type: 'POST',
        url: "/verDetalles",
        data: study,
        contentType: "application/json",
        encode: true,
        success: function rellena(data) {
            tablaHtml(data.comparativa)
        },
        error: function (data) {
            alert("Algo ha fallado!!! :( ");
            console.log(data)
        }
    });
});

function goDetailInterface() {
    if(idStudy != undefined){
        window.location.href = "/detail/" + idStudy
    }else{
        window.location.href = "/detail/" + idStudy
    }
    
}

function tablaHtml(datos) {
    var htmlTable = ""
    for (var i = 0; i < datos.length; i++) {
        htmlTable +=
            '<tr>' +
            '<th>' + datos[i]['titulo']  + '</th>' +
            '<td>' + datos[i]['codigo']  + '</td>' +
            '<td>' + datos[i]['anyo']  + '</td>' +
            '<td>' + datos[i]['gestiontitulo']['organizacionydesarrollo']  + '</td>' +
            '<td>' + datos[i]['gestiontitulo']['informacionytransparencia']  + '</td>' +
            '<td>' + datos[i]['gestiontitulo']['SGIC']  + '</td>' +
            '<td>' + datos[i]['recursos']['personalacademico']  + '</td>' +
            '<td>' + datos[i]['recursos']['apoyoyrecursosmateriales']  + '</td>' +
            '<td>' + datos[i]['resultados']['resultados']  + '</td>' +
            '<td>' + datos[i]['resultados']['indicadores']  + '</td>' +
            '<td>' + datos[i]['finaltotal']  + '</td>' +
            "</tr>" 
    }
    document.getElementById("listDocs").innerHTML = htmlTable;
};
