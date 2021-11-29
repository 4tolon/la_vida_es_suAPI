from flask import Flask, request
from flask import jsonify
import tools.api_lvs as tsa
import tools.sql_tool as sq
import os
import sqlalchemy as alch
password = os.getenv('pass_sql')
dbName="LaVidaEsSueno"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)

app = Flask(__name__)

@app.route("/")
def inicial():
    return "La vida es Sueño, Pedro Calderón de la Barca"

@app.route("/personajes")
def per():
    return f"Estos son todos los personajes: {', '.join(tsa.personajes())} "

@app.route("/time")
def time():
    return f"Estos son todos los personajes: {', '.join(tsa.personajes())} "

@app.route("/poem/<name>")
def frasename(name):
    colore = '<body style="background-color:#8DDBE9;"></body>'
    youtube = '<iframe width="560" height="315" src="https://www.youtube.com/embed/O9y6iAOqUN0?controls=0&amp;start=518" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    frase = f"{colore}{name} dice:<br> {youtube}<br> {tsa.random_poem(name)[0]}" 
    return frase

@app.route("/time", methods=["POST"])
def timerrr():
    seg = request.form.get("segundos")
    return sq.insertSeg(seg)


if __name__ == "__main__":
    app.run(debug=True)