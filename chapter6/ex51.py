import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix

if __name__ == '__main__':
    train = pd.read_csv('./data/train.txt', encoding='utf-8', sep='\t')
    title = train['title'].to_list()
    vectorizer = TfidfVectorizer(lowercase=True, max_df=0.7, min_df=0.01, ngram_range=(1, 1))
    train_X = vectorizer.fit_transform(title)
    
    df = pd.DataFrame(csr_matrix.todense(train_X))
    df.to_csv('./data/train.feature.txt', sep='\t')
    
    valid = pd.read_csv('./data/valid.txt', encoding='utf-8', sep='\t')
    title = valid['title'].to_list()
    valid_X = vectorizer.transform(title)
    df = pd.DataFrame(csr_matrix.todense(valid_X))
    df.to_csv('./data/valid.feature.txt', sep='\t')
    
    test = pd.read_csv('./data/test.txt', encoding='utf-8', sep='\t')
    title = test['title'].to_list()
    test_X = vectorizer.transform(title)
    df = pd.DataFrame(csr_matrix.todense(test_X))
    df.to_csv('./data/test.feature.txt', sep='\t')