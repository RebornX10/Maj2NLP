import time as time
import numpy as np
import pandas as pd
import re
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import ToktokTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tag.util import untag
import contractions
# import pycontractions # Alternative better package for removing contractions
from autocorrect import Speller

spell = Speller()
token = ToktokTokenizer()
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
charac = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~0123456789'
stop_words = set(stopwords.words("english"))
adjective_tag_list = set(['JJ','JJR', 'JJS', 'RBR', 'RBS']) # List of Adjective's tag from nltk package


def clean_text(text):
    text = re.sub(r"\'", "'", text) # apostrophe characters to whitespace
    text = re.sub(r"\n", " ", text) # newlines to whitespace
    text = re.sub(r"\xa0", " ", text) # non-breakable to whitespace
    text = re.sub('\s+', ' ', text) # more than one whitespace character to a single whitespace
    text = text.strip(' ')
    return text.lower()

def expand_contractions(text):
    text = contractions.fix(text)
    return text


def autocorrect(text):
    words = token.tokenize(text)
    words_correct = [spell(w) for w in words]
    return ' '.join(map(str, words_correct)) # Return the text untokenize

def remove_punctuation_and_number(text):
    """remove all punctuation and number"""
    return text.translate(str.maketrans(" ", " ", charac))



def remove_non_alphabetical_character(text):
    """remove all non-alphabetical character"""
    text = re.sub("[^a-z]+", " ", text) # remove all non-alphabetical character
    text = re.sub("\s+", " ", text) # remove whitespaces left after the last operation
    return text


def clean_quest(text: str):
    return remove_non_alphabetical_character(remove_punctuation_and_number(expand_contractions(autocorrect(clean_text(text)))))



