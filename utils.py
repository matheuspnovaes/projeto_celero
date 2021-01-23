
import sys, getopt
import os
import re
import joblib
import pickle

import numpy as np
import pandas as pd

from os import listdir

from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC





# leitura dos reviews
def open_reviews(directory):
    reviews_list = []
    # percorrer todos o diretório
    for filename in listdir(directory):
        # desconsiderar arquivos que não sejam .txt
        if not filename.endswith(".txt"):
            continue 
        path = os.path.join(directory, filename)
        with open(path,'r',encoding="utf8") as file:
            for line in file:
                reviews_list.append(textProcess(line.strip()))              
    return reviews_list

# remover pontuações e tags html do review
def textProcess(review):
    #expressão regular para remover pontuções
    exp_pontuacao = re.compile("[.;:!\'?,\"()\[\]]")
	#expressão regular para remover tags html 
    exp_htmlTag= re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
	
    review = exp_pontuacao.sub("", review.lower())
    review = exp_htmlTag.sub(" ",review)
	
    return review