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
    Test = preprocesarTest(df['texto'])
    writeFile(Test, os.path.join(".", "data", "PreprocesadoTest.txt"))


if __name__ == "__main__":
    main()
