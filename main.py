from flask import Flask, request
from flask import jsonify
import tools.api_lvs as tsa
import tools.sql_tool as sq
import os
import sys
import random
import sqlalchemy as alch
password = os.getenv('pass_sql')
dbName="LaVidaEsSueno"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)

app = Flask(__name__)
a="""<div class="cnt-banner-main">
<h1 class="cnt-banner-title">
Personalización
</h1>
<div class="cnt-banner-box">
<p class="cnt-banner-row">
<a href="https://www.intimissimi.com/es/mujer/special/personaliza_tu_sujetador/" class="cnt-banner-cta">
Sujetadores
</a>
<a href="https://www.intimissimi.com/es/mujer/special/personaliza_tu_braga/" class="cnt-banner-cta">
Braguitas
</a>
<a href="https://www.intimissimi.com/es/mujer/special/personaliza_tu_lingerie/" class="cnt-banner-cta">
Lencería
</a>
</p>
<p class="cnt-banner-row">
<a href="https://www.intimissimi.com/es/mujer/special/personaliza_tu_ropa/" class="cnt-banner-cta">
Ropa
</a>
<a href="https://www.intimissimi.com/es/mujer/special/personaliza_tu_pijama/" class="cnt-banner-cta">
Noche
</a>
</p>
</div>
</div>"""




bb= "<img src='portada.jpg...................' />"

cc="""<img src="portada.jpg"/>"""



@app.route("/")
def inicial():
    return "La vida es Sueño, Pedro Calderón de la Barca"

@app.route("/personajes")
def per():
    return f"Estos son todos los personajes: {', '.join(tsa.personajes())} "

def funSel(random):
    if (random <= 0.40):
        return "C0C0C0"
    elif (random<=0.70):
        return "D8BFD8"
    elif(random<=0.90):
        return "8FBC8B"
    else:
        return "4FF69B4"

@app.route("/poem/<name>")
def frasename(name):
    colore = f'<body style="background-color:#{funSel(random.random())};"></body>'
    youtube = f'<iframe width="560" height="315" src="https://www.youtube.com/embed/O9y6iAOqUN0?controls=0&amp;start={random.randint(540,4200)}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    frase = f"{colore}{name} dice:<br> {youtube}<br> {tsa.random_poem(name)[0]}<p align='center'>https://github.com/4tolon</p><img src='https://hiretail.es/wp-content/uploads/2015/08/ab0a900574424ad987929b81b9c55241.jpg' alt='' />{a}" 
    return frase

@app.route("/time", methods=["POST"])
def timerrr():
    seg = request.form.get("segundos")
    return sq.insertSeg(seg)

@app.route("/senti", methods=["POST"])
def sentis():
    ind = request.form.get("ind")
    seg = request.form.get("seg")
    col = request.form.get("col")
    return sq.insertSenti(ind, seg, col)


if __name__ == "__main__":
    app.run(debug=True)