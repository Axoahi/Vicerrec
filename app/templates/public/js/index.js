var acepciones = { "curriculum": [], "docentia": [], "web": [], "coordinacion": [], "otros": [] }
var curriculum = []
var docentia = []
var web = []
var coordinacion = []
var otras = []


//onInit()
$(document).ready(function () {
    document.getElementById("acepUser").value = JSON.stringify(
        { "curriculum": ['gato', 'oso'], "docentia": [], "web": [], "coordinacion": [], "otros": [] })
    rellenaEstudios();
    showAcep();
    getPagination('#myTable');
});

function rellenaEstudios() {
    var xmlhttp = new XMLHttpRequest();
    //Configuramos la conexion, variable.open("METODO", "URL","TIPO DE CONEXION" )
    xmlhttp.open("GET", "/list", false);
    //Enviamos la peticion
    xmlhttp.send();
    var comparativas = JSON.parse(xmlhttp.responseText);
    var htmlListado = ""
    for (var i = 0; i < comparativas.length; i++) {
        htmlListado +=
            "<tr>" +
            "<td>" + comparativas[i].nombre + "</td>" +
            "<td><button type='button' class='btn btn-primary' onclick='verEstudio(\"m" + comparativas[i].id + "\");'><i class='material-icons'>assignment</i></button></td>" +
            "<td><button type='button' class='btn btn-danger' onclick='eliminarEstudio(\"m" + comparativas[i].id + "\");'><i class='material-icons'>delete_outline</i></button></td>" +
            "</tr>"
    }
    document.getElementById("listado").innerHTML = htmlListado;
}


function downloadGuide() {

    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/getManual', true);
    xhr.responseType = 'blob';

    xhr.onload = function(e) {
      if (this.status == 200) {
        var blob = new Blob([this.response], {type: 'application/pdf'});
        var link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob);
        link.download = "Manual.pdf";
        link.click();       
      }
    };

    xhr.send();

}


function verEstudio(aux) {
    var id = aux.substr(1)
    var estudio = JSON.stringify({ "id": id })
    window.location.href = "/study/" + id
}

function eliminarEstudio(aux) {
    var id = aux.substr(1)
    var estudio = JSON.stringify({ "id": id })
    $.ajax({
        type: 'POST',
        url: "/borrarEstudio",
        data: estudio,
        contentType: "application/json",
        encode: true,
        success: function (data) {
            window.location.href = "/";
        },
        error: function (data) {
            alert("Algo ha fallado!!! :( ");
        }
    });
    event.preventDefault();
}

//var fileTypes = ['pdf', 'docx', 'rtf', 'jpg', 'jpeg', 'png', 'txt'];
var fileTypes = ['pdf'];  //acceptable file types
function readURL(input) {
    if (input.files && input.files[0]) {
        var extension = input.files[0].name.split('.').pop().toLowerCase(),  //file extension from input file
            isSuccess = fileTypes.indexOf(extension) > -1;  //is extension in acceptable types

        if (isSuccess) { //yes
            var reader = new FileReader();
            reader.onload = function (e) {
                if (extension == 'pdf') {
                    $(input).closest('.fileUpload').find(".icon").attr('src', 'https://image.flaticon.com/icons/svg/179/179483.svg');
                }
                else if (extension == 'docx') {
                    $(input).closest('.fileUpload').find(".icon").attr('src', 'https://image.flaticon.com/icons/svg/281/281760.svg');
                }
                else if (extension == 'rtf') {
                    $(input).closest('.fileUpload').find(".icon").attr('src', 'https://image.flaticon.com/icons/svg/136/136539.svg');
                }
                else if (extension == 'png') {
                    $(input).closest('.fileUpload').find(".icon").attr('src', 'https://image.flaticon.com/icons/svg/136/136523.svg');
                }
                else if (extension == 'jpg' || extension == 'jpeg') {
                    $(input).closest('.fileUpload').find(".icon").attr('src', 'https://image.flaticon.com/icons/svg/136/136524.svg');
                }
                else if (extension == 'txt') {
                    $(input).closest('.fileUpload').find(".icon").attr('src', 'https://image.flaticon.com/icons/svg/136/136538.svg');
                }
                else {
                    $(input).closest('.uploadDoc').find(".docErr").slideUp('slow');
                }
            }

            reader.readAsDataURL(input.files[0]);
        }
        else {
            $(input).closest('.uploadDoc').find(".docErr").fadeIn();
            setTimeout(function () {
                $('.docErr').fadeOut('slow');
            }, 9000);
        }
    }
}
$(document).ready(function () {

    $(document).on('change', '.up', function () {
        var id = $(this).attr('id'); /* gets the filepath and filename from the input */
        var profilePicValue = $(this).val();
        var fileNameStart = profilePicValue.lastIndexOf('\\'); /* finds the end of the filepath */
        profilePicValue = profilePicValue.substr(fileNameStart + 1).substring(0, 20); /* isolates the filename */
        //var profilePicLabelText = $(".upl"); /* finds the label text */
        if (profilePicValue != '') {
            $(this).closest('.fileUpload').find('.upl').html(profilePicValue); /* changes the label text */
        }
    });

    $(".btn-new").on('click', function () {
        $("#uploader").append('<div class="uploadDoc"><div class="col-sm-10"><div class="docErr">El archivo no es un PDF. No será procesado.</div><!--error--><div class="fileUpload btn btn-orange"> <img src="https://image.flaticon.com/icons/svg/136/136549.svg" class="icon"><span class="upl" id="upload">Subir documento</span><input class="form-control-file upload up" id="file-picker" type="file" name="file" accept="pdf/*" onchange="readURL(this);"</div></div></div><div class="col-sm-1"><a class="btn-check"><i class="material-icons">delete_outline</i></a></div></div>');
    });

    $(document).on("click", "a.btn-check", function () {
        if ($(".uploadDoc").length > 1) {
            $(this).closest(".uploadDoc").remove();
        } else {
            alert("You have to upload at least one document.");
        }
    });
});



