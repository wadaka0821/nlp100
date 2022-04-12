from ex60 import load_from_pickle

if __name__ == '__main__':
    filename = './dic/word2vec.pickle'
    word2vec = load_from_pickle(filename)
    print(word2vec.most_similar(word2vec['Spain'] - word2vec['Madrid'] + word2vec['Athens'], topn=10))