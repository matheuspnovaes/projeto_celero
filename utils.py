
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

# opcao do modelo em modo de treinamento
def modo_treinamento(argv):
    directory = ''
    file_label = ''
    
    if (len(argv)==4):
        directory = argv[2]
        file_labels = argv[3]
        path_labels = os.path.join(directory, file_labels)
        if not os.path.exists(file_labels):
            print("O arquivo não existe ou não está no diretorio %s" % directory)
        else:
            try:
                label = np.genfromtxt(file_labels,  delimiter=',')
            except:
                print("Falha ao abrir o arquivo")
        if not os.path.exists(directory):
            print("O diretório não existe")
            sys.exit(2)
        else:
            reviews_list = open_reviews(directory)
            
            print("Vetorizando os  dados...")
            X_data = vectorizer_data(reviews_list)
            print("Processo concluido")
            #dividindo os dados em treino e validação
            X_train, X_vali, y_train, y_vali = train_test_split(
	            X_data, label, train_size = 0.7)
            print("Treinamento do modelo iniciado...")
            svm_model =  model_training(X_train, y_train)
            print("treinamento concluido")
            acuracia_vali = accuracy_score(y_vali, svm_model.predict(X_vali))
            print("Acuracia: %s"% acuracia_vali)
            file_model = "svm_model_trained.sav"
            print("Salvando o modelo treinado...")
            pickle.dump(svm_model,open(file_model,"wb"))
    else:
    
        print("Erro: O camando de entrada deve ser da seguinte forma:")
        print("python model.py <opção> <\"diretorio\"> <rotulos>")
        sys.exit(2)  





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