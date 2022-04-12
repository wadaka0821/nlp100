import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import numpy as np
from ex60 import load_from_pickle

if __name__ == '__main__':
    filename = './dic/word2vec.pickle'
    word2vec = load_from_pickle(filename)

    countries = word2vec.most_similar(word2vec['Japan'] - word2vec['Tokyo'], topn=50)
    country_list, country_vec = list(), list()
    for country in countries:
        country_list.append(country[0])
        country_vec.append(word2vec[country_list[-1]])
    country_vec = np.array(country_vec)
    
    linkage_res = linkage(country_vec, 'ward')
    dendrogram(linkage_res, labels=country_list)
    plt.show()
