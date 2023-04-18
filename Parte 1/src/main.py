"""
File: utils.py
Author: Saúl Sosa Díaz
Date: 12/04/2023
Description: This file is a Python script that uses the utils module to read a data file, create a vocabulary from the data, and write the vocabulary to a new file. 
             The script has a main function called main() that orchestrates all the necessary operations.
"""
from utils import *

def main():
    df = readFile()
    vocabulary = createVocab(df)
    writeFile(vocabulary)


if __name__ == "__main__":
    main()

