import pandas as pd
from sklearn.linear_model import LogisticRegression

if __name__ == '__main__':
    train_X = pd.read_table('./data/train.feature.txt', encoding='utf-8', index_col=[0])
    train_Y = pd.read_table('./data/train.txt', encoding='utf-8', sep='\t', usecols=[2])
    #print(train_X.head())
    #print(train_Y.head())
    #train_Y['category_num'] = train_Y['category'].apply(lambda x:{'e':0, 'b':1, 't':2, 'm':3}[x])
    #print(train_Y.head())

    clf = LogisticRegression(max_iter=1500, random_state=40)
    clf.fit(train_X, train_Y['category'])
    print(clf.predict(train_X[:10]))