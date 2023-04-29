"""
File: utils.py
Author: Saúl Sosa Díaz
Date: 12/04/2023
Description: This Python file contains functions to process text and create a vocabulary from a set of text data.
Defined functions:
  * correctSpelling: takes a sentence as input and corrects the spelling using the TextBlob library, and returns the sentence without spelling errors.
  * deleteStopWords: removes stop words from a sentence, which are passed as input, and returns the sentence without these words.
  * deleteHtml: removes HTML tags from a sentence and returns only the text.
  * lematize: uses the spacy library to tokenize and lemmatize the words of a sentence and returns the lemmatized version of the sentence.
  * writeFile: writes the provided content to a file, along with the number of lines of content.
  * readFile: reads a CSV file using pandas and returns a DataFrame object containing the data read from the CSV file. The column names are set to 'text' and 'sentiment'.
  * createVocab: processes the text data in the input DataFrame, removes stop words, HTML tags and performs lemmatization. 
                 It then creates a vocabulary of all unique words in the DataFrame that exist in the loaded dictionary and returns a string containing these words separated by line breaks.
"""

from tqdm import tqdm
import pandas as pd
import time
import re
import nltk
from bs4 import BeautifulSoup
from textblob import TextBlob
import spacy
from colors import bcolors
nltk.download('words')
nltk.download('stopwords')
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


def writeFile(content, nameOut="vocabulario.txt"):
    """
    The function writes the given content to a file named "vocabulario.txt" and also writes the number
    of lines in the content to the file.
    @param content - The content that will be written to the file.
    @param [nameOut=vocabulario.txt] - The name of the output file that will be created. If no name is
    provided, the default name "vocabulario.txt" will be used.
    """
    with open(nameOut, 'w') as file:
        file.write("Numero de palabras:" + str(content.count('\n')) + "\n")
        file.write(content)


def readFile(nameIn="F75_train.csv"):
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


def createVocab(df):
    """
    The function creates a vocabulary by preprocessing text data and extracting unique words from it,
    while also checking if they exist in a given dictionary.
    @param df - a pandas DataFrame containing a column named 'texto' which contains text data to be
    processed and used to create a vocabulary.
    @returns a string containing all the words in the input dataframe that exist in a pre-defined
    dictionary. The words are sorted alphabetically and separated by a newline character.
    """
    # Preprocessing
    # Remove punctuation marks and numbers
    df['texto'] = df['texto'].apply(lambda x: re.sub('[^^a-zA-Z_\s]', '', x))
    # Delete StopWords
    df['texto'] = df['texto'].apply(lambda x: deleteStopWords(x))
    # Delete HTML tags
    df['texto'] = df['texto'].apply(lambda x: deleteHtml(x))

    words = set()
    for sentence in df['texto']:
        for word in sentence.split():
            words.add(word)

    words = list(words)

    print(bcolors.OKCYAN + "Corrigiendo Y lematizando palabras." + bcolors.ENDC)
    for i in tqdm(range(len(words)), bar_format='{l_bar}{bar:30}{r_bar}', leave=True):
        # Change word to lowercase
        words[i] = words[i].lower()
        # Correct spelling
        words[i] = correctSpelling(words[i])
        # Lemmatize
        words[i] = lemmatize(words[i])

    words = set(words)
    print(bcolors.OKCYAN + "Filtrando palabras" + bcolors.ENDC)
    # Create the vocab
    wordsString = ""
    for wordSorted in sorted(list(words)):
        # Check that it exists in the dictionary
        if wordSorted in dictionary:
            wordsString += wordSorted + "\n"
    wordsString += "<unk> \n"
    print(bcolors.OKGREEN + "Se ha creado el vocabulario correctamente." + bcolors.ENDC)
    return wordsString
