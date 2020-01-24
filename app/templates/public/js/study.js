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

// VERDE: Excelente, Se alcanza, Satisfactorio, Satisfactoria, Se supera excelentemente
// AMARILLO: Adecuada, Adecuado, Se alcanza parcialmente, Suficiente
// ROJO: Insuficiente, No se alcanza

 function tablaHtml(datos) {
    var htmlTable = ""
    var perfect = ["Excelente", "Se alcanza", "Satisfactorio", 'Satisfactoria', "Se supera excelentemente", 'Favorable']
    var good = ['Adecuada', 'Adecuado', 'Se alcanza parcialmente', 'Suficiente']
    var bad = ["Insuficiente", "No se alcanza"]
    var state

    for (var i = 0; i < datos.length; i++) {
        htmlTable +=
            '<tr>' +
            '<th>' + datos[i]['titulo'] + '</th>' +
            '<td>' + datos[i]['codigo'] + '</td>' +
            '<td>' + datos[i]['anyo'] + '</td>'

        // datos[i]['gestiontitulo']['organizacionydesarrollo']
        for (var j = 0; j < perfect.length; j++) {
            state = datos[i]['gestiontitulo']['organizacionydesarrollo'].trim().localeCompare(perfect[j].trim())
            if (state == 0) {
                htmlTable +=
                    '<td class="state_perfect">' + datos[i]['gestiontitulo']['organizacionydesarrollo'] + '</td>'
            }
        }
        for (var j = 0; j < good.length; j++) {
            state = datos[i]['gestiontitulo']['organizacionydesarrollo'].trim().localeCompare(good[j])
            if (state == 0) {
                htmlTable +=
                    '<td class="state_good">' + datos[i]['gestiontitulo']['organizacionydesarrollo'] + '</td>'
            }
        }

        for (var j = 0; j < bad.length; j++) {
            state = datos[i]['gestiontitulo']['organizacionydesarrollo'].trim().localeCompare(bad[j])
            if (state == 0) {
                htmlTable +=
                    '<td class="state_bad">' + datos[i]['gestiontitulo']['organizacionydesarrollo'] + '</td>'
            }
        }

        // datos[i]['gestiontitulo']['informacionytransparencia']
        for (var j = 0; j < perfect.length; j++) {
            state = datos[i]['gestiontitulo']['informacionytransparencia'].trim().localeCompare(perfect[j].trim())
            if (state == 0) {
                htmlTable +=
                    '<td class="state_perfect">' + datos[i]['gestiontitulo']['informacionytransparencia'] + '</td>'
            }
        }
        for (var j = 0; j < good.length; j++) {
            state = datos[i]['gestiontitulo']['informacionytransparencia'].trim().localeCompare(good[j])
            if (state == 0) {
                htmlTable +=
                    '<td class="state_good">' + datos[i]['gestiontitulo']['informacionytransparencia'] + '</td>'
            }
        }

        for (var j = 0; j < bad.length; j++) {
            state = datos[i]['gestiontitulo']['informacionytransparencia'].trim().localeCompare(bad[j])
            if (state == 0) {
                htmlTable +=
                    '<td class="state_bad">' + datos[i]['gestiontitulo']['informacionytransparencia'] + '</td>'
            }
        }

        // datos[i]['gestiontitulo']['SGIC']
        for (var j = 0; j < perfect.length; j++) {
            state = datos[i]['gestiontitulo']['SGIC'].trim().localeCompare(perfect[j].trim())
            if (state == 0) {
                htmlTable +=
                    '<td class="state_perfect">' + datos[i]['gestiontitulo']['SGIC'] + '</td>'
            }
        }
        for (var j = 0; j < good.length; j++) {
            state = datos[i]['gestiontitulo']['SGIC'].trim().localeCompare(good[j])
            if (state == 0) {
                htmlTable +=
                    '<td class="state_good">' + datos[i]['gestiontitulo']['SGIC'] + '</td>'
            }
        }

        for (var j = 0; j < bad.length; j++) {
            state = datos[i]['gestiontitulo']['SGIC'].trim().localeCompare(bad[j])
            if (state == 0) {
                htmlTable +=
                    '<td class="state_bad">' + datos[i]['gestiontitulo']['SGIC'] + '</td>'
            }
        }

        // datos[i]['recursos']['personalacademico']
        for (var j = 0; j < perfect.length; j++) {
            state = datos[i]['recursos']['personalacademico'].trim().localeCompare(perfect[j].trim())
            if (state == 0) {
                htmlTable +=
                    '<td class="state_perfect">' + datos[i]['recursos']['personalacademico'] + '</td>'
            }
        }
        for (var j = 0; j < good.length; j++) {
            state = datos[i]['recursos']['personalacademico'].trim().localeCompare(good[j])
            if (state == 0) {
                htmlTable +=
                    '<td class="state_good">' + datos[i]['recursos']['personalacademico'] + '</td>'
            }
        }

        for (var j = 0; j < bad.length; j++) {
            state = datos[i]['recursos']['personalacademico'].trim().localeCompare(bad[j])
            if (state == 0) {
                htmlTable +=
                    '<td class="state_bad">' + datos[i]['recursos']['personalacademico'] + '</td>'
            }
        }

        // datos[i]['recursos']['apoyoyrecursosmateriales']
        for (var j = 0; j < perfect.length; j++) {
            state = datos[i]['recursos']['apoyoyrecursosmateriales'].trim().localeCompare(perfect[j].trim())
            if (state == 0) {
                htmlTable +=
                    '<td class="state_perfect">' + datos[i]['recursos']['apoyoyrecursosmateriales'] + '</td>'
            }
        }
        for (var j = 0; j < good.length; j++) {
            state = datos[i]['recursos']['apoyoyrecursosmateriales'].trim().localeCompare(good[j])
            if (state == 0) {
                htmlTable +=
                    '<td class="state_good">' + datos[i]['recursos']['apoyoyrecursosmateriales'] + '</td>'
            }
        }

        for (var j = 0; j < bad.length; j++) {
            state = datos[i]['recursos']['apoyoyrecursosmateriales'].trim().localeCompare(bad[j])
            if (state == 0) {
                htmlTable +=
                    '<td class="state_bad">' + datos[i]['recursos']['apoyoyrecursosmateriales'] + '</td>'
            }
        }

        // datos[i]['resultados']['resultados']
        for (var j = 0; j < perfect.length; j++) {
            state = datos[i]['resultados']['resultados'].trim().localeCompare(perfect[j].trim())
            if (state == 0) {
                htmlTable +=
                    '<td class="state_perfect">' + datos[i]['resultados']['resultados'] + '</td>'
            }
        }
        for (var j = 0; j < good.length; j++) {
            state = datos[i]['resultados']['resultados'].trim().localeCompare(good[j])
            if (state == 0) {
                htmlTable +=
                    '<td class="state_good">' + datos[i]['resultados']['resultados'] + '</td>'
            }
        }

        for (var j = 0; j < bad.length; j++) {
            state = datos[i]['resultados']['resultados'].trim().localeCompare(bad[j])
            if (state == 0) {
                htmlTable +=
                    '<td class="state_bad">' + datos[i]['resultados']['resultados'] + '</td>'
            }
        }

        // datos[i]['resultados']['indicadores'] 
        for (var j = 0; j < perfect.length; j++) {
            state = datos[i]['resultados']['indicadores'].trim().localeCompare(perfect[j].trim())
            if (state == 0) {
                htmlTable +=
                    '<td class="state_perfect">' + datos[i]['resultados']['indicadores'] + '</td>'
            }
        }
        for (var j = 0; j < good.length; j++) {
            state = datos[i]['resultados']['indicadores'].trim().localeCompare(good[j])
            if (state == 0) {
                htmlTable +=
                    '<td class="state_good">' + datos[i]['resultados']['indicadores'] + '</td>'
            }
        }

        for (var j = 0; j < bad.length; j++) {
            state = datos[i]['resultados']['indicadores'].trim().localeCompare(bad[j])
            if (state == 0) {
                htmlTable +=
                    '<td class="state_bad">' + datos[i]['resultados']['indicadores'] + '</td>'
            }
        }

        // datos[i]['finaltotal'] 
        for (var j = 0; j < perfect.length; j++) {
            state = datos[i]['finaltotal'].trim().localeCompare(perfect[j].trim())
            if (state == 0) {
                htmlTable +=
                    '<td class="state_perfect">' + datos[i]['finaltotal'] + '</td>'
            }
        }
        for (var j = 0; j < good.length; j++) {
            state = datos[i]['finaltotal'].trim().localeCompare(good[j])
            if (state == 0) {
                htmlTable +=
                    '<td class="state_good">' + datos[i]['finaltotal'] + '</td>'
            }
        }

        for (var j = 0; j < bad.length; j++) {
            state = datos[i]['finaltotal'].trim().localeCompare(bad[j])
            if (state == 0) {
                htmlTable +=
                    '<td class="state_bad">' + datos[i]['finaltotal'] + '</td>'
            }
        }

        if(datos[i]['recomendaciones']['curriculum'].length == 0){
            htmlTable +=
                '<td><i class="material-icons">cancel_presentation</i></td>' 
        }else{
            htmlTable +=
                '<td><a href="#info_' + i + '0" onclick="showPopup();"><i class="material-icons">open_in_new</i></a></td>' 
        }

        if(datos[i]['recomendaciones']['docentia'].length == 0){
            htmlTable +=
                '<td><i class="material-icons">cancel_presentation</i></td>' 
        }else{
            htmlTable +=
                '<td><a href="#info_' + i + '1" onclick="showPopup();"><i class="material-icons">open_in_new</i></a></td>' 
        }

        if(datos[i]['recomendaciones']['web'].length == 0){
            htmlTable +=
                '<td><i class="material-icons">cancel_presentation</i></td>' 
        }else{
            htmlTable +=
                '<td><a href="#info_' + i + '2" onclick="showPopup();"><i class="material-icons">open_in_new</i></a></td>' 
        }

        if(datos[i]['recomendaciones']['coordinacion'].length == 0){
            htmlTable +=
                '<td><i class="material-icons">cancel_presentation</i></td>' 
        }else{
            htmlTable +=
                '<td><a href="#info_' + i + '3" onclick="showPopup();"><i class="material-icons">open_in_new</i></a></td>' 
        }

        if(datos[i]['recomendaciones']['otras'].length == 0){
            htmlTable +=
                '<td><i class="material-icons">cancel_presentation</i></td>' +
                "</tr>"
        }else{
            htmlTable +=
                '<td><a href="#info_' + i + '4" onclick="showPopup();"><i class="material-icons">open_in_new</i></a></td>' +
                "</tr>"
        }
            
    }
    document.getElementById("listDocs").innerHTML = htmlTable;
};

