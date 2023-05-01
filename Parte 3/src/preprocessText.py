"""
File: preprocessText.py
Author: Saúl Sosa Díaz
Date: 26/04/2023
Description: The "preprocessText" function reads a CSV file containing text data, processes it, and writes the processed data to a text file named "NewsProcessed.txt" in a folder named "data" in the current directory.
into a text file named "NewsProcessed.txt" in a folder named "data" in the current directory.
"""

from utilTexts import *
import os

def preprocessTexts(nameFile):
    """
    The function creates a preprocessed test file by reading a CSV file, preprocessing the text data,
    and writing the preprocessed data to a text file.
    """
    print("Preproceando Nuevas noticias")
    df = readFileTest(nameFile)
    Test = preprocessText(df['texto'])
    writeFile(os.path.join(".", "data", "NewsProcessed.txt"), Test)
    print(bcolors.OKGREEN + "Las noticias se han preprocesado correctamente." + bcolors.ENDC)


if __name__ == "__main__":
    preprocessText("test")
