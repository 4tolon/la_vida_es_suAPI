import pandas as pd
import sqlalchemy as alch
from dotenv import load_dotenv
load_dotenv()
import os
import sys
import ast
import sqlalchemy as alch
password = os.getenv('pass_sql')
dbName="LaVidaEsSueno"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)

def check(que,string):
    """
    Función parametrizada que comprueba en cada tabla si existe el personje, texto, jornada o verso.
    Devuelve True si existe y False si no
    """
    if que == "personaje":
        query = list(engine.execute(f"SELECT nombre FROM personaje WHERE nombre = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
        
    elif que == "obra":
        query = list(engine.execute(f"SELECT texto FROM obra WHERE texto = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
        
    elif que == "jornada":
        query = list(engine.execute(f"SELECT nombre_del_acto FROM jornada WHERE nombre_del_acto = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
        
    elif que == "verso":
        query = list(engine.execute(f"SELECT verso_suelto FROM versos WHERE verso_suelto = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False

    elif que == "time":
        query = list(engine.execute(f"SELECT tiempo FROM tiempo WHERE tiempo = {string}"))
        if len(query) > 0:
            return True
        else:
            return False


def insertPersonaje(col,string):
    """
    Llama a la función check para comprobar si existe el personaje
    Inserta personaje si no existe
    """
    if check("personaje", string):
        return "el personaje existe"
    else:
        engine.execute(f"INSERT INTO personaje (nombre) VALUES ('{string}');")

def insertJornada(col, string):
    """
    Llama a la función check para comprobar si existe la jornada
    Inserta la jornada si no existe
    """
    if check("jornada ", string):
        return "la jornada existe"
    else:
        engine.execute(f"INSERT INTO jornada (nombre_del_acto) VALUES ('{string}');")

def dameId(que,string):
    """
    Devuelve el ID de lo que le pidamos sabiendo que ese elemento EXISTE
    """
    if que == "personaje":
        return list(engine.execute(f"SELECT idPersonaje FROM personaje WHERE nombre ='{string}';"))[0][0]
    elif que == "jornada":
        return list(engine.execute(f"SELECT idjornada FROM jornada WHERE nombre_del_acto ='{string}';"))[0][0]
    elif que == "obra":
        return list(engine.execute(f"SELECT idtexto FROM obra WHERE texto ='{string}';"))[0][0]

def insertObra(col, tex, n_inter, n_ver, col4, col2):
    """
    Llama a la función check para comprobar si existe el n_ver
    Inserta todos los datos de la tabla texto
    col4 = jornada
    col2 = presonaje
    """
    if check("texto", tex):
        return "el texto existe"
    else:
        idjornada = dameId( 'jornada', col4)
        idPesonaje = dameId('personaje', col2)
        engine.execute(f"INSERT INTO obra (texto, n_interven, n_versos, jornada_idjornada, Personaje_idPersonaje) VALUES ('{tex}','{n_inter}','{n_ver}','{idjornada}', '{idPesonaje}');")

def insertVersos(col, string, obr):
    """
    Llama a la función check para comprobar si existe la jornada
    Inserta la jornada si no existe
    """
    if check("verso ", string):
        return "el verso existe"
    else:
        idtexto = dameId('obra', obr)
        engine.execute(f"INSERT INTO versos (verso_suelto, obra_idtexto) VALUES ('{string}', '{idtexto}');")

def superinsercion(df,col1,col2,col3,col4,col5,col6):
    """
    col1 = n_interven
    col2 = personaje
    col3 = texto
    col4 = jornada
    col5 = versos
    col6 = n_versos
    """
    for i,r in df.iterrows():
        try:
            insertPersonaje(col2, r[col2])          
            insertJornada(col4, r[col4])
            insertObra(col3, r[col3],r[col1],r[col6],r[col4], r[col2])
            for v in ast.literal_eval(r[col5]):
                insertVersos(col5, v, r[col3])
        except:
            return f"{i},{Exception}"



def insertSeg(seg):
    if check("time ", seg):
        return "el verso existe en ese tiempo"
    else:
        #idtexto = dameId('obra', tex)
        engine.execute(f"INSERT INTO tiempo (tiempo) VALUES ('{seg}');")
        return 'insertado'