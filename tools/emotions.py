import string
import spacy
spacy.load('es_core_news_md')
spacy.load('en_core_web_sm')
import es_core_news_md
import en_core_web_sm
import nltk
from nltk.corpus import stopwords
import re
from textblob import TextBlob
nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer





























def tokenizando(texto):
    """º
    - para usar con dataframe
    recibe un string y lo tokeniza:
    quita palabras que no sirven para el análisis de sentimientos
    quita y reemplaza los sufijos de las palabras para dejarlas en la raíz
    devuelve un string con la morfología básica de las palabras
        
    """
    
    nlp = spacy.load("en_core_web_sm")
    stop = nlp.Defaults.stop_words
    tokens = nlp(texto)
    filtro = []
    for t in tokens:
        if not t.is_stop:
            lemma = t.lemma_.lower().strip()
            if re.search('^[a-zA-Z]+$',lemma):
                filtro.append(lemma)
    return " ".join(filtro)


def sentimental(col):
    """
    - para usar con dataframe
    recibe un string tokenizado
    devuelve una lista con su subjetividad, su polaridad según textblog
    también en la lista están incluidos los parámetros de sia(neg,neu,pos y compound)
    """
    

    total = []
    
    blob = TextBlob(col)
    total.append(blob.sentiment[0])
    total.append(blob.sentiment[1])
    
    sia = SentimentIntensityAnalyzer()
    polaridad = sia.polarity_scores(col)
    total.append(polaridad["neg"])
    total.append(polaridad["neu"])
    total.append(polaridad["pos"])
    total.append(polaridad["compound"])
    return total


def sentimientos_fr(frase):
    sia = SentimentIntensityAnalyzer()
    toking = tokenizando(frase)
    analisis = sia.polarity_scores(toking)
    
    # neg = analisis["neg"]
    # neu = analisis["neu"]
    # pos = analisis["pos"]
    # comp = analisis["compound"]
    return analisis #[neg,neu,pos,comp]