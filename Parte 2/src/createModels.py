"""
File: utils.py
Author: Saúl Sosa Díaz
Date: 19/04/2023
Description: This file is a Python script that uses the utils module to read a data file, create corpus from the data, and write the vocabulary to a new file. 
             The script has a main function called main() that orchestrates all the necessary operations.
"""
from utilsModels import *
from colors import bcolors
import os


def main():
    negativeCorpus, numbersNegativeNews = readCorpus(
        os.path.join(".", "corpus", "negative_corpus.txt"))
    positiveCorpus, numbersPositiveNews = readCorpus(
        os.path.join(".", "corpus", "neutral_corpus.txt"))
    neutralCorpus, numbersNeutralNews = readCorpus(
        os.path.join(".", "corpus", "positive_corpus.txt"))
    
    vocabulary = readVocab(os.path.join(".", "data", "vocabulario.txt"))

    negativeModel = createModel(negativeCorpus, vocabulary)
    positiveModel = createModel(positiveCorpus, vocabulary)
    neutralModel = createModel(neutralCorpus, vocabulary)

    writeFileModel(os.path.join(".", "models", "modelo_lenguaje_N.txt"),
                   numbersNegativeNews, len(negativeCorpus), negativeModel)
    print(bcolors.OKGREEN +
          "Se han creado el modelo negativo correctamente" + bcolors.ENDC)
    
    writeFileModel(os.path.join(".", "models", "modelo_lenguaje_P.txt"),
                   numbersPositiveNews, len(positiveCorpus), positiveModel)
    print(bcolors.OKGREEN +
          "Se han creado el modelo positivo correctamente" + bcolors.ENDC)
    
    writeFileModel(os.path.join(".", "models", "modelo_lenguaje_T.txt"),
                   numbersNeutralNews, len(neutralCorpus), neutralModel)
    print(bcolors.OKGREEN +
          "Se han creado el modelo neutro correctamente" + bcolors.ENDC)



if __name__ == "__main__":
    main()
