# -*- coding: utf-8 -*-
"""NLTK Course - Lemmatization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A0DiM6UDPOhYNFlIZGsV3emvu3jz7mRT
"""

from nltk.stem import PorterStemmer

ps = PorterStemmer()
words = ['was', 'runner', 'running', 'ran', 'mice', 'easily', 'fairly']
for word in words:
  print(word + '---->' + ps.stem(word))

  mouse --> mice

import nltk
nltk.download('punkt')

from nltk.stem import WordNetLemmatizer
wlem = WordNetLemmatizer()
wlem.lemmatize("mice")

import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

sentence = "He was running and eating at same time. He has bad habit of swimming after playing long hours in the Sun."
punctuations="?:!.,;"
sentence_words = nltk.word_tokenize(sentence)
for word in sentence_words:
    if word in punctuations:
        sentence_words.remove(word)

sentence_words
print("{0:20}{1:20}".format("Word","Lemma"))
for word in sentence_words:
    print ("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word, pos='v')))