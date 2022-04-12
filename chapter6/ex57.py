import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from ex53 import train

def get_vocabulary() -> dict[str, int]:
    train = pd.read_csv('./data/train.txt', encoding='utf-8', sep='\t')
    titles = train['title'].to_list()
    vectorizer = TfidfVectorizer(lowercase=True, max_df=0.7, min_df=0.01, ngram_range=(1, 1))
    vectorizer.fit(titles)
    
    return vectorizer.vocabulary_

if __name__ == '__main__':
    clf = train()
    coef = clf.coef_
    vocab = {value:key for key, value in get_vocabulary().items()}
    f = np.vectorize(lambda x:vocab[x])
    categories = ['b', 'e', 'm', 't']
    for c, vec in zip(categories, coef):
        print('category {}'.format(c))
        
        sorted_indices = np.argsort(vec)
        upper_indices = sorted_indices[-10:]
        lesser_indices = sorted_indices[:10]
        print('top 10 positive')
        print('{}'.format(f(upper_indices)))
        print('top 10 negative')
        print('{}'.format(f(lesser_indices)))

    