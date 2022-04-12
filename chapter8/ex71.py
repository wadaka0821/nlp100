import torch
from torch import nn
import pandas as pd

class SimpleNN(nn.Module):
    def __init__(self) -> None:
        super(SimpleNN, self).__init__()
        self.linear = nn.Linear(300, 4)
        self.softmax = nn.Softmax(dim=1)
        
    def forward(self, X):
        X = self.linear(X)
        X = self.softmax(X)
        return X
    
if __name__ == '__main__':
    train_X = pd.read_csv('./data/train_X.csv', encoding='utf-8', index_col=0)
    train_X = torch.tensor(train_X.values).float()
    
    nn = SimpleNN()
    with torch.no_grad():
        print(nn(train_X))