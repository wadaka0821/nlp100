from cProfile import label
from ex60 import load_from_pickle
import numpy  as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

if __name__ == '__main__':
    filename = './dic/word2vec.pickle'
    word2vec = load_from_pickle(filename)
    
    countries = word2vec.most_similar(word2vec['Japan'] - word2vec['Tokyo'], topn=50)
    country_list, country_vec = list(), list()
    for country in countries:
        country_list.append(country[0])
        country_vec.append(word2vec[country_list[-1]])
    country_vec = np.array(country_vec)
    
    embedded_vec = TSNE(n_components=2).fit_transform(country_vec)
    for name, vec in zip(country_list, embedded_vec):
        plt.scatter(vec[0], vec[1])
        plt.annotate(name, vec)
    plt.show()