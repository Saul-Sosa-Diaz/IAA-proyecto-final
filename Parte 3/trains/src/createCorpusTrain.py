"""
File: 
Author: Saúl Sosa Díaz
Date: 26/04/2023
Description: This file is a Python script that uses the utils module to read a data file, create corpus from the data, and write the vocabulary to a new file. 
             The script has a main function called main() that orchestrates all the necessary operations.
"""
from utilsCorpus import *
import os

def main():
    df = readFileTrain(os.path.join(".", "data", "F75_train1.csv"))
    negativeCorpus, neutralCorpus, positiveCorpus = createAllCorpusTrain(df)
    writeFile(negativeCorpus, os.path.join(".", "corpus", "negative_corpus.txt"))
    writeFile(neutralCorpus, os.path.join(".", "corpus", "neutral_corpus.txt"))
    writeFile(positiveCorpus, os.path.join(".", "corpus", "positive_corpus.txt"))


if __name__ == "__main__":
    main()

