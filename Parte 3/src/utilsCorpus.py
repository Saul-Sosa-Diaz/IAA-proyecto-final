"""
File: utilsCorpus.py
Author: Saúl Sosa Díaz
Date: 19/04/2023
Description: This Python file contains functions to process text and create a Corpus from a set of text data.
"""

from tqdm import tqdm
import pandas as pd
import re
import nltk
from bs4 import BeautifulSoup
from textblob import TextBlob
import spacy
from colors import bcolors
nltk.download('words', quiet=True)
nltk.download('stopwords', quiet=True)
# Contains a list of more than 236,000 English words, from common words to specialized terms.
dictionary = set(nltk.corpus.words.words())
# Contains a list of stopwords in english
stopwords = nltk.corpus.stopwords.words('english')
# Contains the important object to lemmatize
nlp = spacy.load('en_core_web_sm')


def correctSpelling(word):
    """
    The function corrects the spelling of a given word using the TextBlob library in Python.
    @param word - a string containing a word that may contain spelling errors.
    @returns string - The corrected version of the input word.
    """
    if word in dictionary:
        return word
    else:
        corrected_word = TextBlob(word).correct()
        return str(corrected_word)


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



def lemmatize(word):
    """
    The lemmatize function takes a word as input, lemmatizes it using the spaCy library,
    and returns the lemmatized form of the input word.
    @param word - a string containing the word to be lemmatized.
    @returns a string containing the lemmatized form of the input word.
    """
    doc = nlp(word)
    lemma = ''
    for token in doc:
        if not token.is_punct and not token.is_stop:
            lemma = token.lemma_
    return lemma



def writeFile(content, nameOut):
    """
    The function `writeFile` writes the given content to a file with the given name.
    @param content - The content that will be written to the file.
    @param nameOut - The name of the file that will be created or overwritten with the content provided
    in the 'content' parameter.
    """
    with open(nameOut, 'w') as file:
        file.write(content)



def readFileTrain(nameIn="F75_train.csv"):
    """
    This function reads a CSV file with pandas, names the columns, and returns a dataframe.
    @param [nameIn=F75_train.csv] - The name of the CSV file to be read. If no name is provided, the
    default file name "F75_train.csv" will be used.
    @returns The function `readFile` returns a pandas DataFrame object containing the data read from a
    CSV file with two columns named 'texto' and 'sentimiento'.
    """
    # Read CSV file with pandas
    df = pd.read_csv(nameIn, header=None)
    # Name the columns
    df.columns = ['texto', 'sentimiento']  
    return df



def processCorpus(df):
    """
    The function preprocesses a corpus by removing punctuation marks, numbers, HTML tags, and stop
    words, corrects spelling, lemmatizes words, and returns a sorted final corpus.
    @param df - The input dataframe containing the text data to be processed.
    @returns a string that contains the final corpus of words after preprocessing, correction of
    spelling, lemmatization, and filtering out words that are not in the dictionary.
    """
    # Preprocessing
    # Remove punctuation marks and numbers
    df = df.apply(lambda x: re.sub('[^^a-zA-Z_\s]', '', x))
    # Delete StopWords
    df = df.apply(lambda x: deleteStopWords(x))
    # Delete HTML tags
    df = df.apply(lambda x: deleteHtml(x))

    words = list()
    for sentence in df:
        for word in sentence.split():
            words.append(word)
    
    finalCorpus = []
    print(bcolors.OKCYAN + "\tCorrigiendo y lematizando palabras." + bcolors.ENDC)
    for i in tqdm(range(len(words)), bar_format='{l_bar}{bar:30}{r_bar}', leave=True):
        # Change word to lowercase
        words[i] = words[i].lower()
        # Correct spelling
        words[i] = correctSpelling(words[i])
        # Lemmatize
        words[i] = lemmatize(words[i])
        if words[i] in dictionary:
            finalCorpus.append(words[i])
    
    finalCorpus.sort()
    return '\n'.join(finalCorpus)




def createAllCorpusTrain(df):
    """
    This function creates three different corpora based on the sentiment of the news articles in a given
    dataframe and returns them.
    @param df - The input dataframe containing the news articles and their corresponding sentiment
    labels.
    @returns :string - three variables: negativeCorpus, neutralCorpus, and positiveCorpus.
    """
    neutralCorpus = df[df['sentimiento'] == "neutral"]['texto']
    positiveCorpus = df[df['sentimiento'] == "positive"]['texto']
    negativeCorpus = df[df['sentimiento'] == "negative"]['texto']
    
    # Número de noticias de cada corpus
    stringNegativeCorpus = "Numero de noticias del corpus: " + \
        str(negativeCorpus.shape[0]) + "\n"
    stringNeutral = "Numero de noticias del corpus: " + \
        str(neutralCorpus.shape[0]) + "\n"
    stringPositiveCorpus = "Numero de noticias del corpus: " + \
        str(positiveCorpus.shape[0]) + "\n"
    
    print(bcolors.OKCYAN + "Creando corpus negativo" + bcolors.ENDC)
    stringNegativeCorpus += processCorpus(negativeCorpus)
    print(bcolors.OKCYAN + "Creando corpus neutro" + bcolors.ENDC)
    stringNeutral += processCorpus(neutralCorpus)
    print(bcolors.OKCYAN + "Creando corpus positivo" + bcolors.ENDC)
    stringPositiveCorpus += processCorpus(positiveCorpus)

    print(bcolors.OKGREEN + "Se han creado los corpus correctamente." + bcolors.ENDC)
    return stringNegativeCorpus, stringNeutral, stringPositiveCorpus


