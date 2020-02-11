import json
import pandas as pd
import os
import ast

def creaJSON(codig, titulo, anyo, centro, tipoInforme, criterios, valoracionGlobal, observaciones):
    data = {
                "codigo": codig,
                "titulo": titulo,
                "anyo": anyo,
                "centro": centro,
                "tipoInforme": tipoInforme,
                "gestiontitulo": {
                    "organizacionydesarrollo": criterios[0],
                    "informacionytransparencia":criterios[1],
                    "SGIC":criterios[2]
                },
                "recursos":{
                    "personalacademico":criterios[3],
                    "apoyoyrecursosmateriales":criterios[4]
                },
                "resultados":{
                    "resultados": criterios[5],
                    "indicadores": criterios[6]
                },
                "finaltotal":valoracionGlobal,
                "recomendaciones":{
                    "curriculum": observaciones[0],
                    "docentia":observaciones[1],
                    "web":observaciones[2],
                    "coordinacion":observaciones[3],
                    "otras": observaciones[4]
                }
            }

    return data


def aplanarRecomendaciones(lista):
    recomendacion = ""
    for i in range(0,len(lista)):
        if( i == len(lista)):
            recomendacion = recomendacion + lista[i]
        else:
            recomendacion = recomendacion + lista[i] + ' - '
    return recomendacion

def exportarExcel(nombreExcel, listadoJSON):
    lista = ["Código","Título", "Año","Centro", "Tipo de informe", "Organización y desarrollo","Información y transparencia","SGIC",
             "Personal Académico","Apoyo y recursos materiales","Resultados","Indicadores","Nota Final",
             "CURRÍCULUM","DOCENTIA","WEB","COORDINACIÓN","OTRAS"]
    df = pd.DataFrame(columns=lista)
    for i in range(0,len(listadoJSON)):
        print("ITERACION;", i)
        item = listadoJSON[i]
        Codigo = item["codigo"]
        Titulo = item["titulo"]
        Anyo = item["anyo"]
        Centro = item["centro"]
        Tipo_de_Informe = item["tipoInforme"]
        Organizacion_y_desarrollo = item["gestiontitulo"]["organizacionydesarrollo"]
        Informacion_y_transparencia = item["gestiontitulo"]["informacionytransparencia"]
        SGIC = item["gestiontitulo"]["SGIC"]
        Personal_academico = item["recursos"]["personalacademico"]
        Apoyo_y_recursos_materiales = item["recursos"]["apoyoyrecursosmateriales"]
        Resultados = item["resultados"]["resultados"]
        Indicadores = item["resultados"]["indicadores"]
        Nota_Final = item["finaltotal"]
        curriculum = aplanarRecomendaciones(item["recomendaciones"]["curriculum"])
        docentia = aplanarRecomendaciones(item["recomendaciones"]["docentia"])
        web = aplanarRecomendaciones(item["recomendaciones"]["web"])
        coordinacion = aplanarRecomendaciones(item["recomendaciones"]["coordinacion"])
        otras = aplanarRecomendaciones(item["recomendaciones"]["otras"])
       
        data = [Codigo,Titulo,Anyo,Centro, Tipo_de_Informe, Organizacion_y_desarrollo,Informacion_y_transparencia,SGIC,Personal_academico,Apoyo_y_recursos_materiales,Resultados,Indicadores,Nota_Final,curriculum,docentia,web,coordinacion,otras]
        df_item = pd.DataFrame([data],columns=lista)
        df = df.append(df_item)
    df.to_excel(os.getcwd() + "/data/" + nombreExcel + ".xls", index=False)

    return nombreExcel


def creaEstudio(nombEstudio, listaTitula):
    estudio = {
        "nombre": nombEstudio,
        "comparativa": listaTitula
    }

    return estudio
