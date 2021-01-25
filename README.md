# <center> Projeto: Classificador de comentários de filmes.</center> 
<center> <span style="color:blue; font-size: 1.5em;">Matheus Pereira de Novaes</span></center>
<center> <span style="color:blue; font-size: 1.0em;">matheuspnovaes@gmail.com</span></center>
<center> <span style="color:red">25 de janeiro de 2021</span> </center>

# 1. Introdução 

Este projeto é um desafio proposto pela CELERO com a finiladade de testar as habilidades e conhecimento de algoritmos de classificação
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
que serão gerados por outros processo. Sua utilização é útil para
`git clean` antes de comportilhar o código no `git`
- `README.md` contêm a descrição e documentação do projeto.
- `model.py` contêm a definição do modelo de classificação utilizado. Além disso, 
conta com as funções de treinamento e execução.
- `requirements.txt` contêm todas as dependências que são requeridas pela aplicação
- `review_vectorizer.pkl` arquivo com o dicionário salvo dos dados de treinamento.
- `svm_model_trained.pkl` arquivo com o modelo SVM já treinado.
- `utilis.py` contêm as funcionabilidades da aplicação.


