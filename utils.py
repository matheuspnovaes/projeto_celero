
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