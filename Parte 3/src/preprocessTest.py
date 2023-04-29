"""
File: 
Author: Saúl Sosa Díaz
Date: 26/04/2023
Description: 
"""
from utilTests import *
import os

def preprocessTest(nameFile):
    """
    The function creates a preprocessed test file by reading a CSV file, preprocessing the text data,
    and writing the preprocessed data to a text file.
    """
    print("Preproceando Nuevas noticias")
    df = readFileTest(nameFile)
    Test = preprocesarTest(df['texto'])
    writeFile(os.path.join(".", "data", "NewsProcessed.txt"), Test)
    print(bcolors.OKGREEN + "Las noticias se han preprocesado correctamente." + bcolors.ENDC)


if __name__ == "__main__":
    preprocessTest("test")
