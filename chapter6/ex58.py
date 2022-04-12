import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

def train(norm:float):
    train_X = pd.read_table('./data/train.feature.txt', encoding='utf-8', index_col=[0])
    train_Y = pd.read_table('./data/train.txt', encoding='utf-8', sep='\t', usecols=[2])

    clf = LogisticRegression(max_iter=1500, random_state=40, C=norm)
    clf.fit(train_X.values, train_Y['category'].values)

    return clf

def evaluate(norm:float):
    res = dict()
    clf = train(norm)
    train_X = pd.read_table('./data/train.feature.txt', encoding='utf-8', index_col=[0])
    train_Y = pd.read_table('./data/train.txt', encoding='utf-8', sep='\t', usecols=[2])
    pred_Y = clf.predict(train_X.values)
    res['train'] = accuracy_score(train_Y, pred_Y)
    
    valid_X = pd.read_table('./data/valid.feature.txt', encoding='utf-8', index_col=[0])
    valid_Y = pd.read_table('./data/valid.txt', encoding='utf-8', sep='\t', usecols=[2])
    pred_Y = clf.predict(valid_X.values)
    res['valid'] = accuracy_score(valid_Y, pred_Y)
    
    test_X = pd.read_table('./data/test.feature.txt', encoding='utf-8', index_col=[0])
    test_Y = pd.read_table('./data/test.txt', encoding='utf-8', sep='\t', usecols=[2])
    pred_Y = clf.predict(test_X.values)
    res['test'] = accuracy_score(test_Y, pred_Y)
    
    return res

if __name__ == '__main__':
    params = np.linspace(0.01, 5, 50)
    train_score, valid_score, test_score = list(), list(), list()
    for param in params:
        scores = evaluate(param)
        train_score.append(scores['train'])
        valid_score.append(scores['valid'])
        test_score.append(scores['test'])
    plt.plot(params, train_score, label='train')
    plt.plot(params, valid_score, label='valid')
    plt.plot(params, test_score, label='test')
    
    plt.legend()
    plt.show()