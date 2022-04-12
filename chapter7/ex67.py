from cProfile import label
from ex60 import load_from_pickle
from sklearn.cluster import KMeans
import numpy  as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

if __name__ == '__main__':
    filename = './dic/word2vec.pickle'
    word2vec = load_from_pickle(filename)
    
    '''
    countries = {i[0] for i in word2vec.most_similar('Japan', topn=300)}
    while len(countries) > 100:
        print(len(countries))
        for word in list(countries)[:10]:
            countries = countries.intersection({i[0] for i in word2vec.most_similar(word, topn=300)})
    print(countries)
    '''
    countries = word2vec.most_similar(word2vec['Japan'] - word2vec['Tokyo'], topn=300)
    country_list, country_vec = list(), list()
    for country in countries:
        country_list.append(country[0])
        country_vec.append(word2vec[country_list[-1]])
    country_vec = np.array(country_vec)
    kmeans = KMeans(n_clusters=5, random_state=40)
    kmeans.fit(country_vec)
    
    pca = PCA(n_components=2)
    pca.fit(country_vec)
    
    color_map = {0:'red', 1:'blue', 2:'yellow', 3:'black', 4:'green'}
    pred = kmeans.predict(country_vec)
    for name, cls, vec in zip(country_list, pred, country_vec):
        composed = pca.transform([vec])
        plt.scatter(composed[0][0], composed[0][1], c=color_map[cls])
        plt.annotate(name, composed[0])
    plt.show()