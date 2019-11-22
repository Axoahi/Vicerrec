import json

import tika
import itertools
from tika import parser
import re
import creadExport

tika.initVM()


def extraeInfo(fileName):
    ###### BÚSQUEDA DE RECOMENDACIONES ################################
    recomendaciones = [['curriculum', 'currículum', 'currícula', 'curricula'],
                       ['docentia', 'DOCENTIA'],
                       ['web'],
                       ['coordinación', 'coordinacion'],
                       ['se recomienda', 'se aconseja', 'optimizar', 'revisar', 'baja respuesta',
                        'baja participación', 'baja satisfacción', 'insatisfacción', 'abandono',
                        'se debe', 'se propone', 'CAT']]

    parsed = parser.from_file(fileName)
    textoraw = parsed['content']

    # Eliminamos todas los saltos de línea para tenerlo todo junto
    textofilter = re.sub("\\n", " ", textoraw)
    prueba2 = re.sub("\\s\\s", " ", textofilter)

    # Extracción código
    numRUCT = re.search("Número de RUCT:(.*) Fecha ", prueba2)
    numRUCT = numRUCT[1].lstrip()

    # Extracción título
    titulo = re.search("(Título(.*) Universidad:)", prueba2)
    titulo = titulo[0].replace("Título: ", "").replace(" Universidad:", "")

    # Extracción año
    anyo = re.search("verificación:\s*(\d*)\s*Valoración", prueba2)
    anyo = anyo[1]

    # Extracción universidad
    universidad = re.search("(Universidad: )(.*)Centro:", prueba2)
    universidad = universidad[0].replace("Universidad: ", "").replace(" Centro:", "")

    # Extracción rama
    rama = re.search("(cimiento: )(.*)Créditos:", prueba2)
    rama = rama[0].replace("cimiento: ", "").replace(" Créditos:", "")

    # Extracción créditos
    creditos = re.search("(Créditos: )(\d+)", prueba2)
    creditos = creditos[0].replace("Créditos: ", "")

    # Extracción nºplazas
    nplazas = re.search("(Nº plazas: )(\d+)", prueba2)
    nplazas = nplazas[0].replace("Nº plazas: ", "")

    # Extracción de centro (se me había olvidado, ups)
    centro = re.search("(Centro: )(.*)Rama de conocimiento:", prueba2)
    centro = centro[0].replace("Centro: ", "").replace(" Rama de conocimiento:", "")

    # Extracción de fecha
    fecha = re.search("(Fecha verificación: )(\d+)", prueba2)
    fecha = fecha[0].replace("Fecha verificación: ", "")

    #### Array de criterios ######
    ## Del 1 al 7, según criterios medidos. Para cada criterio
    ## [0]: Valoración del criterio
    ## [1]: Estándard del criterio
    ## [2]: Descripción del criterio

    # Lista de criterios básicos para la creación del JSON final
    listValCrit = []

    arrayCriterios = []
    auxCriterio = []

    # CRITERIO 1
    # Extracción valoración criterio 1
    crit1 = re.search("(Organización y desarrollo \(Criterio 1\))(.*)Información y transparencia \(Criterio 2\)",
                      prueba2)
    crit1 = crit1[0].replace("Organización y desarrollo (Criterio 1) ", "").replace(
        "Información y transparencia (Criterio 2)", "")
    # Se añade al listado de criterios, y se añade la valoración básica al listado de valoraciones listValCrit
    auxCriterio.append(crit1)
    listValCrit.append(crit1)

    # Extracción estándard de criterio 1
    crit1est = re.search("Criterio 1\.\- Organización y desarrollo\.(\s*?)(.*?)Calificación", prueba2)
    crit1est = crit1est[0].replace("Calificación", "").replace("Estándar", "").replace(
        "Criterio 1.- Organización y desarrollo.", "")
    crit1est = crit1est.lstrip().rstrip()
    auxCriterio.append(crit1est)
    # Extracción de valoración descriptiva de criterio 1
    buff = re.search(
        "Criterio 1\.\- Organización y desarrollo.*?Valoración descriptiva(.*?)INFORME DEFINITIVO DE RENOVACIÓN",
        prueba2)
    crit1ValDes = buff[1].lstrip().rstrip()
    auxCriterio.append(crit1ValDes)
    # Inserción en arrayCriterios y reinicio de variable auxiliar de criterio
    arrayCriterios.append(auxCriterio)
    auxCriterio = []

    # CRITERIO 2
    # Extracción valoración criterio 2
    crit2 = re.search(
        "(Información y transparencia \(Criterio 2\))(.*)Sistema de garantía interno de calidad \(Criterio 3\)",
        prueba2)
    crit2 = crit2[0].replace("Información y transparencia (Criterio 2) ", "").replace(
        "Sistema de garantía interno de calidad (Criterio 3)", "")
    auxCriterio.append(crit2)
    listValCrit.append(crit2)

    # Extracción estándar de criterio 2
    buffXX = re.search("Criterio 2\.\- Información y transparencia.\s*?Estándar(.*?)Calificación", prueba2)
    crit2est = buffXX[1]
    crit2est = crit2est.lstrip().rstrip()
    auxCriterio.append(crit2est)
    # Extracción de valoración descriptiva de criterio 2
    buff = re.search(
        "Criterio 2\.\- Información y transparencia\..*?Valoración descriptiva(.*?)INFORME DEFINITIVO DE RENOVACIÓN",
        prueba2)
    crit2ValDes = buff[1].lstrip().rstrip()
    auxCriterio.append(crit2ValDes)
    # Inserción en arrayCriterios y reinicio de variable auxiliar de criterio
    arrayCriterios.append(auxCriterio)
    auxCriterio = []

    # CRITERIO 3
    # Extracción valoración criterio 3
    crit3 = re.search("(Sistema de garantía interno de calidad \(Criterio 3\))(.*)Personal académico \(Criterio 4\)",
                      prueba2)
    crit3 = crit3[0].replace("Sistema de garantía interno de calidad (Criterio 3) ", "").replace(
        "Personal académico (Criterio 4)", "")
    auxCriterio.append(crit3)
    listValCrit.append(crit3)

    # Extracción estándar de criterio 3
    buff = re.search("Criterio 3\.\- Sistema de garantía interno de calidad \(SGIC\)\.(\s*?)Estándar(.*?)Calificación",
                     prueba2)
    crit3est = buff[2]
    crit3est = crit3est.lstrip().rstrip()
    auxCriterio.append(crit3est)
    # Extracción de valoración descriptiva de criterio 3
    buff = re.search(
        "Criterio 3\.\- Sistema de garantía interno de calidad \(SGIC\)\..*?Valoración descriptiva(.*?)INFORME DEFINITIVO DE RENOVACIÓN",
        prueba2)
    crit3ValDes = buff[1].lstrip().rstrip()
    auxCriterio.append(crit3ValDes)
    # Inserción en arrayCriterios y reinicio de variable auxiliar de criterio
    arrayCriterios.append(auxCriterio)
    auxCriterio = []

    # CRITERIO 4
    # Extracción valoración criterio 4
    crit4 = re.search(
        "(Personal académico \(Criterio 4\))(.*)Personal de apoyo, recursos materiales y servicios \(Criterio 5\)",
        prueba2)
    crit4 = crit4[0].replace("Personal académico (Criterio 4) ", "").replace(
        "Personal de apoyo, recursos materiales y servicios (Criterio 5)", "")
    auxCriterio.append(crit4)
    listValCrit.append(crit4)

    # Extracción estándar de criterio 4
    buff = re.search("Criterio 4\.\- Personal académico\.(\s*?)Estándar(.*?)Calificación", prueba2)
    crit4est = buff[2]
    crit4est = crit4est.lstrip().rstrip()
    auxCriterio.append(crit4est)
    # Extracción de valoración descriptiva de criterio 2
    buff = re.search(
        "Criterio 4\.\- Personal académico\..*?Valoración descriptiva(.*?)INFORME DEFINITIVO DE RENOVACIÓN",
        prueba2)
    crit4ValDes = buff[1].lstrip().rstrip()
    auxCriterio.append(crit4ValDes)
    # Inserción en arrayCriterios y reinicio de variable auxiliar de criterio
    arrayCriterios.append(auxCriterio)
    auxCriterio = []

    # CRITERIO 5
    # Extracción valoración criterio 5
    crit5 = re.search(
        "(Personal de apoyo, recursos materiales y servicios \(Criterio 5\))(.*)Resultados de Aprendizaje \(Criterio 6\)",
        prueba2)
    crit5 = crit5[0].replace("Personal de apoyo, recursos materiales y servicios (Criterio 5) ", "").replace(
        "Resultados de Aprendizaje (Criterio 6)", "")
    auxCriterio.append(crit5)
    listValCrit.append(crit5)

    # Extracción estándar de criterio 5
    buff = re.search(
        "Criterio 5\.\- Personal de apoyo, recursos materiales y servicios\.(\s*?)Estándar(.*?)Calificación",
        prueba2)
    crit5est = buff[2]
    crit5est = crit5est.lstrip().rstrip()
    auxCriterio.append(crit5est)
    # Extracción de valoración descriptiva de criterio 2
    buff = re.search(
        "Criterio 5\.\- Personal de apoyo, recursos materiales y servicios\..*?Valoración descriptiva(.*?)INFORME DEFINITIVO DE RENOVACIÓN",
        prueba2)
    crit5ValDes = buff[1].lstrip().rstrip()
    auxCriterio.append(crit5ValDes)
    # Inserción en arrayCriterios y reinicio de variable auxiliar de criterio
    arrayCriterios.append(auxCriterio)
    auxCriterio = []

    # CRITERIO 6
    # Extracción valoración criterio 6
    crit6 = re.search(
        "(Resultados de Aprendizaje \(Criterio 6\))(.*)Indicadores de Satisfacción y Rendimiento \(Criterio 7\)",
        prueba2)
    crit6 = crit6[0].replace("Resultados de Aprendizaje (Criterio 6) ", "").replace(
        "Indicadores de Satisfacción y Rendimiento (Criterio 7)", "")
    auxCriterio.append(crit6)
    listValCrit.append(crit6)

    # Extracción estándar de criterio 6
    buff = re.search("Criterio 6\.\- Resultados de Aprendizaje\.(\s*?)Estándar(.*?)Calificación", prueba2)
    crit6est = buff[2]
    crit6est = crit6est.lstrip().rstrip()
    auxCriterio.append(crit6est)
    # Extracción de valoración descriptiva de criterio 2
    buff = re.search(
        "Criterio 6\.\- Resultados de Aprendizaje\..*?Valoración descriptiva(.*?)INFORME DEFINITIVO DE RENOVACIÓN",
        prueba2)
    crit6ValDes = buff[1].lstrip().rstrip()
    auxCriterio.append(crit6ValDes)
    # Inserción en arrayCriterios y reinicio de variable auxiliar de criterio
    arrayCriterios.append(auxCriterio)
    auxCriterio = []

    # CRITERIO 7
    # Extracción valoración criterio 7
    crit7 = re.search(
        "(Indicadores de Satisfacción y Rendimiento \(Criterio 7\))(.*)Escala:",
        prueba2)
    crit7 = crit7[0].replace("Indicadores de Satisfacción y Rendimiento (Criterio 7) ", "").replace(
        "Escala: se supera excelentemente, se alcanza, se alcanza parcialmente y no se alcanza.", "")
    auxCriterio.append(crit7)
    listValCrit.append(crit7)

    # Extracción estándar de criterio 7
    buff = re.search("Criterio 7\.\- Indicadores de Satisfacción y Rendimiento\.(\s*?)Estándar(.*?)Calificación",
                     prueba2)
    crit7est = buff[2]
    crit7est = crit7est.lstrip().rstrip()
    auxCriterio.append(crit7est)
    # Extracción de valoración descriptiva de criterio 2
    buff = re.search(
        "Criterio 7\.\- Indicadores de Satisfacción y Rendimiento\..*?Valoración descriptiva(.*?)INFORME DEFINITIVO DE RENOVACIÓN",
        prueba2)
    crit7ValDes = buff[1].lstrip().rstrip()
    auxCriterio.append(crit7ValDes)
    # Inserción en arrayCriterios y reinicio de variable auxiliar de criterio
    arrayCriterios.append(auxCriterio)
    auxCriterio = []

    # Extracción valoración global
    # Al añadir el ? dentro del (.*?) hacemos que no busque de manera tan greedy, y solo se queda con la primera solución
    valGlob = re.search("(Valoración global )(.*?)INFORME DEFINITIVO DE RENOVACIÓN", prueba2)
    valGlob = valGlob[0].replace("Valoración global ", "").replace("INFORME DEFINITIVO DE RENOVACIÓN", "")
    # Esta línea elimina los espacios del string al principio (a la parte left, por eso la l del lstrip)
    # también está el comando rstrip, para eliminar a la derecha (que sería el que sustituiría a nuesto  valGlob[:-1])
    valGlob = valGlob.lstrip()

    # Se obtiene un array 2D con todos los criterios, y las frases que conforman cada criterio
    arrayFrases = []
    for i in range(len(arrayCriterios)):
        aux = []
        aux = arrayCriterios[i][2].split(". ")
        arrayFrases.append(aux)

    # +
    # MAIN de descomposición de todas las frases
    frasesJSON = []
    otrosJSON = []
    for iteraFra in range(len(arrayFrases)):
        frases = arrayFrases[iteraFra]
        # Se obtienen todos los camposClave, excepto el últio (Otros)
        indices = extraeIndFrases(frases, recomendaciones[:-1])
        #     print(indices)
        frasesSacadas = extraeFrases(frases, indices, iteraFra)
        #     print(frasesSacadas)
        #     print("(-------------)")
        frasesJSON.append(frasesSacadas)

        # Se eliminan las frases ya usadas
        frasesOtros = limpiaFrases(frases.copy(), indices)

        # Se extraen las frases para Otros de las frases limpias
        indicesOtros = extraeIndFrases(frasesOtros, [recomendaciones[-1]])
        frasesSacadas = extraeFrases(frasesOtros, indicesOtros, iteraFra)
        otrosJSON.append(frasesSacadas)

    # Finalmente, se reestructuran frasesJSON (con las frases de los
    # principales campos clave) y el frasesOtros (con las frases del
    # campoClave "Otros") para que tengan la estructua necesaria para formar
    # el JSON
    criteriosJSON = reordena(frasesJSON, otrosJSON, recomendaciones)

    dataTo = creadExport.creaJSON(numRUCT, titulo, anyo, listValCrit, valGlob, criteriosJSON)
    dataToFront = json.dumps(dataTo, sort_keys = False, indent = 2)
    return (dataToFront)


