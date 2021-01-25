
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


import gzip, pickle, pickletools


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

# convertendo o texto em vetor: Bag of words    
def vectorizer_data(reviews_list):
    review_vectorizer = CountVectorizer(binary=True, ngram_range=(1, 3), 
									stop_words=['in', 'of', 'at', 'a', 'the'])
    review_vectorizer.fit(reviews_list)
    # salvando o vocabulario
    joblib.dump(review_vectorizer, "review_vectorizer.pkl")
    # dados tratados e vetorizados
    X_data = review_vectorizer.transform(reviews_list)
    
    return X_data

# salvar o modelo treinado
def save_model(model):
    model_path = 'svm_model_trained.pkl'
    with gzip.open(model_path, "wb") as file:
    pickled =  pickle.dumps(model)
    optmized_pickle = pickletools.optimize(pickled)
    file.write(optimized_pickle)

# carregar modelo já treinado 
def load_model()
    model_path = 'svm_model_trained.pkl'
    with gzip.open(filepath, 'rb') as f:
        p = pickle.Unpickler(f)
        svm_model = p.load()
    return svm_model    
    