# -*- coding: utf-8 -*-
"""NLTK Course - preprocessing_practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KHyS-YoybaQpSMR9g-EaIfnKCW9aIeLb
"""

from IPython.display import HTML, display

def set_css():
  display(HTML('''
  <style>
    pre {
        white-space: pre-wrap;
    }
  </style>
  '''))
get_ipython().events.register('pre_run_cell', set_css)

"""# We're gonna practice the following:

- Use the following text from IMDB dataset:
- Tokenize sentences.
- Tokenize words.
- Lemmatize the tokens
- Perform POS
- Lemmatization with POS
- Perform NER

"Our family and the entire sold out sneak preview audience enjoyed The Guardian. Kevin Costner and Ashton Kutcher gave convincing performances as the fictional helicopter rescue swimmer characters Ben and Jake. After seeing this movie, you can't help but imagine how difficult it must be to graduate from the USCG helicopter rescue swimmer school and one day take part in real rescues.Even though this is a fictional movie, it delivered rather convincing virtues of team spirit, dedication and bravery exhibited by all the members of the actual U. S. Coast Guard.The special effects used to create the rescue scenes were incredible. You actually felt like you were taking part in a real rescue.I feel the movie could have been made without the Hollywood bar scene when you see the movie, you might agree since the real Coast Guard does not condone such behavior. Very entertaining, very action packed, definitely worth seeing. Thank you, US Coast Guard and the REAL helicopter rescue swimmers, So Others May Live. I'd highly recommend this movie to everyone."
"""

my_string = "Our family and the entire sold out sneak preview audience enjoyed The Guardian. Kevin Costner and Ashton Kutcher gave convincing performances as the fictional helicopter rescue swimmer characters Ben and Jake. After seeing this movie, you can't help but imagine how difficult it must be to graduate from the USCG helicopter rescue swimmer school and one day take part in real rescues. Even though this is a fictional movie, it delivered rather convincing virtues of team spirit, dedication and bravery exhibited by all the members of the actual US Coast Guard. The special effects used to create the rescue scenes were incredible. You actually felt like you were taking part in a real rescue. I feel the movie could have been made without the Hollywood bar scene when you see the movie, you might agree since the real Coast Guard does not condone such behavior. Very entertaining, very action packed, definitely worth seeing. Thank you, US Coast Guard and the real helicopter rescue swimmers, So Others May Live. I'd highly recommend this movie to everyone."

# IMPORTING LIBRARIES
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk import ne_chunk

nltk.download("punkt")
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# SENTENCE TOKENIZATION
sentences = sent_tokenize(my_string)
print(sentences)

# WORD TOKENIZATION
words = []
for sentence in sentences:
  words.extend(word_tokenize(sentence))
print(words)

# LEMMATIZATION
lemma = []
wordnet_lemmatizer = WordNetLemmatizer()
for word in words:
  l = wordnet_lemmatizer.lemmatize(word, pos='v')
  lemma.append(l)
print(lemma)

# POS TAGGING
tagged = pos_tag(lemma)
print(tagged)

from nltk.corpus import wordnet

def getpos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''

# LEMMATIZATION WITH POS
punctuation = u",.?!()-_\"\'\\\n\r\t;:+*<>@#§^$%&|/"
stop_words_eng = set(stopwords.words('english'))
lemma_pos = []
for word, tag in tagged:
  if word not in punctuation and word not in stop_words_eng:
    p = getpos(tag)
    if p != '':
      l = wordnet_lemmatizer.lemmatize(word, pos = p)
      lemma_pos.append(l)
print(lemma_pos)

# NAMED ENTITY RECOGNITION (NER)
print(ne_chunk(tagged, binary = False))