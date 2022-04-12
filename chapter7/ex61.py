from ex60 import load_from_pickle

if __name__ == '__main__':
    filename = './dic/word2vec.pickle'
    word2vec = load_from_pickle(filename)
    print(word2vec.similarity('United_States', 'U.S.'))