function popupHtml(datos) {
    var htmlTable = ""
    for (var i = 0; i < datos.length; i++) {
        for (var j = 0; j < 5; j++) {
            htmlTable +=
                '<div id="info_' + i + j + '"  class="overlay">' +
                '<div class="popup">'
            if (j == 0) {

                htmlTable +=
                    '<h2>Curriculum</h2>' +
                    '<a class="close" href="#" onclick="closePopup();">&times;</a>' +
                    '<div class="content">' +
                    '<p>' + datos[i]['recomendaciones']['curriculum'] + '</p>'

            } else if (j == 1) {

                htmlTable +=
                    '<h2>Docentia</h2>' +
                    '<a class="close" href="#" onclick="closePopup();">&times;</a>' +
                    '<div class="content">' +
                    '<p>' + datos[i]['recomendaciones']['docentia'] + '</p>'

            } else if (j == 2) {

                htmlTable +=
                    '<h2>Web</h2>' +
                    '<a class="close" href="#" onclick="closePopup();">&times;</a>' +
                    '<div class="content">' +
                    '<p>' + datos[i]['recomendaciones']['web'] + '</p>'

            } else if (j == 3) {

                htmlTable +=
                    '<h2>Coordinación</h2>' +
                    '<a class="close" href="#" onclick="closePopup();">&times;</a>' +
                    '<div class="content">' +
                    '<p>' + datos[i]['recomendaciones']['coordinacion'] + '</p>'

            } else if (j == 4) {

                htmlTable +=
                    '<h2>Otras</h2>' +
                    '<a class="close" href="#" onclick="closePopup();">&times;</a>' +
                    '<div class="content">' +
                    '<p>' + datos[i]['recomendaciones']['otras'] + '</p>'

            }

            htmlTable +=
                '</div>' +
                '</div>' +
                '</div>'
        }
    }

    document.getElementById("listPopup").innerHTML = htmlTable;
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

function showPopup(){
    document.getElementById("comparative").style.display = "none";
}

function closePopup(){
    document.getElementById("comparative").style.display = "block"; 
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
            window.location.href = "/";
        },
        error: function (data) {
            alert("No se ha podido guardar");
        }
    });
    event.preventDefault();
};
