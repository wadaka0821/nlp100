import pandas as pd
from sklearn.metrics import accuracy_score
from ex53 import train

if __name__ == '__main__':
    clf = train()
    
    train_X = pd.read_table('./data/train.feature.txt', encoding='utf-8', index_col=[0])
    train_Y = pd.read_table('./data/train.txt', encoding='utf-8', sep='\t', usecols=[2])
    
    pred_Y = clf.predict(train_X.values)
    print('train accuracy : {}'.format(accuracy_score(train_Y, pred_Y)))
    
    test_X = pd.read_table('./data/test.feature.txt', encoding='utf-8', index_col=[0])
    test_Y = pd.read_table('./data/test.txt', encoding='utf-8', sep='\t', usecols=[2])
    
    pred_Y = clf.predict(test_X.values)
    print('test accuracy : {}'.format(accuracy_score(test_Y, pred_Y)))