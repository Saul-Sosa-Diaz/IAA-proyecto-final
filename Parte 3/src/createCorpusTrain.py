"""
File: 
Author: Saúl Sosa Díaz
Date: 26/04/2023
Description: This file is a Python script that uses the utils module to read a data file, create corpus from the data, and write the vocabulary to a new file. 
             The script has a main function called main() that orchestrates all the necessary operations.
"""
from utilsCorpus import *
import os

def createCopusOfTrain(nameOfTrainFile):
    print("Creando los corpus")
    df = readFileTrain(nameOfTrainFile)
    negativeCorpus, neutralCorpus, positiveCorpus = createAllCorpusTrain(df)
    writeFile(negativeCorpus, os.path.join(".", "corpus", "negative_corpus.txt"))
    writeFile(neutralCorpus, os.path.join(".", "corpus", "neutral_corpus.txt"))
    writeFile(positiveCorpus, os.path.join(".", "corpus", "positive_corpus.txt"))
    print(bcolors.OKGREEN + "Creados corpus correctamente" + bcolors.ENDC)

if __name__ == "__main__":
    createCopusOfTrain()

