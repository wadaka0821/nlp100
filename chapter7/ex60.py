import gensim
import pickle

def save_as_pickle(filename, obj):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)
        
def load_from_pickle(filename):
    with open(filename, 'rb') as f:
        model = pickle.load(f)
    return model

if __name__ == '__main__':
    filename = './dic/word2vec.pickle'
    # word2vec = gensim.models.KeyedVectors.load_word2vec_format('./dic/GoogleNews-vectors-negative300.bin', binary=True)
    # save_as_pickle(filename, word2vec)
    word2vec = load_from_pickle(filename)
    print(word2vec['United_States'])