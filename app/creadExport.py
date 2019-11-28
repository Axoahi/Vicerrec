import json
import pandas as pd
import ast

def creaJSON(codig, titulo, anyo, criterios, valoracionGlobal, observaciones):
    data = {
                "codigo": codig,
                "titulo": titulo,
                "anyo": anyo,
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
    lista = ["codigo","titulo", "anyo","crit1","crit2","crit3","crit4","crit5","crit6","crit7","final","curriculum","docentia","web","coordinacion","otras"]
    df = pd.DataFrame(columns=lista)
    for i in range(0,len(listadoJSON)):
        print("ITERACION;", i)
        item = listadoJSON[i]
        codigo = item["codigo"]
        titulo = item["titulo"]
        anyo = item["anyo"]
        crit1 = item["gestiontitulo"]["organizacionydesarrollo"]
        crit2 = item["gestiontitulo"]["informacionytransparencia"]
        crit3 = item["gestiontitulo"]["SGIC"]
        crit4 = item["recursos"]["personalacademico"]
        crit5 = item["recursos"]["apoyoyrecursosmateriales"]
        crit6 = item["resultados"]["resultados"]
        crit7 = item["resultados"]["indicadores"]
        final = item["finaltotal"]
        curriculum = aplanarRecomendaciones(item["recomendaciones"]["curriculum"])
        docentia = aplanarRecomendaciones(item["recomendaciones"]["docentia"])
        web = aplanarRecomendaciones(item["recomendaciones"]["web"])
        coordinacion = aplanarRecomendaciones(item["recomendaciones"]["coordinacion"])
        otras = aplanarRecomendaciones(item["recomendaciones"]["otras"])
       
        data = [codigo,titulo,anyo,crit1,crit2,crit3,crit4,crit5,crit6,crit7,final,curriculum,docentia,web,coordinacion,otras]
        df_item = pd.DataFrame([data],columns=lista)
        df = df.append(df_item)
    df.to_excel("data/" + nombreExcel + ".xls")

    return nombreExcel


def creaEstudio(nombEstudio, listaTitula):
    estudio = {
        "nombre": nombEstudio,
        "comparativa": listaTitula
    }

    return estudio