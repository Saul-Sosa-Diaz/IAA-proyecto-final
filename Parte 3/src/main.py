"""
File: main.py
Author: Saúl Sosa Díaz
Date: 26/04/2023
Description: Main program file
"""

import argparse
from colors import bcolors
import os
from createCorpusTrain import *
from createModels import *
from preprocessText import *
from categorizeText import *
from createVocab import *

def main():
    nameTrain = os.path.join(".", "data", "F75_train.csv")
    nameText = os.path.join(".", "data", "F75_trainTest.csv")
    

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", '--vocab', action='store_true', help='Crea el vocabulario de los corpus.')
    parser.add_argument("-c", '--corpus', action='store_true', help= 'Crea los corpus de las noticias.')
    parser.add_argument("-m", '--models', action='store_true',help='Entrena los modelos.')
    parser.add_argument("-t", '--text', action='store_true', help='Preprocesa el texto a clasificar.')
    args = parser.parse_args()
    
    # Crear corpus
    if args.vocab:
        createVocabulary(nameTrain)

    if args.corpus:
        if not os.path.exists(os.path.join(".", "data", "vocabulario.txt")):
            raise Exception(bcolors.FAIL + "No se ha podido encontrar el vocabulario, por favor ejecute el programa con la opción -v" + bcolors.ENDC)
        createCopusOfTrain(nameTrain)
    
    # Crear Modelos
    if args.models:
        folder_path = os.path.join(".", "corpus")
        file_names = ['corpusN.txt',
                      'corpusP.txt',
                      'corpusT.txt']
        files_in_folder = os.listdir(folder_path)
        for file_name in file_names:
            if file_name not in files_in_folder:
                raise Exception(bcolors.FAIL + "No se han podido encontrar los corpus, por favor ejecute el programa con la opción -c" + bcolors.ENDC)
        createModels()
    
    # Preprocear texto
    if args.text:

        folder_path = os.path.join(".", "models")
        file_names = ['modelo_lenguaje_N.txt',
                      'modelo_lenguaje_P.txt',
                      'modelo_lenguaje_T.txt']
        files_in_folder = os.listdir(folder_path)

        for file_name in file_names:
            if file_name not in files_in_folder:
                raise Exception(
                    bcolors.FAIL + "No se han podido encontrar los modelos, por favor ejecute el programa con la opción -m" + bcolors.ENDC)
        folder_path = os.path.join(".", "corpus")

        file_names = ['corpusN.txt',
                      'corpusP.txt',
                      'corpusT.txt']
        
        files_in_folder = os.listdir(folder_path)
        for file_name in file_names:
            if file_name not in files_in_folder:
                raise Exception(bcolors.FAIL + "No se han podido encontrar los corpus, por favor ejecute el programa con la opción -c" + bcolors.ENDC)
        
        preprocessTexts(nameText)
    
    if not os.path.exists(os.path.join(".", "data", "NewsProcessed.txt")):
        raise Exception(bcolors.FAIL + "No se han podido encontrar el fichero test preproceado, por favor ejecute el programa con la opción -t" + bcolors.ENDC)
    
    categorizeText(nameText)




if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(str(err))
