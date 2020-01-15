# coding=utf-8
from flask import jsonify
import glob
import mongoDB
import ConversionPDF
import os
from werkzeug.utils import secure_filename
from flask import request, redirect, url_for, Response
from flask import render_template
import ast
import json

from flask import Flask, send_from_directory, after_this_request
import creadExport

app = Flask(__name__)


# Variable que nos marca que se permite subir
app.config["ALLOWED_EXTENSIONS"] = ["pdf"]
app.config["CLIENT_DIRECTORY"] = os.getcwd() + "/data/"


def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)


# Pagina index
@app.route("/")
def index():
    return render_template("/public/index.html")

# Pagina comparativa guardada
@app.route("/compare/<id>", methods=["GET"])
def getIdStudyComparative(id):
    datajson = {"id": id}
    return render_template("public/compare.html", data=json.dumps(datajson))

# Pagina detalle guardado
@app.route("/detail/<id>", methods=["GET"])
def detalles(id):
    datajson = {"id": id}
    return render_template("public/complete.html", data=json.dumps(datajson))

# Página nuevo estudio
@app.route("/detail", methods=['POST', "GET"])
def upload():
    # Borramos todos los archivos excel que existan previamente en el servidor
    files = glob.glob(app.config["CLIENT_DIRECTORY"]+"*.xls")
    for f in files:
        os.remove(f)

    target = os.path.join(app.instance_path)
    # Si no existe el directorio donde dejar los archivos, se crea
    if not os.path.isdir(target):
        os.mkdir(target)

    # Miramos que la lista de archivos a subir no esté vacía
    if request.files['file'].filename == '':
        print("Se debe de subir un archivo por lo menos")
        return redirect(url_for('about'))
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
                textoSacado.append(ConversionPDF.extraeInfo(destination))

                # Una vez se ha subido el archivo y se ha procesado, se elimina
                if os.path.exists(destination):
                    os.remove(destination)
                    print("Archivo eliminado")
                else:
                    print("El archivo no existe")
        
    return render_template("public/complete.html", data=json.dumps(textoSacado))

# Página compare
@app.route("/compare")
def compare():
    return render_template("/public/compare.html")

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

# Procesamiento de subida de archivo, previo a muestra de
@app.route("/getExcel", methods=['POST'])
def getExcel():
    nombre = request.form["pynombre"]
    listado = request.form["pylistadoAneca"]
    newlistado = ast.literal_eval(listado)
    # Se crea el archivo y se devuelve ruta y nombre para bajar y eliminar
    nombreFile = creadExport.exportarExcel(nombre, newlistado) + ".xls"
    print(os.getcwd())
    print(app.config['CLIENT_DIRECTORY'])
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
    id = mongoDB.crearEstudio(estudio)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

# Actualizar un estudio
@app.route("/actualizar", methods=['POST', 'GET'])
def actualizar():
    return render_template('public/complete.html')

# Listado de estudios guardados
@app.route("/list", methods=['POST', 'GET'])
def listaEstudios():
    response = mongoDB.listaEstudios()
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
    detalles = mongoDB.findEstudio(data['id'])
    detalles['_id'] = str(detalles['_id'])
    return Response(json.dumps(detalles), mimetype='application/json')

# Borrado de estudio (cuando borra no actualiza la lista)
@app.route("/borrarEstudio", methods=['POST', 'GET'])
def borrarEstudio():
    estudio = request.get_json(force=True)
    mongoDB.borrarEstudio(estudio['id'])
    return render_template("public/index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
