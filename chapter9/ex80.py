from lib2to3.pgen2 import token
from sys import maxsize
from nltk.tokenize import word_tokenize
from collections import Counter
import pickle
import numpy as np

def make_vocablary(filename='../chapter6/data/train.txt'):
    with open(filename, 'r', encoding='utf-8') as f:
        words = list(map(lambda x:x.lower(), word_tokenize(f.read())))
        counter = Counter(words)
        words = sorted([[key, value] for key, value in counter.items() if value > 1], key=lambda x:x[::-1], reverse=True)
        return {j[0]:i for i, j in enumerate(words, 1)}
    
def vectorize(text, vocab, max_size=300, seq_size=20):
    words = list(map(lambda x:x.lower(), word_tokenize(text)))
    tokens = np.zeros((len(words), max_size))
    for i, word in enumerate(words):
        if word in vocab and vocab[word] < max_size:
            tokens[i, vocab[word]] = 1
        else:
            tokens[i, 0] = 1
    if len(tokens) > seq_size:
        tokens = tokens[:seq_size]
    elif len(tokens) < seq_size:
        tokens = np.concatenate([tokens, np.zeros((seq_size-len(tokens), max_size))], axis=0)
    return tokens

if __name__ == '__main__':
    '''
    vocab = make_vocablary()
    with open('vocab.pickle', 'wb') as f:
        pickle.dump(vocab, f)
    '''
    
    vocab = None
    with open('vocab.pickle', 'rb') as f:
        vocab = pickle.load(f)
        
    text = 'hello, good moring.'
    print(vectorize(text, vocab))