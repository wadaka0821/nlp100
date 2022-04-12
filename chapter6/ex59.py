import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

def train(solver, C=1., l1_ratio=None):
    train_X = pd.read_table('./data/train.feature.txt', encoding='utf-8', index_col=[0])
    train_Y = pd.read_table('./data/train.txt', encoding='utf-8', sep='\t', usecols=[2])

    clf = LogisticRegression(max_iter=1500, random_state=40, C=C, solver=solver, l1_ratio=l1_ratio)
    clf.fit(train_X.values, train_Y['category'].values)

    return clf

def search():
    params = [['newton-cg', [np.linspace(0.1, 1, 5)], ['l2']],
              ['lbfgs', [np.linspace(0.1, 1, 5)], ['l2']],
              ['saga', [np.linspace(0, 1, 5)], ['elasticnet']]]
    best_acc = 0.
    best_clf = None
    
    for param in params:
        for c in param[1][0]:
            if param[2][0] == 'l2':
                clf = train(param[0], c)
            else:
                clf = train(param[0], l1_ratio=c)
            valid_X = pd.read_table('./data/valid.feature.txt', encoding='utf-8', index_col=[0])
            valid_Y = pd.read_table('./data/valid.txt', encoding='utf-8', sep='\t', usecols=[2])
            pred_Y = clf.predict(valid_X.values)
            acc = accuracy_score(valid_Y, pred_Y)
            if best_acc < acc:
                best_clf = clf
                best_acc = acc
    return best_clf

if __name__ == '__main__':
    best_clf = search()
    print(best_clf)
    test_X = pd.read_table('./data/test.feature.txt', encoding='utf-8', index_col=[0])
    test_Y = pd.read_table('./data/test.txt', encoding='utf-8', sep='\t', usecols=[2])
    pred_Y = best_clf.predict(test_X.values)
    print(accuracy_score(test_Y, pred_Y))