import argparse
from colors import bcolors
import os
from createCorpusTrain import *
from createModels import *
from preprocessTest import *
from categorizeText import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", '--corpus', action='store_true',
                        help= 'Crea los corpus de las noticias.')
    parser.add_argument("-m", '--models', action='store_true',
                        help='Entrena los modelos.')
    parser.add_argument("-t", '--text', action='store_true',
                        help='Preprocesa el texto de prueba.')
    
    args = parser.parse_args()
    # Crear corpus
    if args.c:
        createCopusOfTrain("F75_train.csv")
    
    # Crear Modelos
    if args.m:
        folder_path = os.path.join(".", "corpus")
        file_names = ['negative_corpus.txt',
                      'neutral_corpus.txt', 
                      'positive_corpus.txt']
        files_in_folder = os.listdir(folder_path)
        
        for file_name in file_names:
            if file_name not in files_in_folder:
                raise bcolors.FAIL + "No se han podido encontrar los corpus, por favor ejecute el programa con la opción -c" + bcolors.ENDC
        
        createModels()
    
    # Preprocear texto
    if args.t:
        folder_path = os.path.join(".", "corpus")
        file_names = ['negative_corpus.txt',
                      'neutral_corpus.txt',
                      'positive_corpus.txt']
        files_in_folder = os.listdir(folder_path)

        for file_name in file_names:
            if file_name not in files_in_folder:
                raise bcolors.FAIL + "No se han podido encontrar los corpus, por favor ejecute el programa con la opción -c" + bcolors.ENDC
        
        folder_path = os.path.join(".", "models")
        file_names = ['modelo_lenguaje_N.txt',
                      'modelo_lenguaje_P.txt',
                      'modelo_lenguaje_T.txt']
        
        files_in_folder = os.listdir(folder_path)

        for file_name in file_names:
            if file_name not in files_in_folder:
                raise bcolors.FAIL + "No se han podido encontrar los modelos, por favor ejecute el programa con la opción -m" + bcolors.ENDC

        preprocessTest("F75_trainTest.csv")
    
    categorizeText("F75_trainTest.csv")


if __name__ == "__main__":
    main()
