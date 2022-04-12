import sys
import pandas as pd
sys.path.append('../chapter7')
from ex60 import load_from_pickle
import numpy as np
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def w2v_tokenize_text(text):
    tokens = []
    for sent in nltk.sent_tokenize(text, language='english'):
        for word in nltk.word_tokenize(sent, language='english'):
            if len(word) < 2:
                continue
            if word.lower() in stopwords.words('english'):
                continue
            tokens.append(word)
    return tokens

def convert(df, vectorizer):
    X = list()
    Y = list()
    class_map = {'b':0, 't':1, 'e':2, 'm':3}
    for i in df.itertuples():
        tokens = w2v_tokenize_text(i[1])
        vec = np.zeros(shape=(300,))
        N = 0
        for token in tokens:
            if token in vectorizer:
                vec += vectorizer[token]
                N += 1
        vec /= N
        X.append(vec)
        Y.append(class_map[i[2]])
    return X, Y
    

if __name__ == '__main__':
    filename = '../chapter7/dic/word2vec.pickle'
    word2vec = load_from_pickle(filename)
    
    #train_df = pd.read_table('../chapter6/data/train.txt', index_col=0)
    #X, Y = convert(train_df, word2vec)
    
    #pd.DataFrame(X).to_csv('./data/train_X.csv')
    #pd.DataFrame(Y).to_csv('./data/train_Y.csv')
    
    valid_df = pd.read_table('../chapter6/data/valid.txt', index_col=0)
    X, Y = convert(valid_df, word2vec)
    
    pd.DataFrame(X).to_csv('./data/valid_X.csv')
    pd.DataFrame(Y).to_csv('./data/valid_Y.csv')
    
    test_df = pd.read_table('../chapter6/data/test.txt', index_col=0)
    X, Y = convert(test_df, word2vec)
    
    pd.DataFrame(X).to_csv('./data/test_X.csv')
    pd.DataFrame(Y).to_csv('./data/test_Y.csv')