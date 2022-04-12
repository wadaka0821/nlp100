from ex71 import SimpleNN
import pandas as pd
import torch
from torch.nn import CrossEntropyLoss
from torch.optim import SGD

if __name__ == '__main__':
    train_X = pd.read_csv('./data/train_X.csv', encoding='utf-8', index_col=0)
    train_X = torch.tensor(train_X.values).float()
    
    train_Y = pd.read_csv('./data/train_Y.csv', encoding='utf-8', index_col=0)
    train_Y = torch.tensor(train_Y.iloc[:, 0])
    
    simple_nn = SimpleNN()
    
    criterion = CrossEntropyLoss()
    optimizer = SGD(simple_nn.parameters(), lr=0.6)
    
    max_epoch = 1000
    for epoch in range(max_epoch):
        optimizer.zero_grad()
        
        pred = simple_nn(train_X)
        loss = criterion(pred, train_Y)
        loss.backward()
        if (epoch + 1) % 50 == 0:
            print('epoch : {} | loss : {}'.format(epoch + 1, loss.item()))
            
        optimizer.step()

    