# IAA - Segunda parte proyecto: 
* author: Saúl Sosa Díaz
* email: _alu0101404141@ull.edu.es_

## Resumen
El objetivo es clasificar correctamente una serie de noticias dadas.

## Ejecución

```BASH
python3 ./src/main.py
```

## Opciones del programa
 * -v  -> Crea el vocabulario de las noticias de entrenamiento
 * -c  -> Crea los corpus y los guarda en la carpeta corpus.
 * -m  -> Crea los modelos.
 * -t  -> Preprocesa el texto a clasificar


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