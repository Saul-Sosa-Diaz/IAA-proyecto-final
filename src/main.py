import pandas as pd
import time
import re
import nltk
from bs4 import BeautifulSoup
from textblob import TextBlob
import spacy
startTime = time.perf_counter()
nltk.download('words')
nltk.download('stopwords')

words = set(nltk.corpus.words.words())
stopwords = nltk.corpus.stopwords.words('english')
# Corrección ortográfica y lematización
nlp = spacy.load('en_core_web_sm')


def corregirOrtografia(frase):
    blob = TextBlob(frase)
    correccion = []
    for palabras in blob.sentences:
        correccion.append(str(palabras.correct()))
    return ' '.join(correccion)

def eliminarStopWords(frase):   
    # Primero divide la frase en trozos y luego guarda la palabra si esta no es una stopword
    return " ".join([palabra for palabra in frase.split() if palabra not in stopwords])


def eliminarHtml(frase):
    return BeautifulSoup(frase, 'html.parser').get_text()


def corregirOrtografia(texto):
    blob = TextBlob(texto)
    correccion = []
    for frase in blob.sentences:
        for palabra in frase.split():
            correccion.append(str(palabra.correct()))
    return ' '.join(correccion)

def lematizar(frase):
    doc = nlp(frase)
    lemas = []
    for token in doc:
        if not token.is_punct and not token.is_stop:
            lemas.append(token.lemma_)
    return ' '.join(lemas)


# Leer el archivo CSV con pandas
df = pd.read_csv('F75_train.csv', header= None)
df.columns = ['texto', 'sentimiento'] # Ponerle nombres a las columnas
# Pasar a minúsculas
df['texto'] = df['texto'].apply(lambda x : x.lower())
# Eliminar signos de puntuación
# Expresion regular que caza con todo lo que no sea una palabra o espacios en blanco o numeros
df['texto'] = df['texto'].apply(lambda x: re.sub('[^^a-zA-Z_\s]', '', x))
# Eliminar stopWords
df['texto'] = df['texto'].apply(lambda x: eliminarStopWords(x))

df['texto'] = df['texto'].apply(lambda x: eliminarHtml(x))

df['texto'] = df['texto'].apply(lambda x: corregirOrtografia(x))

df['texto'] = df['texto'].apply(lambda x: lematizar(x))

print(df)

NumeroPalabras = 0
palabras = ""
palabraSet = set()
for frase in df['texto']:
    for palabra in frase.split():
        palabraSet.add(palabra)
        
for palabraOrdenada in sorted(list(palabraSet)):
    if palabraOrdenada in words: # Comprobar que exista 
        palabras += palabraOrdenada + "\n"
        NumeroPalabras += 1

nameFile = "vocabulario.txt"

with open(nameFile, 'w') as archivo:
    archivo.write("Numero de palabras:" + str(NumeroPalabras) + "\n")
    archivo.write(palabras)

endTime = time.perf_counter()

print(endTime -startTime)

