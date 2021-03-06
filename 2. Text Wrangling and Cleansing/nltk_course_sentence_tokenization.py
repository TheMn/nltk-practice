# -*- coding: utf-8 -*-
"""NLTK Course - Sentence tokenization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Feegv8b_W_X1IHSwlmIbjLxl3N9UOmsu
"""

import nltk
nltk.download("punkt")
myString = 'This is a large text. It is usually separated into sentences. We know that, but computers do not.'
from nltk.tokenize import sent_tokenize
sentences = sent_tokenize(myString)
print(sentences)

import nltk.data
sentences = "Hola. Esta es una frase espanola"
spanish_sentence_tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
sentences = spanish_sentence_tokenizer.tokenize(sentences)
print(sentences)

import nltk
nltk.download('webtext')

from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext
text = webtext.raw('overheard.txt')
print(text)

sent_tokenizer = PunktSentenceTokenizer(text)

sents1 = sent_tokenizer.tokenize(text)
sents1[0]

from nltk.tokenize import sent_tokenize
sents2 = sent_tokenize(text)
sents2[0]

print(sents1[678])

print(sents2[678])