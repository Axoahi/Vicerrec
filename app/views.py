# coding=utf-8
from flask import jsonify
import glob
import os
import ast
import json
import estudiosMongo
import acepcionesMongo
import ConversionPDF
import creadExport
import estadisticas
from werkzeug.utils import secure_filename
from flask import request, redirect, url_for, Response
from flask import render_template
from flask import Flask, send_from_directory, after_this_request

app = Flask(__name__)


# Variable que nos marca que se permite subir
app.config["ALLOWED_EXTENSIONS"] = ["pdf"]
app.config["CLIENT_DIRECTORY"] = os.getcwd() + "/data/"


def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

#  Carga de css y js
@app.route('/<path:path>')
def get_resource(path):  # pragma: no cover
    mimetypes = {
        ".css": "text/css",
        ".html": "text/html",
        ".js": "application/javascript",
    }
    complete_path = os.path.join(root_dir(), path)
    ext = os.path.splitext(path)[1]
    mimetype = mimetypes.get(ext, "text/html")
    content = get_file(complete_path)
    return Response(content, mimetype=mimetype)

# Pagina index
@app.route("/")
def index():
    return render_template("/public/index.html")

# Pagina estudio
@app.route("/study/<id>", methods=["GET"])
def detalles(id):
    datajson = {"id": id}
    return render_template("public/study.html", data=json.dumps(datajson))

# Página nuevo estudio
@app.route("/study", methods=['POST', "GET"])
def upload():

    # Borramos todos los archivos excel que existan previamente en el servidor
    files = glob.glob(app.config["CLIENT_DIRECTORY"]+"*.xls")

    # Convertimos el texto a JSON, para luego extraer los campos y pasarlos a lista
    acepsFrontend = request.form["pyacepUser"]
    dictAcepUser = ast.literal_eval(acepsFrontend)
    acepUser = list(dictAcepUser.values())

    for f in files:
        os.remove(f)

    target = os.path.join(app.instance_path)
    # Si no existe el directorio donde dejar los archivos, se crea
    if not os.path.isdir(target):
        os.mkdir(target)

    # Miramos que la lista de archivos a subir no esté vacía
    if request.files['file'].filename == '':
        print("Se debe de subir un archivo por lo menos")
        return redirect(url_for('index'))
    else:
        archiValidos = []
        textoSacado = []
        # Recorremos los archivos, y aplicamos seguridad básica
        for file in request.files.getlist("file"):
            filename = file.filename

            # Si el archivo ha pasado la seguridad básica, se procesa.
            if archivoPermitido(filename):
                # Otra capa de seguridad
                filename = secure_filename(filename)
                destination = "/".join([target, filename])
                # Se guarda el archivo
                file.save(destination)
                # Leemos la información del archivo
                try:
                    textoSacado.append(ConversionPDF.validaInforme(destination, acepUser))
                except:
                    textoSacado.append(False)

                # Una vez se ha subido el archivo y se ha procesado, se elimina
                if os.path.exists(destination):
                    os.remove(destination)
                    print("Archivo eliminado")
                else:
                    print("El archivo no existe")
    # return Response(json.dumps(textoSacado), mimetype='application/json')
    return render_template("public/study.html", data=json.dumps(textoSacado))

# Procesamiento de subida de archivo, previo a muestra de
@app.route("/getExcel", methods=['POST'])
def getExcel():
    target = app.config["CLIENT_DIRECTORY"]
    # Si no existe el directorio donde dejar los archivos, se crea
    if not os.path.isdir(target):
        os.mkdir(target)

    print(request.form["pynombre"])
    if not request.form["pynombre"]:
        nombre = "estudio"
    else:
        nombre = request.form["pynombre"]
    listado = request.form["pylistadoAneca"]
    newlistado = ast.literal_eval(listado)
    # Se crea el archivo y se devuelve ruta y nombre para bajar y eliminar
    nombreFile = creadExport.exportarExcel(nombre, newlistado) + ".xls"
    try:
        return send_from_directory(
            app.config["CLIENT_DIRECTORY"], filename=nombreFile, as_attachment=True
        )
    except FileNotFoundError:
        abort(404)

# borrado de un excel
@app.route("/borraExcel", methods=['POST'])
def borraExcel():
    nombre = request.form["pynombre"]
    nombreFile = nombre + ".xls"

    if os.path.exists(app.config["CLIENT_DIRECTORY"] + nombreFile):
        os.remove(app.config["CLIENT_DIRECTORY"] + nombreFile)
        print("Archivo Excel eliminado")
    else:
        print("El archivo Excel no existe")


