import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
import numpy as np
from ex53 import train

if __name__ == '__main__':
    categories = ['b', 'e', 'm', 't']
    clf = train()
    
    test_X = pd.read_table('./data/test.feature.txt', encoding='utf-8', index_col=[0])
    test_Y = pd.read_table('./data/test.txt', encoding='utf-8', sep='\t', usecols=[2])
    
    pred_Y = clf.predict(test_X.values)

    matrix = confusion_matrix(test_Y, pred_Y)
    for c in categories:
        dic = {i:'not ' + c if i != c else c for i in categories}
        vfunc = np.vectorize(lambda x:dic[x])
        binary_pred_Y = vfunc(pred_Y)
        binary_test_Y = vfunc(test_Y['category'].to_numpy())
        
        print('category : {}'.format(c))
        print('precision : {}'.format(precision_score(binary_test_Y, binary_pred_Y, pos_label=c)))
        print('recall : {}'.format(recall_score(binary_test_Y, binary_pred_Y, pos_label=c)))
        print('f1 : {}'.format(f1_score(binary_test_Y, binary_pred_Y, pos_label=c)))
    print('average')
    print('precision(micro) : {}'.format(precision_score(test_Y, pred_Y, average='micro')))
    print('precision(macro) : {}'.format(precision_score(test_Y, pred_Y, average='macro')))
    print('recall(micro) : {}'.format(recall_score(test_Y, pred_Y, average='micro')))
    print('recall(macro) : {}'.format(recall_score(test_Y, pred_Y, average='macro')))
    print('f1(micro) : {}'.format(f1_score(test_Y, pred_Y, average='micro')))
    print('f1(macro) : {}'.format(f1_score(test_Y, pred_Y, average='macro')))