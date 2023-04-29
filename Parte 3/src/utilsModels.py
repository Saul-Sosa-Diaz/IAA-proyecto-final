"""
File: utils.py
Author: Saúl Sosa Díaz
Date: 19/04/2023
Description: This file contains several functions for natural language processing. 
"""

import math

def readCorpus(nameIn):
    '''This function reads a corpus from a file and returns a list of words and the number of news articles
    in the corpus.
    
    Parameters
    ----------
    nameIn
        The name of the file that contains the corpus to be read.
    
    Returns
    -------
        The function `readCorpus` returns a tuple containing two values: a list of words and an integer
    representing the number of news in the corpus.
    
    '''
    with open(nameIn, "r") as fileContent:
        NumberOfNews = int(fileContent.readline().split(":")[1])
        words = []
        for line in fileContent.readlines():
            words.append(line.strip())
        return words, NumberOfNews


def readVocab(nameIn):
    '''This function reads a file containing a list of words and returns a list of those words.
    
    Parameters
    ----------
    nameIn
        The name of the file that contains the vocabulary words to be read.
    
    Returns
    -------
        The function `readVocab` returning a list of words read from a file specified by the input
    parameter `nameIn`.
    '''
    with open(nameIn, "r") as fileContent:
        words = []
        for line in fileContent.readlines()[1:]:
            words.append(line.strip())
        return words


def createModel(corpus, vocabulary):
    '''This function creates a language model by calculating the log probability of each word in a given
    corpus based on its frequency and the size of the vocabulary.
    
    Parameters
    ----------
    corpus
        The corpus is a list of words that the model will be trained on. It is the set of all words that
    the model will use to calculate probabilities.
    vocabulary
        a list of all the unique words in the corpus
    
    Returns
    -------
        The function `createModel` returns a dictionary `probs` containing the frequency and log
    probability of each word in the vocabulary, calculated based on its occurrence in the given corpus.
    
    '''
    probs = {}
    WORDSINCORPUS = len(corpus)
    WORDSINVOCAB = len(vocabulary)

    for word in vocabulary:
        frec = corpus.count(word)
        logProb = math.log((frec + 1)/(WORDSINCORPUS + WORDSINVOCAB))
        probs[word] = [frec, logProb]

    return probs


def writeFileModel(nameOut, numberOfNews, numberOfWordsInCorpus, probs: dict):
    '''This function writes information about a language model to a file, including the number of news
    in the class, the number of words in the corpus, and the frequency and log probability of each word
    in the model.
    
    Parameters
    ----------
    nameOut
        The name of the output file where the model will be written.
    numberOfNews
        The number of documents (news) in the corpus.
    numberOfWordsInCorpus
        The total number of words in the corpus, which is the collection of all the documents or news
    articles.
    probs : dict
        A dictionary containing the probabilities and frequencies of each word in a corpus. The keys are
    the words and the values are tuples containing the frequency and log probability of the word.
    
    '''
    with open(nameOut, 'w') as file:
        stringToFile = "Numero de documentos (noticias) del corpus :" + \
            str(numberOfNews) + "\n"
        stringToFile += "Numero de palabras del corpus:" + \
            str(numberOfWordsInCorpus) + "\n"
        for word, prob in probs.items():
            stringToFile += "Palabra:" + word + " Frec:" + \
                str(prob[0]) + " LogProb:" + str(prob[1]) + "\n"

        stringToFile = stringToFile[:-1]
        file.write(stringToFile)


def readFile(nameIn):
    with open(nameIn, "r") as fileContent:
        return fileContent.read()



def getProb(model, news):
    model = model.split('\n')
    numberOfNewsThisType = int(model[0].split(":")[1])
    probs = []
    
    words = {}
    for j in range(2, len(model)):
        words[model[j].split(" ")[0].split(":")[1]] = float(model[j].split(":")[-1])
    
    for sentence in news.split('\n')[:-1]:
        prob = 0
        for word in sentence.split(" "):
            try:
                prob += words[word] 
            except:
                prob += words["<unk>"]
        prob += math.log(numberOfNewsThisType/2500)
        probs.append(prob)

    return probs
