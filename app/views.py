import json

from flask import Flask
import creadExport

app = Flask(__name__)

from flask import render_template
from flask import request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import ConversionPDF
import mongoDB
import json


# Variable que nos marca que se permite subir
app.config["ALLOWED_EXTENSIONS"] = ["pdf"]
app.config["CLIENT_DIRECTORY"] = 'C:\\Users\\Buba\\Desktop\\LucentiaLab\\PDF2CSV\\PruebasFlask\\app\\data'

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
                textoSacado.append(json.loads(ConversionPDF.extraeInfo(destination)))

                #Una vez se ha subido el archivo y se ha procesado, se elimina
                if os.path.exists(destination):
                    os.remove(destination)
                    print("Archivo eliminado")
                else:
                    print("El archivo no existe")
        return render_template("public/complete.html", data=textoSacado)

# Procesamiento de subida de archivo, previo a muestra de
@app.route("/getExcel", methods=['POST','GET'])
def getExcel():

    ##### Variable auxiliar que debe ser sustituida por la lista de importada desde el front
    listaTitula = []
    titula = {
    "codigo": 696969,
    "titulo": "GRADO EN QUÍMICA",
    "anyo": 2014,
    "gestiontitulo": {
        "organizacionydesarrollo": "AD",
        "informacionytransparencia":"AD",
        "SGIC":"AD"
    },
    "recursos":{
        "personalacademico":"SA",
        "apoyoyrecursosmateriales":"SA"
    },
    "resultados":{
        "resultados": "AD",
        "indicadores": "AD"
    },
    "finaltotal":"FAVORABLE",
    "recomendaciones":{
        "curriculum": [],
        "docentia":["Se recomienda la implantación definitiva del programa DOCENTIA"],
        "web":[],
        "coordinacion":["Mejorar coordinación entre actividades de evaluación y las docentes (CR1)"],
        "otras":["Alumnado no conoce sistema de tramitación de quejas (CR1)",
                 "Puede mejorar consulta a agentes externos (CR1) (CR3)",
                 "Perfil de ingreso no bien definido puede explicar bajas tasas en algunos indicadores (CR1)",
                 "Potenciar acción tutorial (CR1)","Aumentar participacion estudiantes en encuestas (CR1) (CR3)",
                 "Difundir mejor informes de seguimiento del título (CR2)",
                 "Baja participación en programas de movilidad (CR2)",
                 "Faltan competencias básicas en guías docentes (CR2)",
                 "Adecuar programas de formación pedagógica del profesorado a las necesidades (CR3)",
                 "Profesorado desconoce y desconfía de resultados del SIGC, y alumnado lo desconoce también (CR3)",
                 "Falta información de sexenios y quinquenios del profesorado (CR4)",
                 "Poca información sobre movilidad y prácticas en empresas (CR5)",
                 "Baja tasa de rendimiento en algunas asignaturas (CR6)",
                 "Posibilidad de curso cero o cambiar perfil de ingreso (CR6)",
                 "Alumnado solicita formación (en plan de estudios o no) sobre comunicación y relaciones con clientes/emprendimiento (CR6)","Tasa de abandono superior a la memoria (CR7)","Revisar encuestas para incluir competencias (CR7)","Necesario aumentar la participación de los alumnos en encuestas (CR7)","Actualizar el Plan de  actuación institucional en lo referente a inserción laboral, aunque los resultados son aceptables (CR7)"]
    }
}
    listaTitula.append(titula)
    listaTitula.append(titula)
    ###############################################################################

    nombreEstudio = request.form["excel-name"]
    # Se crea el archivo y se devuelve ruta y nombre para bajar y eliminar
    nombre = creadExport.exportarExcel(nombreEstudio, listaTitula) + ".xls"
    try:
        print('/data/' + nombre)
        return send_from_directory(
            app.config["CLIENT_DIRECTORY"], filename=nombre, as_attachment=True)

    except FileNotFoundError:
            abort(404)

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

