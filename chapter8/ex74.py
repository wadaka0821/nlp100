from ex71 import SimpleNN
import pandas as pd
import numpy as np
import torch
from torch.nn import CrossEntropyLoss
from torch.optim import SGD
from sklearn.metrics import accuracy_score

if __name__ == '__main__':
    train_X = pd.read_csv('./data/train_X.csv', encoding='utf-8', index_col=0)
    train_X = torch.tensor(train_X.values).float()
    
    train_Y = pd.read_csv('./data/train_Y.csv', encoding='utf-8', index_col=0)
    train_Y = torch.tensor(train_Y.iloc[:, 0])
    
    simple_nn = SimpleNN()
    
    criterion = CrossEntropyLoss()
    optimizer = SGD(simple_nn.parameters(), lr=0.6)
    
    max_epoch = 2000
    for epoch in range(max_epoch):
        optimizer.zero_grad()
        
        pred = simple_nn(train_X)
        loss = criterion(pred, train_Y)
        loss.backward()
        if (epoch + 1) % 50 == 0:
            print('epoch : {} | loss : {}'.format(epoch + 1, loss.item()))
            
        optimizer.step()
        
    with torch.no_grad():
        out = simple_nn(train_X)
        out = out.to('cpu').detach().numpy().copy()
        pred = np.argmax(out, axis=1)
        
        print('tain data :', accuracy_score(train_Y, pred))
        
        test_X = pd.read_csv('./data/test_X.csv', encoding='utf-8', index_col=0)
        test_X = torch.tensor(test_X.values).float()
        
        test_Y = pd.read_csv('./data/test_Y.csv', encoding='utf-8', index_col=0)
        testn_Y = torch.tensor(test_Y.iloc[:, 0])
        
        out = simple_nn(test_X)
        out = out.to('cpu').detach().numpy().copy()
        pred = np.argmax(out, axis=1)
        
        print('test data :', accuracy_score(test_Y, pred))
        

    