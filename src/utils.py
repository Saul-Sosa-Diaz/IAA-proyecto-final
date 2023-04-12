"""
File: utils.py
Author: Saúl Sosa Díaz
Date: 12/04/2023
Description: Implementation of the K-Means algorithm for solving a clustering problem.
This implementation generates random centroids and random assigns points to the cluster of the closest centroid.
Then, the centroids of each cluster are recalculated and the process is repeated until no further changes are made to the clusters.
"""

import pandas as pd
import re
import nltk
from bs4 import BeautifulSoup
from textblob import TextBlob
import spacy
nltk.download('words')
nltk.download('stopwords')

# Contains a list of more than 236,000 English words, from common words to specialized terms.
words = set(nltk.corpus.words.words())
# Contains a list of stopwords in english
stopwords = nltk.corpus.stopwords.words('english')
# Contains the important object to lemmatize
nlp = spacy.load('en_core_web_sm')

def correctSpelling(sentence):
    """
    The function corrects the spelling of a given sentence using the TextBlob library in Python.
    @param sentence - a string containing one or more sentences that may contain spelling errors.
    @returns string - The sentence without spelling mistakes.
    """
    blob = TextBlob(sentence)
    correccion = []
    for words in blob.sentences:
        correccion.append(str(words.correct()))
    return ' '.join(correccion)


def deleteStopWords(sentence):
    """
    Eliminate stopwords from sentences.  
    @param sentence - a string containing one or more sentences that may contain stopwords.
    @returns string The setence without
    """
    return " ".join([palabra for palabra in sentence.split() if palabra not in stopwords])


def deleteHtml(sentence):
    """
    The function takes a sentence containing HTML tags as input and returns the same sentence without
    the HTML tags using the BeautifulSoup library.
    @param sentence - a string that may contain HTML tags and text.
    @returns string - The text content of the input `sentence` after
    removing any HTML tags using the BeautifulSoup library.
    """
    return BeautifulSoup(sentence, 'html.parser').get_text()


def lematizar(sentence):
    """
    The function lematizar takes a sentence as input, uses the spaCy library to tokenize and lemmatize
    the words in the sentence, and returns a string of the lemmatized words.
    @param sentence - a string containing a sentence to be lemmatized.
    @returns a string that contains the lemmatized version of the input sentence.
    """
    doc = nlp(sentence)
    lemas = []
    for token in doc:
        if not token.is_punct and not token.is_stop:
            lemas.append(token.lemma_)
    return ' '.join(lemas)

def writeFile(nameOut="vocabulario.txt"):
    pass


def readFile(nameIn="F75_train.csv"):
    # Read CSV file with pandas
    df = pd.read_csv('F75_train.csv', header=None)
    # Name the columns
    df.columns = ['texto', 'sentimiento']  
    return df

def createVocab(df):
    # Preprocessing
    # Change to lowercase
    df['texto'] = df['texto'].apply(lambda x: x.lower())
    # Remove punctuation marks and numbers
    df['texto'] = df['texto'].apply(lambda x: re.sub('[^^a-zA-Z_\s]', '', x))
    # Delete StopWords
    df['texto'] = df['texto'].apply(lambda x: deleteStopWords(x))
    # Delete HTML tags
    df['texto'] = df['texto'].apply(lambda x: deleteHtml(x))
    # Correct spelling
    df['texto'] = df['texto'].apply(lambda x: correctSpelling(x))
    # Lemantizar
    df['texto'] = df['texto'].apply(lambda x: lematizar(x))
    
    #Create the vocab
    words = ""
    wordSet = set()
    for sentence in df['texto']:
        for palabra in sentence.split():
            wordSet.add(palabra)
    for wordSorted in sorted(list(wordSet)):
        # Check that it exists in the dictionary
        if wordSorted in words:  
            words += wordSorted + "\n"
    return words
