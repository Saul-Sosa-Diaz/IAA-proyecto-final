import pandas as pd
import re
from utilsCorpus import *


def readFileTest(nameIn="F75_train.csv"):
    """
    This function reads a CSV file with pandas, names the columns, and returns a dataframe.
    @param [nameIn=F75_train.csv] - The name of the CSV file to be read. If no name is provided, the
    default file name "F75_train.csv" will be used.
    @returns The function `readFile` returns a pandas DataFrame object containing the data read from a
    CSV file with two columns named 'texto' and 'sentimiento'.
    """
    # Read CSV file with pandas
    df = pd.read_csv(nameIn, header=None)
    # Name the columns
    df.columns = ['texto']
    return df


def preprocesarTest(df):
    df = df.apply(lambda x: re.sub('[^^a-zA-Z_\s]', '', x))
    # Delete StopWords
    df = df.apply(lambda x: deleteStopWords(x))
    # Delete HTML tags
    df = df.apply(lambda x: deleteHtml(x))
    print(bcolors.OKCYAN + "\tPreprocesando noticias." + bcolors.ENDC)
    for i in tqdm(range(len(df)), bar_format='{l_bar}{bar:30}{r_bar}', leave=True):
        words = df[i].split()
        newWords = []
        for j in range(0, len(words)):
            # Change word to lowercase
            aux = words[j].lower()
            # Correct spelling
            aux = correctSpelling(aux)
            # Lemmatize
            aux = lemmatize(aux)
            if aux in dictionary:
                newWords.append(aux)
        df[i] = " ".join(newWords)

    sentences = ""
    for sentence in df:
        sentences += str(sentence) + "\n"

    print(bcolors.OKGREEN +
          "Se preproceasdo el fichero de test correctamente." + bcolors.ENDC)
    return sentences


def writeFile(nameOut, contain):
    with open(nameOut, 'w') as file:
        file.write(contain)

