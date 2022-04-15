from ex81 import MyRNN
import numpy as np
import pandas as pd
import pickle
import torch
from torch.optim import SGD
from torch.nn import CrossEntropyLoss
from sklearn.metrics import accuracy_score
import nltk
import sys

sys.path.append('../chapter7')
from ex60 import load_from_pickle

vectorizer = load_from_pickle('../chapter7/dic/word2vec.pickle')
#nltk.download('punkt')

def get_batch(X, Y, idx, batch_size):
    if idx < len(X):
        return X[idx:min(len(X), idx+batch_size)], Y[idx:min(len(Y), idx+batch_size)]
    else:
        return list(), list()

def vectorize(text, seq_size):
    embedding_dim = 300
    tokens = nltk.word_tokenize(text)
    if len(tokens) > seq_size:
        tokens = tokens[:seq_size]
    tokens = np.array([vectorizer[token] if token in vectorizer else np.zeros((embedding_dim, )) for token in tokens])
    if len(tokens) < seq_size:
        tokens = np.concatenate([tokens, np.zeros((seq_size - len(tokens), embedding_dim))], axis=0)
    return tokens
    
if __name__ == '__main__':
    vocab = None
    with open('vocab.pickle', 'rb') as f:
        vocab = pickle.load(f)
        
    batch_size = 100
    hidden_size = 100
    seq_size = 20
    rnn = MyRNN(embedding_dim=300, hidden_dim=hidden_size)
    criterion = CrossEntropyLoss()
    optimizer = SGD(rnn.parameters(), lr=2e-3)
    
    train_data = pd.read_table('../chapter6/data/train.txt', encoding='utf-8', index_col=0)
    train_X = train_data.iloc[:, 0]
    train_X = np.array([vectorize(text, seq_size) for text in train_X])
    train_X = torch.from_numpy(train_X).float()
    
    mapping = {'e':0, 'b':1, 't':2, 'm':3}
    train_Y = train_data.iloc[:, 1]
    train_Y = torch.from_numpy(np.array([mapping[i] for i in train_Y]))
    
    test_data = pd.read_table('../chapter6/data/test.txt', encoding='utf-8', index_col=0)
    test_X = test_data.iloc[:, 0]
    test_X = np.array([vectorize(text, seq_size) for text in test_X])
    test_X = torch.from_numpy(test_X).float()
    
    test_Y = test_data.iloc[:, 1]
    test_Y = torch.from_numpy(np.array([mapping[i] for i in test_Y]))
    
    max_epoch = 700
    for epoch in range(max_epoch):
        i = 0
        l = 0
        while True:
            batch_X, batch_Y = get_batch(train_X, train_Y, i*batch_size, batch_size)
            if not len(batch_X):
                break
            batch_X = torch.swapaxes(batch_X, 0, 1)
            
            optimizer.zero_grad()
            pred_Y = rnn(batch_X)
            loss = criterion(pred_Y, batch_Y)
            l += loss.item()
            loss.backward()
            
            optimizer.step()
            
            i += 1
        
        if (epoch + 1) % 10 == 0:
            print('epoch : {} | loss : {}'.format(epoch+1, l / (i+1)))
            
    with torch.no_grad():
        test_X = torch.swapaxes(test_X, 0, 1)
        out = rnn(test_X)
        loss = criterion(out, test_Y)
        print('test : loss {}'.format(loss.item()))
        
        pred = torch.argmax(out, dim=1)
        acc = accuracy_score(test_Y.to('cpu').detach().numpy().copy(), pred)
        print('test accuracy : {}'.format(acc))
    