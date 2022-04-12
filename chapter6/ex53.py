import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

def train():
    train_X = pd.read_table('./data/train.feature.txt', encoding='utf-8', index_col=[0])
    train_Y = pd.read_table('./data/train.txt', encoding='utf-8', sep='\t', usecols=[2])

    clf = LogisticRegression(max_iter=1500, random_state=40)
    clf.fit(train_X.values, train_Y['category'].values)

    return clf

def predict(clf, title:list[str]) -> str:
    train = pd.read_csv('./data/train.txt', encoding='utf-8', sep='\t')
    titles = train['title'].to_list()
    vectorizer = TfidfVectorizer(lowercase=True, max_df=0.7, min_df=0.01, ngram_range=(1, 1))
    vectorizer.fit(titles)
    return clf.predict(vectorizer.transform(title))

if __name__ == '__main__':
    clf = train()
    print(predict(clf, ['Small and midsize Kyushu firms look to Africa for growth']))