function putAcep() {
    var curriculum_form = document.getElementById("curriculum").value
    curriculum = curriculum_form.split(",")
    var docentia_form = document.getElementById("docentia").value
    docentia = docentia_form.split(",")
    var web_form = document.getElementById("web").value
    web = web_form.split(",")
    var coordinacion_form = document.getElementById("coordinacion").value
    coordinacion = coordinacion_form.split(",")
    var otras_form = document.getElementById("otras").value
    otras = otras_form.split(",")
    if (curriculum != "") {
        acepciones["curriculum"] = curriculum
    }
    if (docentia != "") {
        acepciones["docentia"] = docentia
    }
    if (web != "") {
        acepciones["web"] = web
    }
    if (coordinacion != "") {
        acepciones["coordinacion"] = coordinacion
    }
    if (otras != "") {
        acepciones["otros"] = otras
    }

    document.getElementById("acepUser").value = JSON.stringify(acepciones)
    showAcep()
    window.location.href = "#"
}

function showAcep() {

    var listAcepciones = ""

    if (curriculum.length != 0 && docentia.length != 0 && web.length != 0 && coordinacion.length != 0 && otras.length != 0) {
        listAcepciones +=
            '<h5>Acepciones</h5>' +
            '<ul>' + '<li>Curriculum: '

        for (var i = 0; i < curriculum.length; i++) {
            if (i < curriculum.length - 1)
                listAcepciones += curriculum[i] + ', '
            else
                listAcepciones += curriculum[i]
        }

        listAcepciones +=
            '</li>' + '<li>Docentia: '

        for (var i = 0; i < docentia.length; i++) {
            if (i < docentia.length - 1)
                listAcepciones += docentia[i] + ', '
            else
                listAcepciones += docentia[i]
        }

        listAcepciones += '</li>' + '<li>Web: '
        for (var i = 0; i < web.length; i++) {
            if (i < web.length - 1)
                listAcepciones += web[i] + ', '
            else
                listAcepciones += web[i]
        }

        listAcepciones += '</li>' + '<li>Coordinación: '
        for (var i = 0; i < coordinacion.length; i++) {
            if (i < coordinacion.length - 1)
                listAcepciones += coordinacion[i] + ', '
            else
                listAcepciones += coordinacion[i]
        }

        listAcepciones += '</li>' + '<li>Otros: '
        for (var i = 0; i < otras.length; i++) {
            if (i < otras.length - 1)
                listAcepciones += otras[i] + ', '
            else
                listAcepciones += otras[i]
        }

        listAcepciones += '</li>' + '</ul>'

    }

    document.getElementById("listAcep").innerHTML = listAcepciones;
}

