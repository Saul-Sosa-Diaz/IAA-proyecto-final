"""
File: utils.py
Author: Saúl Sosa Díaz
Date: 19/04/2023
Description: This file is a Python script that uses the utils module to read a data file, create corpus from the data, and write the vocabulary to a new file. 
             The script has a main function called main() that orchestrates all the necessary operations.
"""

from utilTests import *
from utilsModels import *
from colors import bcolors
import pandas as pd
import os


def categorizeText(nameNews):

  modelo_N = readFile(os.path.join(".", "models", "modelo_lenguaje_N.txt"))
  modelo_P = readFile(os.path.join(".", "models", "modelo_lenguaje_P.txt"))
  modelo_T = readFile(os.path.join(".", "models", "modelo_lenguaje_T.txt"))

  test = readFile(os.path.join(".", "data", "NewsProcessed.txt"))

  Probs_N = getProb(modelo_N, test)
  Probs_P = getProb(modelo_P, test)
  Probs_T = getProb(modelo_T, test)

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


  """
  comprobar = []
  for i in range(0, len(Probs_N)):
    if Probs_N[i] > Probs_P[i] and Probs_N[i] > Probs_T[i]:
      stringToAbstract.append("negative")
    elif Probs_P[i] > Probs_N[i] and Probs_P[i] > Probs_T[i]:
      stringToAbstract.append("positive")
    else:
      stringToAbstract.append("neutral")
 
  # Read CSV file with pandas
  df = pd.read_csv(os.path.join(".", "data", "F75_train.csv"), header=None)
  # Name the columns
  df.columns = ['texto', 'sentimiento']
  correctas = df['sentimiento']
  correcta = 0

  for i in range(0, len(correctas)):
    if correctas[i] == comprobar[i]:
      correcta += 1
  porcentaje = (correcta / len(correctas)) * 100

  print("Procentaje de acierto: " + str(porcentaje) + " %")
  """


if __name__ == "__main__":
    categorizeText()
