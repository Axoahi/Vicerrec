function tablaHtml(datos) {
    var htmlTable = ""

    for (var i = 0; i < datos.length; i++) {

        htmlTable +=
            "<div id='tab-" + (i + 1) + "'>" +
            "<p>" +
            "<h3>" + datos[i]['titulo'] + "</h3>" +
            "<article>" +
            "<section class='row'>" +
            "<section class='col'>" +
            "<h4>DATOS</h4>" +
            "</section>" +
            "</section>" +
            "<section class='row'>" +
            "<section class='col'>" +
            "<h6>Código</h6>" +
            "<p>" + datos[i]['codigo'] + "</p>" +
            "</section>" +
            "<section class='col'>" +
            "<h6>año</h6>" +
            "<p>" + datos[i]['anyo'] + "</p>" +
            "</section>" +
            "</section>" +
            "<section class='row'>" +
            "<section class='col'>" +
            "<section class='row'>" +
            "<section class='col'>" +
            "<h4>GESTIÓN DE TÍTULO</h4>" +
            "</section>" +
            "</section>" +
            "<section class='row'>" +
            "<section class='col'>" +
            "<h6>Organización y desarrollo</h6>" +
            "<p>" + datos[i]['gestiontitulo']['organizacionydesarrollo'] + "</p>" +
            "</section>" +
            "<section class='col'>" +
            "<h6>Información y trasparencia</h6>" +
            "<p>" + datos[i]['gestiontitulo']['informacionytransparencia'] + "</p>" +
            "</section>" +
            "<section class='col'>" +
            "<h6>SGIC</h6>" +
            "<p>" + datos[i]['gestiontitulo']['SGIC'] + "</p>" +
            "</section>" +
            "</section>" +
            "<section class='row'>" +
            "<section class='col'>" +
            "<h4>RECURSOS</h4>" +
            "</section>" +
            "</section>" +
            "<section class='row'>" +
            "<section class='col'>" +
            "<h6>Personal Académico</h6>" +
            "<p>" + datos[i]['recursos']['personalacademico'] + "</p>" +
            "</section>" +
            "<section class='col'>" +
            "<h6>Personal Apoyo y Recursos materiales</h6>" +
            "<p>" + datos[i]['recursos']['apoyoyrecursosmateriales'] + "</p>" +
            "</section>" +
            "</section>" +
            "<section class='row'>" +
            "<section class='col'>" +
            "<h4>RESULTADOS</h4>" +
            "</section>" +
            "</section>" +
            "<section class='row'>" +
            "<section class='col'>" +
            "<h6>Resultados</h6>" +
            "<p>" + datos[i]['resultados']['resultados'] + "</p>" +
            "</section>" +
            "<section class='col'>" +
            "<h6>Indicadores satisfacción y rendimiento</h6>" +
            "<p>" + datos[i]['resultados']['indicadores'] + "</p>" +
            "</section>" +
            "</section>" +
            "<section class='row'>" +
            "<section class='col'>" +
            "<h4>FINAL TOTAL</h4>" +
            "<h6 class='resultado'>" + datos[i]['finaltotal'] + "</h6>" +
            "</section>" +
            "</section>" +
            "<section class='row'>" +
            "<section class='col'>" +
            "<h4>OBSERVACIONES</h4>" +
            "</section>" +
            "</section>" +
            "<section class='row'>" +
            "<section class='col'>"
        if (datos[i]['recomendaciones']['curriculum'].length > 0) {
            htmlTable +=
                "<h6>Curriculum</h6>" +
                "<fieldset class='tasks-list'>"
        }

        for (var j = 0; j < datos[i]['recomendaciones']['curriculum'].length; j++) {
            htmlTable +=
                "<label class='tasks-list-item'>" +
                "<input type='checkbox' name='task_1' value='1' class='tasks-list-cb'>" +
                "<span class='tasks-list-mark'></span>" +
                "<span class='tasks-list-desc'>" + datos[i]['recomendaciones']['curriculum'][j] + "</span>" +
                "</label>"
        }

        htmlTable +=
            "</fieldset>" +
            "</section>" +
            "</section>" +
            "<section class='row'>" +
            "<section class='col'>"
        if (datos[i]['recomendaciones']['docentia'].length > 0) {
            htmlTable +=
                "<h6>Docencia</h6>" +
                "<fieldset class='tasks-list'>"
        }

        for (var j = 0; j < datos[i]['recomendaciones']['docentia'].length; j++) {
            htmlTable +=
                "<label class='tasks-list-item'>" +
                "<input type='checkbox' name='task_1' value='1' class='tasks-list-cb'>" +
                "<span class='tasks-list-mark'></span>" +
                "<span class='tasks-list-desc'>" + datos[i]['recomendaciones']['docentia'][j] + "</span>" +
                "</label>"
        }

        htmlTable +=
            "</fieldset>" +
            "</section>" +
            "</section>" +
            "<section class='row'>" +
            "<section class='col'>"
        if (datos[i]['recomendaciones']['web'].length > 0) {
            htmlTable +=
                "<h6>WEB</h6>" +
                "<fieldset class='tasks-list'>"
        }

        for (var j = 0; j < datos[i]['recomendaciones']['web'].length; j++) {
            htmlTable +=
                "<label class='tasks-list-item'>" +
                "<input type='checkbox' name='task_1' value='1' class='tasks-list-cb'>" +
                "<span class='tasks-list-mark'></span>" +
                "<span class='tasks-list-desc'>" + datos[i]['recomendaciones']['web'][j] + "</span>" +
                "</label>"
        }

        htmlTable +=
            "</fieldset>" +
            "</section>" +
            "</section>" +
            "<section class='row'>" +
            "<section class='col'>"
        if (datos[i]['recomendaciones']['coordinacion'].length > 0) {
            htmlTable +=
                "<h6>Coordinación</h6>" +
                "<fieldset class='tasks-list'>"
        }

        for (var j = 0; j < datos[i]['recomendaciones']['coordinacion'].length; j++) {
            htmlTable +=
                "<label class='tasks-list-item'>" +
                "<input type='checkbox' name='task_1' value='1' class='tasks-list-cb'>" +
                "<span class='tasks-list-mark'></span>" +
                "<span class='tasks-list-desc'>" + datos[i]['recomendaciones']['coordinacion'][j] + "</span>" +
                "</label>"
        }

        htmlTable +=
            "</fieldset>" +
            "</section>" +
            "</section>" +
            "<section class='row'>" +
            "<section class='col'>"
        if (datos[i]['recomendaciones']['otras'].length > 0) {
            htmlTable +=
                "<h6>Otras</h6>" +
                "<fieldset class='tasks-list'>"
        }

        for (var j = 0; j < datos[i]['recomendaciones']['otras'].length; j++) {
            htmlTable +=
                "<label class='tasks-list-item'>" +
                "<input type='checkbox' name='task_1' value='1' class='tasks-list-cb'>" +
                "<span class='tasks-list-mark'></span>" +
                "<span class='tasks-list-desc'>" + datos[i]['recomendaciones']['otras'][j] + "</span>" +
                "</label>"
        }

        htmlTable +=
            "</ul>" +
            "</section>" +
            "</section>" +
            "</article>" +
            "</p>" +
            "</div>"
    }

    document.getElementById("listado").innerHTML = htmlTable;

    // Show the first tab by default
    $('.tabs-stage div').hide();
    $('.tabs-stage div:first').show();
    $('.tabs-nav li:first').addClass('tab-active');

    // Change tab class and display content
    $('.tabs-nav a').on('click', function (event) {
        event.preventDefault();
        $('.tabs-nav li').removeClass('tab-active');
        $(this).parent().addClass('tab-active');
        $('.tabs-stage div').hide();
        $($(this).attr('href')).show();
    });
};


function getPDFs(datos) {
    var aux = document.getElementById("list-PDFs");
    var aux2 = aux.getElementsByTagName("A");
    for (var j = 0; j < aux2.length; j++) {
        if (datos[j] != undefined) {
            aux2[j].innerHTML = datos[j]['titulo'];
        } else {
            var padre = aux2[j].parentNode.parentNode;
            padre.removeChild(aux2[j].parentNode);
            j--;
        }
    }
};

//Guardamos el estudio en la bd
function actualizarEstudio() {
    //actualizamos el nombre
    var name = document.getElementById("nombre").value;
    actualizar.nombre = name
    //Aqui tendriamos que cojer los datos de la tabla(han eliminado archivos, han añadido archivos)
    //actualizar.comparativa = 
    alert("funciona");
};