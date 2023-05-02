from colors import bcolors
import spacy
from textblob import TextBlob
from bs4 import BeautifulSoup
import nltk
from tqdm import tqdm
import pandas as pd
import re

nltk.download('words', quiet=True)
nltk.download('stopwords', quiet=True)
# Contains a list of more than 236,000 English words, from common words to specialized terms.
dictionary = set(nltk.corpus.words.words())
# Contains a list of stopwords in english
stopwords = nltk.corpus.stopwords.words('english')
# Contains the important object to lemmatize
nlp = spacy.load('en_core_web_sm')


