"""
File: utils.py
Author: Saúl Sosa Díaz
Date: 19/04/2023
Description: This file is a Python script that uses the utils module to read a data file, create corpus from the data, and write the vocabulary to a new file. 
             The script has a main function called main() that orchestrates all the necessary operations.
"""
from utilsVocab import *
from colors import bcolors
import os


def createVocabulary():
    df = readFile()
    vocabulary = createVocab(df)
    writeFile(vocabulary)


if __name__ == "__main__":
    createVocabulary()
