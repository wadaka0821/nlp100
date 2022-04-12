from ex71 import SimpleNN
import pandas as pd
import torch
from torch.nn import CrossEntropyLoss

if __name__ == '__main__':
    train_X = pd.read_csv('./data/train_X.csv', encoding='utf-8', index_col=0)
    train_X = torch.tensor(train_X.values).float()
    
    train_Y = pd.read_csv('./data/train_Y.csv', encoding='utf-8', index_col=0)
    train_Y = torch.tensor(train_Y.iloc[:, 0])
    
    criterion = CrossEntropyLoss()
    
    simple_nn = SimpleNN()
    pred = simple_nn(train_X)
    loss = criterion(pred, train_Y)
    
    print('loss :', loss.item())
    loss.backward()
    print(simple_nn.linear.weight.grad)
    
    