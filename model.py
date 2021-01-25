import sys, getopt
import os
import re
import numpy as np

import joblib
import pickle
#import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC


from utils import open_reviews, textProcess, vectorizer_data

# opcao do modelo em modo de treinamento
def modo_treinamento(argv):
    directory = ''
    file_label = ''
    
    if (len(argv)==4):
        directory = argv[2]
        file_labels = argv[3]
        print(file_labels)
        path_labels = os.path.join(directory, file_labels)
        
        try:
            label = np.genfromtxt(file_labels,  delimiter=',')
        except:
            print("Falha ao abrir o arquivo de rotulos")
            sys.exit(2)
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
        
def modo_execucao(argv):
    reviews_list = []
    file_teste = ''
    review_vectorizer = joblib.load("review_vectorizer.pkl")
    print(len(argv))
    if (len(argv)==3):
        file_teste = argv[2]
        if not os.path.exists(file_teste):
            print("O arquivo não existe ou não está no diretorio")
        else:
            with open(file_teste,'r',encoding="utf8") as file:
                for line in file:
                    reviews_list.append(textProcess(line.strip()))    
            print("Vetorizando os dados...")
            X_data = review_vectorizer.transform(reviews_list)
            svm_model = pickle.load(open('svm_model_trained.sav', 'rb'))
            result = svm_model.predict(X_data)
            print("Classificação do review: %s"% result[0])
    else:
        print("Erro: O camando de entrada deve ser da seguinte forma:")
        print("python model.py <opção> <arquivo_teste>")
        sys.exit(2)  
  


def model_training(X_train, y_train):       
    model = LinearSVC(C=0.01)
    model.fit(X_train,y_train)
    return model


# dicionario para selecionar treinamento ou execução 
optionDic={
    '1': modo_treinamento,
    '2': modo_execucao
}


        
def main(argv):
    optionDic[argv[1]](argv)        
if __name__ == "__main__":
   main(sys.argv)       