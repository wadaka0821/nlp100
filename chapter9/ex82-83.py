from ex80 import vectorize
from ex81 import MyRNN
import numpy as np
import pandas as pd
import pickle
import torch
from torch.optim import SGD
from torch.nn import CrossEntropyLoss

def get_batch(X, Y, idx, batch_size):
    if idx < len(X):
        return X[idx:min(len(X), idx+batch_size)], Y[idx:min(len(Y), idx+batch_size)]
    else:
        return list(), list()

if __name__ == '__main__':
    vocab = None
    with open('vocab.pickle', 'rb') as f:
        vocab = pickle.load(f)
        
    batch_size = 50
    hidden_size = 50
    seq_size = 20
    rnn = MyRNN(embedding_dim=300, hidden_dim=hidden_size, batch_size=batch_size)
    criterion = CrossEntropyLoss()
    optimizer = SGD(rnn.parameters(), lr=0.4)
    
    train_data = pd.read_table('../chapter6/data/train.txt', encoding='utf-8', index_col=0)
    train_X = train_data.iloc[:, 0]
    train_X = np.array([vectorize(text, vocab, 300, seq_size) for text in train_X])
    train_X = torch.from_numpy(train_X).float()
    
    mapping = {'e':0, 'b':1, 't':2, 'm':3}
    train_Y = train_data.iloc[:, 1]
    train_Y = torch.from_numpy(np.array([mapping[i] for i in train_Y]))
    
    max_epoch = 1000
    for epoch in range(max_epoch):
        i = 0
        l = 0
        while True:
            batch_X, batch_Y = get_batch(train_X, train_Y, i*batch_size, batch_size)
            if not len(batch_X):
                break
            elif len(batch_X) < batch_size:
                batch_X = torch.concat([batch_X, torch.zeros(batch_size-len(batch_X), seq_size, 300)])
                batch_Y = torch.concat([batch_Y, torch.zeros(batch_size-len(batch_Y))]).long()
            batch_X = batch_X.reshape(seq_size, batch_size, -1)
            
            optimizer.zero_grad()
            pred_Y = rnn(batch_X)
            loss = criterion(pred_Y, batch_Y)
            l += loss.item()
            loss.backward()
            
            optimizer.step()
            
            i += 1
        
        if (epoch + 1) % 50 == 0:
            print('epoch : {} | loss : {}'.format(epoch+1, l / (i+1)))
    