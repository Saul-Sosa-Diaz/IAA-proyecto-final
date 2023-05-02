"""
File: utils.py
Author: Saúl Sosa Díaz
Date: 19/04/2023
Description: This file is a Python script that uses the utils module to read a data file, create corpus from the data, and write the vocabulary to a new file. 
             The script has a main function called main() that orchestrates all the necessary operations.
"""

from utilTexts import *
from utilsModels import *
from colors import bcolors
import pandas as pd
import os


def categorizeText(nameNews):
  """
  This function categorizes news articles into one of three categories (N, P, or T) based on their content. It does this by reading in three pre-trained language models, and using them to calculate the probability of each article belonging to each category. It then writes the results to two separate CSV files: one containing the category for each article, and one containing only the categories. 
  @param nameNews - the name of the file containing the news articles to be categorized.
  """

  modelo_N = readFile(os.path.join(".", "models", "modelo_lenguaje_N.txt"))
  modelo_P = readFile(os.path.join(".", "models", "modelo_lenguaje_P.txt"))
  modelo_T = readFile(os.path.join(".", "models", "modelo_lenguaje_T.txt"))

  totalNumberOfNews = int(modelo_N.split('\n')[0].split(":")[1]) + int(modelo_P.split('\n')[0].split(":")[1]) + int(modelo_T.split('\n')[0].split(":")[1])

  text = readFile(os.path.join(".", "data", "NewsProcessed.txt"))

  Probs_N = getProb(modelo_N, text, totalNumberOfNews)
  Probs_P = getProb(modelo_P, text, totalNumberOfNews)
  Probs_T = getProb(modelo_T, text, totalNumberOfNews)

  stringToAbstract = ""
  stringToClasificator = ""
  NewsWithoutPreprosessing = pd.read_csv(nameNews, header = None)

  for i in range(0, len(Probs_N)):
    
    enter =  "\n"
    if i == len(Probs_N) - 1:
      enter = ""

    first10Characters = str(NewsWithoutPreprosessing.iloc[i, 0])[:10]
    stringToClasificator += first10Characters + "," + str(Probs_P[i]) + "," + str(Probs_N[i]) + "," + str(Probs_T[i]) + ","

    if Probs_N[i] > Probs_P[i] and Probs_N[i] > Probs_T[i]:
      stringToAbstract += "N" + enter
      stringToClasificator += "N" + enter
    elif Probs_P[i] > Probs_N[i] and Probs_P[i] > Probs_T[i]:
      stringToAbstract += "P" + enter
      stringToClasificator += "P" + enter
    else:
      stringToAbstract += "T" + enter
      stringToClasificator += "T" + enter
  
  writeFile(os.path.join(".", "solutions", "clasificacion_alu0101404141.csv"), stringToClasificator)
  writeFile(os.path.join(".", "solutions", "resumen_alu0101404141.csv"), stringToAbstract)
  print(bcolors.OKGREEN + "Se han categorizado las noticias correctamente y se han guardado los resultados en el directorio solutions." + bcolors.ENDC)




if __name__ == "__main__":
    categorizeText()
