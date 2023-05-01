"""
File: aciertos.py
Author: Saúl Sosa Díaz
Date: 26/04/2023
Description: this file contains the function to check the word processor's success rate
"""
import pandas as pd
import os

def main():
  '''
  This function reads a CSV file, compares the sentiment values with a solution file, and calculates
  the percentage of correct predictions.
  '''

  df = pd.read_csv(os.path.join(".", "data", "F75_train.csv"), header=None)
  # Name the columns
  df.columns = ['texto', 'sentimiento']
  correctas = list(df['sentimiento'])
  correcta = 0
  contenido = ""
  with open(os.path.join(".", "solutions", "resumen_alu0101404141.csv"), 'r') as file:
    contenido = file.read()
  comprobar = []
  contenidos = contenido.split('\n')
  for i in range(0, len(contenidos)):
    if contenidos[i] == "N":
      comprobar.append("negative")
    elif contenidos[i] == "P":
      comprobar.append("positive")
    else:
      comprobar.append("neutral")

  for i in range(0, len(correctas)):
    if correctas[i] == comprobar[i]:
      correcta += 1

  porcentaje = (correcta / len(correctas)) * 100

  print("Procentaje de acierto: " + str(porcentaje) + " %")


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(str(err))
