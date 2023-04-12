

def main():


nameFile = "vocabulario.txt"

with open(nameFile, 'w') as archivo:
    archivo.write("Numero de palabras:" + str(Numerowords) + "\n")
    archivo.write(words)

endTime = time.perf_counter()

print(endTime -startTime)