@app.route("/new", methods=['POST','GET'])
def crearNuevoEstudio():
    comparativa = {
        "nombre": "Estudios de grado de alguna cosa",
        "comparativa": [{
            "codigo": 11111111,
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
                "curriculum": [],
                "docentia": ["Se recomienda la implantación definitiva del programa DOCENTIA"],
                "web": [],
                "coordinacion": ["Mejorar coordinación entre actividades de evaluación y las docentes (CR1)"],
                "otras": ["Alumnado no conoce sistema de tramitación de quejas (CR1)",
                          "Puede mejorar consulta a agentes externos (CR1) (CR3)",
                          "Perfil de ingreso no bien definido puede explicar bajas tasas en algunos indicadores (CR1)",
                          "Potenciar acción tutorial (CR1)",
                          "Aumentar participacion estudiantes en encuestas (CR1) (CR3)",
                          "Difundir mejor informes de seguimiento del título (CR2)",
                          "Baja participación en programas de movilidad (CR2)",
                          "Faltan competencias básicas en guías docentes (CR2)",
                          "Adecuar programas de formación pedagógica del profesorado a las necesidades (CR3)",
                          "Profesorado desconoce y desconfía de resultados del SIGC, y alumnado lo desconoce también (CR3)",
                          "Falta información de sexenios y quinquenios del profesorado (CR4)",
                          "Poca información sobre movilidad y prácticas en empresas (CR5)",
                          "Baja tasa de rendimiento en algunas asignaturas (CR6)",
                          "Posibilidad de curso cero o cambiar perfil de ingreso (CR6)",
                          "Alumnado solicita formación (en plan de estudios o no) sobre comunicación y relaciones con clientes/emprendimiento (CR6)",
                          "Tasa de abandono superior a la memoria (CR7)",
                          "Revisar encuestas para incluir competencias (CR7)",
                          "Necesario aumentar la participación de los alumnos en encuestas (CR7)",
                          "Actualizar el Plan de  actuación institucional en lo referente a inserción laboral, aunque los resultados son aceptables (CR7)"]
            }

        },
            {
                "codigo": 222222,
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
                    "curriculum": [],
                    "docentia": ["Se recomienda la implantación definitiva del programa DOCENTIA"],
                    "web": [],
                    "coordinacion": ["Mejorar coordinación entre actividades de evaluación y las docentes (CR1)"],
                    "otras": ["Alumnado no conoce sistema de tramitación de quejas (CR1)",
                              "Puede mejorar consulta a agentes externos (CR1) (CR3)",
                              "Perfil de ingreso no bien definido puede explicar bajas tasas en algunos indicadores (CR1)",
                              "Potenciar acción tutorial (CR1)",
                              "Aumentar participacion estudiantes en encuestas (CR1) (CR3)",
                              "Difundir mejor informes de seguimiento del título (CR2)",
                              "Baja participación en programas de movilidad (CR2)",
                              "Faltan competencias básicas en guías docentes (CR2)",
                              "Adecuar programas de formación pedagógica del profesorado a las necesidades (CR3)",
                              "Profesorado desconoce y desconfía de resultados del SIGC, y alumnado lo desconoce también (CR3)",
                              "Falta información de sexenios y quinquenios del profesorado (CR4)",
                              "Poca información sobre movilidad y prácticas en empresas (CR5)",
                              "Baja tasa de rendimiento en algunas asignaturas (CR6)",
                              "Posibilidad de curso cero o cambiar perfil de ingreso (CR6)",
                              "Alumnado solicita formación (en plan de estudios o no) sobre comunicación y relaciones con clientes/emprendimiento (CR6)",
                              "Tasa de abandono superior a la memoria (CR7)",
                              "Revisar encuestas para incluir competencias (CR7)",
                              "Necesario aumentar la participación de los alumnos en encuestas (CR7)",
                              "Actualizar el Plan de  actuación institucional en lo referente a inserción laboral, aunque los resultados son aceptables (CR7)"]
                }
            }]
    }
    id = mongoDB.crearEstudio(comparativa)
    print(id)
    return render_template("public/about.html")

#Listado de estudios
@app.route("/listado", methods=['POST', 'GET'])
def listado():
    return render_template('public/mongoDB.html')

@app.route("/list", methods=['POST','GET'])
def listaEstudios():
    listado = mongoDB.listaEstudios()
    for item in listado:
        print(item)
    return render_template("public/about.html")

#Detalles de un estudio
@app.route("/detalles", methods=['POST', 'GET'])
def detalles():
    return render_template('public/mongoDB.html')

@app.route("/verDetalles", methods=['POST','GET'])
def verDetalles():
    detallesEstudio = mongoDB.findEstudio("5dd68c5b676e2498b6a929a9")
    print(detallesEstudio)
    return render_template("public/about.html")

#Actualizar un estudio
@app.route("/actualizar", methods=['POST', 'GET'])
def actualizar():
    return render_template('public/mongoDB.html')

@app.route("/actualizarEstudio", methods=['POST','GET'])
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

#Detalles de un estudio
@app.route("/borrar", methods=['POST', 'GET'])
def borrar():
    return render_template('public/mongoDB.html')

@app.route("/borrarEstudio", methods=['POST','GET'])
def borrarEstudio():
    mongoDB.borrarEstudio("5dd68c5b676e2498b6a929a9")
    return render_template("public/about.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
