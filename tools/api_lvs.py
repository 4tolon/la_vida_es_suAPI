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

def random_season(season):
    """
    recibe un numero de temporada de friends (Entre el 1 y el 10)
    devuelve una frase random de esa temporada indicando qué personaje la dice y el título del episodio.
    """
    try:
        idepisodes = list(engine.execute(f"SELECT idEpisodio FROM episodios where idTemporadas = {season};"))
        idep = random.choice(idepisodes)[0]
        epi = list(engine.execute(f"SELECT tituloEp FROM episodios where idEpisodio = {idep};"))[0][0]
        que = list(engine.execute(f"SELECT texto, idcharacters FROM quotes WHERE idEpisodio ={idep};"))
        line_ch = random.choice(que)
        char = list(engine.execute(f"SELECT nombre FROM characters WHERE idcharacters = {line_ch[1]};"))[0][0]
        line = line_ch[0]
        
        return f"in episdode '{epi}', from season {season} {char} says '{line}'"
    except:
        return "Friends tiene 10 temporadas, elige un número del 1 al 10"
    
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


def newline(temp, epi, charac, line):
    """
    recibe temporada, episodio, nombre de presonaje y frase qué ha dicho
    la inserta en las tablas de mysql.
    """
    try:
        sqt.insertTemp("season",temp)
        sqt.insertCar("character",charac)
        sqt.insertEp("episode_title",epi)
        sqt.insertquote("quote",line,epi,charac)
        return "inserted"
    except:
        return "fallo garrafal"