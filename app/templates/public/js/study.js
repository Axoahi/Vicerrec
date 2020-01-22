function detailHtml(datos) {
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
                "<input type='checkbox' name='task_1' id='curriculum_" + i + j + "' value='1' class='tasks-list-cb'>" +
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
                "<input type='checkbox' name='task_1' id='docentia_" + i + j + "' value='1' class='tasks-list-cb'>" +
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
                "<input type='checkbox' name='task_1' id='web_" + i + j + "' value='1' class='tasks-list-cb'>" +
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
                "<input type='checkbox' name='task_1' id='coordinacion_" + i + j + "' value='1' class='tasks-list-cb'>" +
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
                "<input type='checkbox' name='task_1' id='otras_" + i + j + "' value='1' class='tasks-list-cb'>" +
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


function tablaHtml(datos) {
    var htmlTable = ""
    for (var i = 0; i < datos.length; i++) {
        htmlTable +=
            '<tr>' +
            '<th>' + datos[i]['titulo'] + '</th>' +
            '<td>' + datos[i]['codigo'] + '</td>' +
            '<td>' + datos[i]['anyo'] + '</td>' +
            '<td>' + datos[i]['gestiontitulo']['organizacionydesarrollo'] + '</td>' +
            '<td>' + datos[i]['gestiontitulo']['informacionytransparencia'] + '</td>' +
            '<td>' + datos[i]['gestiontitulo']['SGIC'] + '</td>' +
            '<td>' + datos[i]['recursos']['personalacademico'] + '</td>' +
            '<td>' + datos[i]['recursos']['apoyoyrecursosmateriales'] + '</td>' +
            '<td>' + datos[i]['resultados']['resultados'] + '</td>' +
            '<td>' + datos[i]['resultados']['indicadores'] + '</td>' +
            '<td>' + datos[i]['finaltotal'] + '</td>' +
            '<td><a href="#popup1"><i class="material-icons">open_in_new</i></a></td>' +
            '<td><a href="#popup1"><i class="material-icons">open_in_new</i></a></td>' +
            '<td><a href="#popup1"><i class="material-icons">open_in_new</i></a></td>' +
            '<td><a href="#popup1"><i class="material-icons">open_in_new</i></a></td>' +
            '<td><a href="#popup1"><i class="material-icons">open_in_new</i></a></td>' +
            "</tr>"

    }
    document.getElementById("listDocs").innerHTML = htmlTable;
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


function showComparative() {
    document.getElementById("detail").style.display = "none"
    document.getElementById("comparative").style.display = "block"
    document.getElementById("view").value = "Vista detalle"
    document.getElementById("view").setAttribute("onclick", "showDetail()")

}

function showDetail() {
    document.getElementById("detail").style.display = "block";
    document.getElementById("comparative").style.display = "none";
    document.getElementById("view").value = "Vista comparativa"
    document.getElementById("view").setAttribute("onclick", "showComparative()")
}

function updateStudy() {
    var prueba
    var name = document.getElementById("nombre").value;
    var elem_otras = 0
    var elem_curriculum = 0
    var elem_docentia = 0
    var elem_web = 0
    var elem_coordinacion = 0
    var estudio = {
        "id": idStudy,
        "nombre": name,
        "comparativa": study.comparativa
    };

    for (var i = 0; i < study.comparativa.length; i++) {
        for (var j = 0; j < study.comparativa[i]['recomendaciones']['curriculum'].length; j++) {
            if ($('#curriculum_' + i + elem_curriculum).prop('checked')) {
                this.study.comparativa[i]['recomendaciones']['curriculum'].splice(j, 1)
                j--
            }
            elem_curriculum++
        }

        for (var j = 0; j < study.comparativa[i]['recomendaciones']['docentia'].length; j++) {
            if ($('#docentia_' + i + elem_docentia).prop('checked')) {
                this.study.comparativa[i]['recomendaciones']['docentia'].splice(j, 1)
                j--
            }
            elem_docentia++
        }

        for (var j = 0; j < study.comparativa[i]['recomendaciones']['web'].length; j++) {
            if ($('#web_' + i + elem_web).prop('checked')) {
                this.study.comparativa[i]['recomendaciones']['web'].splice(j, 1)
                j--
            }
            elem_web++
        }

        for (var j = 0; j < study.comparativa[i]['recomendaciones']['coordinacion'].length; j++) {
            if ($('#coordinacion_' + i + elem_coordinacion).prop('checked')) {
                this.study.comparativa[i]['recomendaciones']['coordinacion'].splice(j, 1)
                j--
            }
            elem_coordinacion++
        }

        for (var j = 0; j < study.comparativa[i]['recomendaciones']['otras'].length; j++) {
            if ($('#otras_' + i + elem_otras).prop('checked')) {
                this.study.comparativa[i]['recomendaciones']['otras'].splice(j, 1)
                j--
            }
            elem_otras++
        }
    }

    $.ajax({
        type: 'POST',
        url: "/updateStudy",
        data: JSON.stringify(estudio),
        contentType: "application/json",
        encode: true,
        success: function (data) {
            alert("Estudio actualizado!!! :) ");
            window.location.href = "/";
        },
        error: function (data) {
            alert("Algo ha fallado!!! :( ");
        }
    });
    event.preventDefault();
};
