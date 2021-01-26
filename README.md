# <center> Projeto: Classificador de comentários de filmes.</center> 
<center> <span style="color:blue; font-size: 1.5em;">Matheus Pereira de Novaes</span></center>
<center> <span style="color:blue; font-size: 1.0em;">matheuspnovaes@gmail.com</span></center>
<center> <span style="color:red">25 de janeiro de 2021</span> </center>

# 1. Introdução 

Este projeto é um desafio proposto pela CELERO com a finalidade de testar as habilidades e conhecimento de algoritmos de classificação
com base em aprendizado de máquinas supervisionado, assim como a implementação destas 
soluções utilizando a linguagem de programação Python.

## 1.1 Objetivo 

O objetivo foi criar classificador de comentário de filmes, utilizando o cojunto de dados 
[Large Movie Review Dataset](http://ai.stanford.edu/~amaas/data/sentiment/). 
O modelo preditivo determinar se um comentário é negativo ou positivo
A métrica utlizada para avalição foi a [Acurácia](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html) 

## 1.2 Cojunto de dados: Descrição

O [Large Movie Review Dataset](http://ai.stanford.edu/~amaas/data/sentiment/) é um conjunto de 
dados para a classifcação binária de sentimento. Este dataset contêm 50 mil reviews de filmes 
divididos em 25 mil para treino 25 mil para teste. Os reviews são rotulados como positivos ou negativos. 

# 2 Organização do projeto

Os arquivos que compõem o projeto são explicados a seguir: 

- `.gitignore` é importante devido a geração de arquivos adicionais 
que serão gerados por outros processos. Sua utilização é útil para
`git clean` antes de compartilhar o código no `git`
- `README.md` contêm a descrição e documentação do projeto.
- `model.py` contêm a definição do modelo de classificação utilizado. Além disso, 
conta com as funções de treinamento e execução.
- `requirements.txt` contêm todas as dependências que são requeridas pela aplicação
- `review_vectorizer.pkl` arquivo com o dicionário salvo dos dados de treinamento.
- `svm_model_trained.pkl` arquivo com o modelo SVM já treinado.
- `utils.py` contêm as funcionabilidades da aplicação.

# # 2.1 Documentação

- `model.py`: 

```python
def main(argv):
# a função define se a aplicação será iniciada 
# em modo treinamento ou execução
#  argv: parâmetros da incilização da aplicação

def modo_treinamento(argv):
# função utilizada para executar a aplicação 
# em modo de treinamento
# argv: parâmetro com diretório dos arquivos
# de treinamento e o arquivo de rotulo.


def modo_execucao(argv):
# função utilizada para execução a aplição após
# o treinamento
# argv: parâmetro com o nome do arquivo para classificação


def model_training(X_train, y_train):
# função para treinar o modelo
# X_train: cojunto de dados de treinamento
# y_train: resultado esperado do cojunto de treinamento 
```

- `utils.py`: 
```python

def open_reviews(directory):
# função para abrir os reviews
# directory: diretório com os reviews
# retorna uma lista contendo os reviews

def textProcess(review):
# processa o review para eliminar
# pontuações e tags html
# review: texto para ser processado
# retorna review  processado

def vectorizer_data(reviews_list):
# converte o texto em vetor: Bag of words
# reviews_list: recebe uma lista com reviews
# retorna X_data contendo os dados vetorizados

def save_pkl(fileToSave, path):
# salva determinado dado em um arquivo pkl
# fileToSave: dado para ser salvo
# path: diretório para salvar o dado

def load_pkl(pkl_path):
# carrega determinado dado que foi
# salvo em um arquivo pkl
# pkl_path: diretório do arquivo p
# para ser aberto 
# retorna o arquivo lido
  
```


# 3 Ambiente virtual 

Este projeto é executado em um ambiente virtual. Um ambiente virtual é uma instalação Python 
específica que gerencia seus próprios binários e pacotes. Uma grande vantagem que isso oferece
é que cada projeto  tem seu próprio ambiente sem nenhuma configuração global.

Veja maiores detalhes de [ambiente virtual](https://docs.python.org/pt-br/3/library/venv.html) em sua documentação.


# 4 Utilizando a aplicação

# # 4.1 Instalar os requirements
1. Instalar o Python 3
2. Instalar o `virtualenv`

# # 4.2: Criar um novo projeto
1. Clonar este projeto 
2. Criar um novo ambiente virtual e ativá-lo, utilizando o `virtualenv`
3. No ambiente virtual criado, instalar os pacotes requeridos:
   ```sh
    pip install -r requirements.txt
    ``` 
# # 4.3 Aplicação em modo de treinamento
1. Executar o `model.py` com os seguintes parâmetros
 ```sh
    python model.py <opção> <"diretorio"> <"rotulos">
 ```
 - `<opção>` = 1 para treinamento
 - `<"diretorio">`: caminho para o diretório contendo os
    reviews dentro de arquivos `.txt`
 - `<"rotulos>`: arquivo `.txt` com o resultado dos reviews.
 Cada linha do arquivo representa o resultado de um review.
 1 para reviews positivos e -1 para reviews negativos. 
 
 ```sh
    python model.py 1 "C:\Users\projeto_celero\train" "C:\Users\projeto_celero\rotulos.txt"
 ```

# # 4.4 Aplicação em modo execução
1. Executar o `model.py` com os seguintes parâmetros:
  ```sh
     python model.py <opção> <"review.txt">
  ```
  - `<opção>` = 2 para modo execução
  - `<"review.txt">` : arquivo `.txt` com o review 
   ```sh
    python model.py 2 "C:\Users\projeto_celero\teste\0_2.txt"
 ```