# Método para facilitar la visualización de las frases
def verFrases(frases):
    for i in range(len(frases)):
        print(i)
        print(frases[i])
        print("-----------------------")


# Creamos un método que extrae los índices de las frases. Dichas frases serán también eliminadas a posteriori
# antes de acceder al apartado de Otros
def extraeIndFrases(listaFrases, recomendas):
    listIndCampClav = []
    for campoClave in recomendas:
        auxInd = extraeAcepciones(listaFrases, campoClave)
        listIndCampClav.append(auxInd)
    return listIndCampClav


# Extraemos todos los índices que asociados a un campo clave, en todas sus variantes
def extraeAcepciones(listFrases, listAcep):
    listIndices = []
    for acep in listAcep:
        for indFrase in range(len(listFrases)):
            if acep in listFrases[indFrase].lower():
                listIndices.append(indFrase)
    return listIndices


# Extraigo las frases y les añado el criterio al que pertenecen, y los meto en la lista de criterios
def extraeFrases(frasesCriterio, indCC, numCrit):
    listaCriterios = []
    for crit in range(len(indCC)):

        # Si la lista está vacía
        if not indCC[crit]:
            listaCriterios.append("[]")
        else:
            auxList = []
            for y in range(len(indCC[crit])):
                auxList = frasesCriterio[indCC[crit][y]] + " (CR" + str(numCrit + 1) + ")"
                listaCriterios.append(auxList)
    return listaCriterios