def archivoPermitido(fileName):
    # 1 seg: Se mira que sea un archivo.
    if not "." in fileName:
        return False

    # 2 seg: Se mira la extensión pdf
    ext = fileName.rsplit(".", 1)[1]
    if ext.lower() in app.config["ALLOWED_EXTENSIONS"]:
        return True
    else:
        return False

# Guardar estudio
@app.route("/new", methods=['POST'])
def GuardarEstudio():
    estudio = request.get_json()
    id = estudiosMongo.crearEstudio(estudio)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

# Actualizar un estudio
@app.route("/updateStudy", methods=['POST', 'GET'])
def actualizar():
    estudio = request.get_json(force=True)
    id = estudio['id']
    del estudio['id']
    done = estudiosMongo.actualizarEstudio(id, estudio)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

# Añadir archivos a un estudio
@app.route("/addFiles", methods=['POST'])
def anyadirArchivos():
    allData = request.form.to_dict('pointOfStudy')
    acepciones = allData['pyacepUser']
    dictAcepUser = ast.literal_eval(str(acepciones))
    acepUser = list(dictAcepUser.values())

    oldData = allData['pointOfStudy']

    target = os.path.join(app.instance_path)
    # Si no existe el directorio donde dejar los archivos, se crea
    if not os.path.isdir(target):
        os.mkdir(target)

    # Miramos que la lista de archivos a subir no esté vacía
    if request.files['file'].filename == '':
        print("Se debe de subir un archivo por lo menos")
        return redirect(url_for('index'))
    else:
        archiValidos = []
        textoSacado = []
        listaFalses = []
        # Recorremos los archivos, y aplicamos seguridad básica
        for file in request.files.getlist("file"):
            filename = file.filename

            # Si el archivo ha pasado la seguridad básica, se procesa.
            if archivoPermitido(filename):
                # Otra capa de seguridad
                filename = secure_filename(filename)
                destination = "/".join([target, filename])
                # Se guarda el archivo
                file.save(destination)
                # Leemos la información del archivo
                try:
                    textoSacado.append(ConversionPDF.validaInforme(destination, acepUser))
                except:
                    listaFalses.append(filename)

                # Una vez se ha subido el archivo y se ha procesado, se elimina
                if os.path.exists(destination):
                    os.remove(destination)
                    print("Archivo eliminado")
                else:
                    print("El archivo no existe")

    # Convertimos los datos antinguos a JSON
    oldData = json.loads(oldData)

    # Si existe id, solo, se devuelve solo la información nueva
    if "id" in oldData:
        for x in textoSacado:
            oldData["comparativa"].append(x)
        print(oldData)
        return render_template("public/study.html", data=json.dumps(oldData), listaNoValidos=listaFalses)
    else:
        print("No hay ID")
        for x in textoSacado:
            oldData.append(x)
        print(oldData)
        return render_template("public/study.html", data=json.dumps(oldData), listaNoValidos=listaFalses)
    # json
    # textoSacado

    # if tiene id devolvemos C
    # if not devolvemos ABC

# Listado de estudios guardados
@app.route("/list", methods=['POST', 'GET'])
def listaEstudios():
    response = estudiosMongo.listaEstudios()
    listadoJson = []
    for item in response:
        element = {
            'id': str(item['_id']),
            'nombre': item['nombre']
        }
        listadoJson.append(element)
    return Response(json.dumps(listadoJson),  mimetype='application/json')


# Carga de estudio
@app.route("/verDetalles", methods=['POST', 'GET'])
def verDetalles():
    data = request.get_json(force=True)
    detalles = estudiosMongo.findEstudio(data['id'])
    if '_id' in detalles:
        detalles['id'] = str(detalles['_id'])
        del detalles['_id']
    return Response(json.dumps(detalles), mimetype='application/json')

# Borrado de estudio (cuando borra no actualiza la lista)
@app.route("/borrarEstudio", methods=['POST', 'GET'])
def borrarEstudio():
    estudio = request.get_json(force=True)
    estudiosMongo.borrarEstudio(estudio['id'])
    return render_template("public/index.html")

# METODOS PARA TRATAR CON LAS ACEPCIONES
@app.route("/viewMeaning", methods=['GET'])
def verAcepciones():
    acepciones = acepcionesMongo.findAcepcionesByUser('default')
    return Response(json.dumps(acepciones['acepciones']), mimetype='application/json')


@app.route("/updateMeaning", methods=['POST'])
def updateAcepcion():
    listaAcepciones = request.get_json(force=True)
    listaAcepciones['user'] = 'default'
    acepcion = acepcionesMongo.actualizarAcepcion('default', listaAcepciones)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

# ESTADISTICAS
@app.route("/stadistics", methods=['GET', 'POST'])
def updateEstadisticas(centro):
    success = estadisticas.actualizarEstadistica(centro)
    if(success == True):
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
