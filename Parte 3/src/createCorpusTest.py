"""
File: 
Author: Saúl Sosa Díaz
Date: 26/04/2023
Description: 
"""
from utilsCorpus import *
import os

def main():
    df = readFileTest(os.path.join(".", "data", "F75_train2.csv"))
    corpusTest = createCorpusTest(df)
    writeFile(corpusTest, os.path.join(".", "corpus", "corpus_test.txt"))


if __name__ == "__main__":
    main()
