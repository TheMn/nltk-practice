# -*- coding: utf-8 -*-
"""NLTK Course - Sentiment Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ASWaaX0a82Szp1PHZwnIY3zt1qx6w3Ol
"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
import nltk

nltk.download('punkt')
nltk.download('vader_lexicon')

my_string = "I read a book. The first three chapters were boring and depressing. Then the next 2 chapters were wonderful. I recommend this book to my friends."
sent = sent_tokenize(my_string)
print(sent)

sa = SentimentIntensityAnalyzer()
for sentence in sent:
  print(sentence)
  ps = sa.polarity_scores(sentence)
  for n in ps:
    print('{0}: {1}, '.format(n, ps[n]), end='')
  print()
  print()