/*PAGINATION 
- on change max rows select options fade out all rows gt option value mx = 5
- append pagination list as per numbers of rows / max rows option (20row/5= 4pages )
- each pagination li on click -> fade out all tr gt max rows * li num and (5*pagenum 2 = 10 rows)
- fade out all tr lt max rows * li num - max rows ((5*pagenum 2 = 10) - 5)
- fade in all tr between (maxRows*PageNum) and (maxRows*pageNum)- MaxRows 
*/

function getPagination(table) {
    var lastPage = 1;
    $('#maxRows')
        .on('change', function (evt) {
            lastPage = 1;
            $('.pagination')
                .find('li')
                .slice(1, -1)
                .remove();
            var trnum = 0; // reset tr counter
            var maxRows = parseInt($(this).val()); // get Max Rows from select option
            if (maxRows == 5000) {
                $('.pagination').hide();
            } else {
                $('.pagination').show();
            }
            var totalRows = $(table + ' tbody tr').length; // numbers of rows
            $(table + ' tr:gt(0)').each(function () {
                // each TR in  table and not the header
                trnum++; // Start Counter
                if (trnum > maxRows) {
                    // if tr number gt maxRows
                    $(this).hide(); // fade it out
                }
                if (trnum <= maxRows) {
                    $(this).show();
                } // else fade in Important in case if it ..
            }); //  was fade out to fade it in
            if (totalRows > maxRows) {
                // if tr total rows gt max rows option
                var pagenum = Math.ceil(totalRows / maxRows); // ceil total(rows/maxrows) to get ..
                //	numbers of pages
                for (var i = 1; i <= pagenum;) {
                    // for each page append pagination li
                    $('.pagination #prev')
                        .before(
                            '<li data-page="' +
                            i +
                            '">\
              <span>' +
                            i++ +
                            '<span class="sr-only">(current)</span></span>\
            </li>'
                        )
                        .show();
                }
            }
            $('.pagination [data-page="1"]').addClass('active'); // add active class to the first li
            $('.pagination li').on('click', function (evt) {
                // on click each page
                evt.stopImmediatePropagation();
                evt.preventDefault();
                var pageNum = $(this).attr('data-page'); // get it's number

                var maxRows = parseInt($('#maxRows').val()); // get Max Rows from select option

                if (pageNum == 'prev') {
                    if (lastPage == 1) {
                        return;
                    }
                    pageNum = --lastPage;
                }
                if (pageNum == 'next') {
                    if (lastPage == $('.pagination li').length - 2) {
                        return;
                    }
                    pageNum = ++lastPage;
                }

                lastPage = pageNum;
                var trIndex = 0; // reset tr counter
                $('.pagination li').removeClass('active'); // remove active class from all li
                $('.pagination [data-page="' + lastPage + '"]').addClass('active'); // add active class to the clicked
                limitPagging();
                $(table + ' tr:gt(0)').each(function () {
                    // each tr in table not the header
                    trIndex++; // tr index counter
                    // if tr index gt maxRows*pageNum or lt maxRows*pageNum-maxRows fade if out
                    if (
                        trIndex > maxRows * pageNum ||
                        trIndex <= maxRows * pageNum - maxRows
                    ) {
                        $(this).hide();
                    } else {
                        $(this).show();
                    }
                });
            });
            limitPagging();
        })
        .val(5)
        .change();
}

function limitPagging() {
    if ($('.pagination li').length > 7) {
        if ($('.pagination li.active').attr('data-page') <= 3) {
            $('.pagination li:gt(5)').hide();
            $('.pagination li:lt(5)').show();
            $('.pagination [data-page="next"]').show();
        } if ($('.pagination li.active').attr('data-page') > 3) {
            $('.pagination li:gt(0)').hide();
            $('.pagination [data-page="next"]').show();
            for (let i = (parseInt($('.pagination li.active').attr('data-page')) - 2); i <= (parseInt($('.pagination li.active').attr('data-page')) + 2); i++) {
                $('.pagination [data-page="' + i + '"]').show();
            }
        }
    }
}

$(function () {
    $('table tr:eq(0)').prepend('<th> ID </th>');
    var id = 0;
    $('table tr:gt(0)').each(function () {
        id++;
        $(this).prepend('<td>' + id + '</td>');
    });
});

function showPopupAcep() {
    document.getElementById("cargar").style.display = "none"
    document.getElementById("crear").style.display = "none"
    document.getElementById("titulo").style.display = "none"
}

function showIndex() {
    document.getElementById("cargar").style.display = "block"
    document.getElementById("crear").style.display = "flex"
    document.getElementById("titulo").style.display = "block"
}