# Preprocesado de las frases antes de acceder a Otros: Se eliminan
# las frases que han sido usadas en las recomendaciones normales,
# para que no se dupliquen en Otros
def limpiaFrases(frasesALimpiar, indCriter):
    # Como primer paso, se obtiene una lista de frases a eliminar (por índice), ordenadas
    # de mayor a menor
    flat_list = list(set([item for sublist in indCriter for item in sublist]))
    flat_list.sort(reverse=True)

    # A continuación se eliminan todos las frases de dicha lista
    for i in flat_list:
        del frasesALimpiar[i]
    return frasesALimpiar


# # Reordenado y limpieza de los dos listados antes de la creación del
# # # JSON final
# # def preparaJSONfinal(listaCriterios, otrosCriterios):
# #     auxCriterio = []
# #     finalJSON = []
# #     for i in range(len(listaCriterios)):
# #         auxCriterio.clear()
# #         auxCriterio.append(listaCriterios[i])
# #         auxCriterio.append(otrosCriterios[i])
# #
# #         #         print(auxCriterio)
# #         #         print("--------------")
# #
# #         # Deshacemos todas las listas anidadas para "flatear"
# #         chain = itertools.chain(*auxCriterio)
# #         #         print(list(chain))
# #         #        print("-----------")
# #         cleanSent = [x for x in chain if x != '[]']
# #         #         print(mierda)
# #         finalJSON.append(cleanSent)
# #     return finalJSON


# Reordenamiento de las frases sacadas del JSON
def reordena(frases, otrosJSON, recomendaciones):
    recomend = recomendaciones[:-1]
    listaplana = list(itertools.chain(*frases))

    # Se crea una lista con X posiciones vacías (se debe hacer así), que será
    # la variable a devolver
    listaOrdenada = []
    for i in range(len(recomend)):
        listaOrdenada.append([])

    # Iteramos por cada acepción de cada campo clave
    for intcc in range(len(recomend)):
        for intcadaAcep in range(len(recomend[intcc])):
            # Buscamos cada acepción en cada frases, y si está la añadimos a la lista correspondiente
            for sent in listaplana:
                if recomend[intcc][intcadaAcep] in sent:
                    listaOrdenada[intcc].append(sent)

    ###Añadimos las frases de Otros
    # 1ro flateamos el JSON y eliminamos listas vacías
    merged = itertools.chain(*otrosJSON)
    flated = list(merged)
    cleanSent = [x for x in flated if x != '[]']
    listaOrdenada.append(cleanSent)

    # Devolvemos la lista ordenada a la cuál se le ha anexado listaOtros flateada
    return (listaOrdenada)
