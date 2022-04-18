import numpy as np
import pandas as pd
import pickle
import torch
from torch.nn import Conv2d, MaxPool2d, Linear, Softmax, Flatten, Module

from ex85 import vectorize

class CNN(Module):
    def __init__(self) -> None:
        super(CNN, self).__init__()
        
        self.conv1 = Conv2d(1, 3, (3, 300), padding=(2, 0))
        self.pool1 = MaxPool2d((3, 1))
        self.conv2 = Conv2d(3, 3, (3, 1), padding=(2, 0))
        self.flatten = Flatten()
        self.linear = Linear(9, 4)
        self.softmax = Softmax(dim=1)
        
    def forward(self, X):
        X = self.conv1(X)
        X = self.pool1(X)
        X = self.conv2(X)
        X = self.pool1(X)
        X = X.reshape((X.shape[0], -1))
        X = self.linear(X)
        Y = self.softmax(X)
        
        return Y
    
if __name__ == '__main__':
    vocab = None
    with open('vocab.pickle', 'rb') as f:
        vocab = pickle.load(f)
        
    batch_size = 100
    hidden_size = 100
    seq_size = 20
    model = CNN()
    #criterion = CrossEntropyLoss()
    #optimizer = SGD(rnn.parameters(), lr=2e-3)
    
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
    
    model(train_X.reshape((train_X.shape[0], 1, train_X.shape[1], train_X.shape[2])))