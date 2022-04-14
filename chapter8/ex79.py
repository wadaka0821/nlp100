import torch
from torch.nn import Linear, Softmax, CrossEntropyLoss, ReLU, Dropout
from torch.optim import Adam, SGD
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

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

class DNN(torch.nn.Module):
    def __init__(self) -> None:
        super(DNN, self).__init__()
        
        self.hidden1 = Linear(300, 100)
        self.activation = ReLU()
        self.hidden2 = Linear(in_features=self.hidden1.out_features, out_features=100)
        self.hidden3 = Linear(in_features=self.hidden2.out_features, out_features=4)
        self.softmax = Softmax(dim=1)
        self.dropout = Dropout(0.2)
        
    def forward(self, X):
        X = self.hidden1(X)
        X = self.dropout(X)
        X = self.activation(X)
        X = self.hidden2(X)
        X = self.dropout(X)
        X = self.activation(X)
        X = self.hidden3(X)
        X = self.softmax(X)
        return X
    
if __name__ == '__main__':
    train_X = pd.read_csv('./data/train_X.csv', encoding='utf-8', index_col=0)
    train_X = torch.tensor(train_X.values).float()
    
    train_Y = pd.read_csv('./data/train_Y.csv', encoding='utf-8', index_col=0)
    train_Y = torch.tensor(train_Y.iloc[:, 0])
    
    model = DNN()
    criterion = CrossEntropyLoss()
    #optimizer = Adam(model.parameters(), lr=0.2)
    optimizer  = SGD(model.parameters(), lr=0.5)
    max_epoch = 2000
    for epoch in range(max_epoch):
        optimizer.zero_grad()
        pred_Y = model(train_X)
        loss = criterion(pred_Y, train_Y)
        loss.backward()
        optimizer.step()
        
        if not (epoch + 1) % 50:
            with torch.no_grad():
                pred = model(train_X)
                loss = criterion(pred, train_Y)
                print('epoch : {}'.format(epoch + 1), end=' | ')
                print('train_loss : {}'.format(loss.item()), end=' | ')
                valid_loss, _ = validate(model, criterion)
                print('validation_loss: {}'.format(valid_loss))
    
    with torch.no_grad():
        out = model(train_X)
        out = out.to('cpu').detach().numpy().copy()
        pred = np.argmax(out, axis=1)
        
        print('train data :', accuracy_score(train_Y, pred))
        
        test_X = pd.read_csv('./data/test_X.csv', encoding='utf-8', index_col=0)
        test_X = torch.tensor(test_X.values).float()
        
        test_Y = pd.read_csv('./data/test_Y.csv', encoding='utf-8', index_col=0)
        testn_Y = torch.tensor(test_Y.iloc[:, 0])
        
        out = model(test_X)
        out = out.to('cpu').detach().numpy().copy()
        pred = np.argmax(out, axis=1)
        
        print('test data :', accuracy_score(test_Y, pred))