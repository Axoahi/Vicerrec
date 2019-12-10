# coding=utf-8
import ast
import json

from flask import Flask, send_from_directory, after_this_request
import creadExport

app = Flask(__name__)

from flask import render_template
from flask import request, redirect, url_for, Response
from werkzeug.utils import secure_filename
import os
import ConversionPDF
import mongoDB
import json
import glob
from flask import jsonify

# Variable que nos marca que se permite subir
app.config["ALLOWED_EXTENSIONS"] = ["pdf"]
app.config["CLIENT_DIRECTORY"] = os.getcwd() + "/data/"


# Página index
@app.route("/")
def index():
    return render_template("/public/index.html")


@app.route("/about")
def about():
    return render_template("/public/about.html")


# Página de carga de archivos
@app.route("/upload", methods=['POST', 'GET'])
def loadWebpage():
    return render_template("public/upload.html")

# Procesamiento de subida de archivo, previo a muestra de
@app.route("/complete", methods=['POST', "GET"])
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


# Procesamiento de subida de archivo, previo a muestra de
@app.route("/newEst", methods=['POST', 'GET'])
def newEstudio():
    return render_template('public/mongoDB.html')


@app.route("/new", methods=['POST'])
def crearNuevoEstudio():
    estudio = request.get_json()
    id = mongoDB.crearEstudio(estudio)
    print(id)
    return render_template("public/about.html")


# Listado de estudios
@app.route("/listado", methods=['POST', 'GET'])
def listado():
    return render_template('public/mongoDB.html')


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
    # return jsonify(results=listadoJson)
    # return listadoJson
    return Response(json.dumps(listadoJson),  mimetype='application/json')


#Detalles de un estudio
@app.route("/detalles/<id>", methods=["GET"])
def detalles(id):
    datajson = {"id": id}
    return render_template("public/complete.html", data=json.dumps(datajson))


@app.route("/verDetalles", methods=['POST', 'GET'])
def verDetalles():
    data = request.get_json(force=True)
    print(data)
    detalles = mongoDB.findEstudio(data['id'])
    detalles['_id'] = str(detalles['_id'])
    print(detalles)
    return Response(json.dumps(detalles), mimetype='application/json')



# Actualizar un estudio
@app.route("/actualizar", methods=['POST', 'GET'])
def actualizar():
    return render_template('public/mongoDB.html')


@app.route("/actualizarEstudio", methods=['POST', 'GET'])
def actualizarEstudio():
    act = {
        "nombre": "Estudios de grado de alguna cosa",
        "comparativa": [{
            "codigo": 978454,
            "titulo": "GRADO EN QUÍMICA",
            "anyo": 1234,
            "gestiontitulo": {
                "organizacionydesarrollo": "AD",
                "informacionytransparencia": "AD",
                "SGIC": "AD"
            },
            "recursos": {
                "personalacademico": "SA",
                "apoyoyrecursosmateriales": "SA"
            },
            "resultados": {
                "resultados": "AD",
                "indicadores": "AD"
            },
            "finaltotal": "FAVORABLE",
            "recomendaciones": {
                "curriculum": ["Puede mejorar consulta a agentes externos (CR1) (CR3)"],
                "docentia": ["Se recomienda la implantación definitiva del programa DOCENTIA"],
                "web": ["Puede mejorar consulta a agentes externos (CR1) (CR3)"],
                "coordinacion": ["Mejorar coordinación entre actividades de evaluación y las docentes (CR1)"],
                "otras": ["Alumnado no conoce sistema de tramitación de quejas (CR1)",
                          "Puede mejorar consulta a agentes externos (CR1) (CR3)"]
            }

        },
            {
                "codigo": 123456,
                "titulo": "GRADO EN QUÍMICA",
                "anyo": 201414,
                "gestiontitulo": {
                    "organizacionydesarrollo": "AD",
                    "informacionytransparencia": "AD",
                    "SGIC": "AD"
                },
                "recursos": {
                    "personalacademico": "SA",
                    "apoyoyrecursosmateriales": "SA"
                },
                "resultados": {
                    "resultados": "AD",
                    "indicadores": "AD"
                },
                "finaltotal": "FAVORABLE",
                "recomendaciones": {
                    "curriculum": ["Se recomienda la implantación definitiva del programa DOCENTIA"],
                    "docentia": ["Se recomienda la implantación definitiva del programa DOCENTIA"],
                    "web": ["Se recomienda la implantación definitiva del programa DOCENTIA"],
                    "coordinacion": ["Mejorar coordinación entre actividades de evaluación y las docentes (CR1)"],
                    "otras": ["Alumnado no conoce sistema de tramitación de quejas (CR1)",
                              "Puede mejorar consulta a agentes externos (CR1) (CR3)"]
                }
            }]
    }
    estudio = mongoDB.actualizarEstudio("5dd68c5b676e2498b6a929a9", act)
    print(estudio)
    return render_template("public/about.html")


# Detalles de un estudio
@app.route("/borrar", methods=['POST', 'GET'])
def borrar():
    return render_template('public/mongoDB.html')


@app.route("/borrarEstudio", methods=['POST', 'GET'])
def borrarEstudio():
    estudio = request.get_json(force=True)
    mongoDB.borrarEstudio(estudio['id'])
    return render_template("public/about.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
