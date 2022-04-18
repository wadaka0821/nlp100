import numpy as np
import pickle
import pandas as pd
import torch
from torch.nn import CrossEntropyLoss
from torch.optim import SGD
from sklearn.metrics import accuracy_score

from ex85 import get_batch, vectorize
from ex86 import CNN

if __name__ == '__main__':
    model = CNN()
    criterion = CrossEntropyLoss()
    optimizer = SGD(model.parameters(), lr=1e-2)
    
    seq_size = 20
    
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
    
    max_epoch = 500
    batch_size = 100
    for epoch in range(max_epoch):
        batch = 0
        l = 0
        while True:
            #print('batch {} / {}'.format(batch, int(len(train_X) / batch_size) + 1), end='\r')
            batch_X, batch_Y = get_batch(train_X, train_Y, batch*batch_size, batch_size)
            if not len(batch_X):
                break
            batch_X = torch.unsqueeze(batch_X, 1)
            optimizer.zero_grad()
            pred = model(batch_X)
            loss = criterion(pred, batch_Y)
            
            l += loss.item()
            loss.backward()
            
            optimizer.step()
            
            batch += 1
            
        if not (epoch + 1) % 50:
            print('epoch {} | loss {}'.format(epoch+1, l / (batch + 1)))
            
    with torch.no_grad():
        test_X = torch.unsqueeze(test_X, 1)
        out = model(test_X)
        loss = criterion(out, test_Y)
        print('test : loss {}'.format(loss.item()))
        
        pred = torch.argmax(out, dim=1)
        acc = accuracy_score(test_Y.to('cpu').detach().numpy().copy(), pred)
        print('test accuracy : {}'.format(acc))
            
            
    