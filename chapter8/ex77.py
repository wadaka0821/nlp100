from cProfile import label
from inspect import getabsfile
from ex71 import SimpleNN
import pandas as pd
import numpy as np
import torch
from torch.nn import CrossEntropyLoss
from torch.optim import SGD
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def get_batch(X, Y, idx, batch_size):
    if idx < len(X):
        return X[idx:min(len(X), idx+batch_size)], Y[idx:min(len(Y), idx+batch_size)]
    else:
        return list(), list()

def validate(model, criterion):
    valid_X = pd.read_csv('./data/valid_X.csv', encoding='utf-8', index_col=0)
    valid_X = torch.tensor(valid_X.values).float()
    
    valid_Y = pd.read_csv('./data/valid_Y.csv', encoding='utf-8', index_col=0)
    valid_Y = torch.tensor(valid_Y.iloc[:, 0])
    
    with torch.no_grad():
        out = model(valid_X)

        loss = criterion(out, valid_Y)
        out = out.to('cpu').detach().numpy().copy()
        pred = np.argmax(out, axis=1)
        
        return loss, accuracy_score(valid_Y, pred)

if __name__ == '__main__':
    train_X = pd.read_csv('./data/train_X.csv', encoding='utf-8', index_col=0)
    train_X = torch.tensor(train_X.values).float()
    
    train_Y = pd.read_csv('./data/train_Y.csv', encoding='utf-8', index_col=0)
    train_Y = torch.tensor(train_Y.iloc[:, 0])
    
    simple_nn = SimpleNN()
    
    criterion = CrossEntropyLoss()
    optimizer = SGD(simple_nn.parameters(), lr=2.1)
    
    max_epoch = 700
    batch_size = 20
    for epoch in range(max_epoch):
        i = 0
        batch_loss = 0
        while True:
            X, Y = get_batch(train_X, train_Y, i*batch_size, batch_size)
            
            if not len(X):
                break

            optimizer.zero_grad()
            
            pred = simple_nn(X)
            loss = criterion(pred, Y)
            
            batch_loss += loss.item()
            loss.backward()
                
            optimizer.step()
            
            i += 1
                
        if not (epoch + 1) % 50:
            print('epoch : {}'.format(epoch + 1), end=' | ')
            print('train_loss : {}'.format(batch_loss / (i + 1)), end=' | ')
            valid_loss, _ = validate(simple_nn, criterion)
            print('validation_loss: {}'.format(valid_loss))
        
    with torch.no_grad():
        out = simple_nn(train_X)
        out = out.to('cpu').detach().numpy().copy()
        pred = np.argmax(out, axis=1)
        
        print('train data :', accuracy_score(train_Y, pred))
        
        test_X = pd.read_csv('./data/test_X.csv', encoding='utf-8', index_col=0)
        test_X = torch.tensor(test_X.values).float()
        
        test_Y = pd.read_csv('./data/test_Y.csv', encoding='utf-8', index_col=0)
        testn_Y = torch.tensor(test_Y.iloc[:, 0])
        
        out = simple_nn(test_X)
        out = out.to('cpu').detach().numpy().copy()
        pred = np.argmax(out, axis=1)
        
        print('test data :', accuracy_score(test_Y, pred))
        

    