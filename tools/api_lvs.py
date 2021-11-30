from config.configuration import engine
import random
import sql_tool as sqt
import sqlalchemy as alch
import os
password = os.getenv('pass_sql')
dbName="LaVidaEsSueno"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)

def personajes():
    """
    hace una selección los nombres de personajes en la tabla personajes de mysql
    """
    query = list(engine.execute("SELECT distinct(nombre) FROM personaje;"))
    return [q[0] for q in query]


def random_poem(perso):
    """
    hace una seleccion del id de un personaje que se pide
    te devuelve una frase random de ese personaje
    """
    idper = list(engine.execute(f"SELECT idPersonaje FROM personaje WHERE nombre ='{perso}';"))[0][0]
    que = list(engine.execute(f"SELECT texto FROM obra WHERE Personaje_idPersonaje ='{idper}';"))
    return random.choice(que)


def insertusuario(nombre):
    """º
    recibe el nombre de un nuevo usuario 
    inserta el usuario en su tabla correspondiente.
    """
    try:
        if sqt.check("usuario", nombre):
            return "choose another user name, this one is taken"
        else:
            engine.execute(f"INSERT INTO usuario (nombre) VALUES ('{nombre}');")
            return f"your username is {nombre}"
    except:
        return "fallo garrafal"

def insertSeg(seg):
    if check("time ", seg):
        return "el verso existe en ese tiempo"
    else:
        engine.execute(f"INSERT INTO tiempo (tiempo) VALUES ('{seg}');")
        return 'insertado'

def insertSenti(df, ind, seg, col):
    for i,r in df.iterrows():
        engine.execute(f"INSERT INTO senti (ind, seg, col) VALUES ('{ind}', '{seg}', '{col}');")
        return 'insertado'

