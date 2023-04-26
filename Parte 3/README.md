# IAA - Segunda parte proyecto: 
* author: Saúl Sosa Díaz
* email: _alu0101404141@ull.edu.es_

## Resumen
El objetivo es generar 3 modelos a partir F75_train.csv que contiene noticias, los tres modelos corresponden a los tres tipos de noticias que hay, Positivas, Neutras y negativas.

## Ejecución
Para poder ejecutar el programa y crear los modelos debemos tener los corpus necesarios en la carpeta corpus.  
En caso de no tenerlos, los podemos generar con el siguiente comando:
```BASH
python3 ./src/preprocessCorpus.py
```
Una vez hecho esto ya tendemos los corpus generados, ahora deberemos de crear los modelos, para ello utilizamos el siguiente comando:
```BASH
python3 ./src/createModels.py
```
Ahora tendremos una carpeta modelos con los tres modelos generados.

## Estructura de directorios
```
  .
  ├── src # Contiene el código fuente del programa.
  ├─── data # Contiene información necesaria para crear los corpus y los modelos.
  ├─── corpus # Contiene los corpus necesarios para la creación de los modelos.     
  └── models # Contiene los modelos generados por el programa.  
```


## Dependencias:
Para ejecutar este programa son necesarias las siguientes librerías:
* [Pandas](https://pandas.pydata.org/): Se utiliza para manipular y analizar datos.
```BASH
python3 pip install pandas
```
* [NLTK](https://pypi.org/project/typeguard/): Se utiliza para el procesamiento del lenguaje natural.
```BASH
python3 pip install nltk
```
* [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): Para analizar y extraer datos de documentos HTML y XML.
```BASH
python3 pip install beautifulsoup4
```
* [TextBlob](https://textblob.readthedocs.io/): Se utiliza para realizar tareas de análisis de texto como etiquetado de partes del discurso, análisis de sentimientos, análisis de sujetos y extracción de frases clave.
```BASH
python3 pip install textblob
python3 -m textblob.download_corpora
```
* [Spacy](https://textblob.readthedocs.io/): Se utiliza para realizar tareas avanzadas de procesamiento de texto, como etiquetado de partes del discurso, análisis sintáctico, reconocimiento de entidades nombradas, análisis semántico y más.
```BASH
python3 pip install spacy
python3 -m spacy download en_core_web_sm
```

**IMPORTANTE**: Para que funcione el programa es necesario tener instalado el modelo de lenguaje *en_core_web_sm* de Spacy.  
Para ello:
```BASH
python3 -m spacy download en_core_web_sm
```

## Referencias:
* [Pandas](https://pandas.pydata.org/)
* [NLTK](https://pypi.org/project/typeguard/)
* [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [TextBlob](https://textblob.readthedocs.io/)
* [Spacy](https://textblob.readthedocs.io/)


[Python website]: <https://www.python.org/downloads/>