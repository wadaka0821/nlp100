# skip
from ex71 import SimpleNN
import pandas as pd
import numpy as np
import torch
from torch.nn import CrossEntropyLoss
from torch.optim import SGD
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

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
    train_loss, train_acc = list(), list()
    valid_loss, valid_acc = list(), list()
    for epoch in range(max_epoch):
        optimizer.zero_grad()
        
        pred = simple_nn(train_X)
        loss = criterion(pred, train_Y)
        loss.backward()
            
        optimizer.step()
        
        with torch.no_grad():
            pred = simple_nn(train_X)
            loss = criterion(pred, train_Y)
            
            class_pred = np.argmax(pred.detach().numpy().copy(), axis=1)
            train_loss.append(loss.item())
            train_acc.append(accuracy_score(train_Y, class_pred))
            
            valid, acc = validate(simple_nn, criterion)
            
            valid_loss.append(valid.item())
            valid_acc.append(acc)
        if not (epoch + 1) % 50:
            print(epoch+1)
    plt.plot(list(range(1, len(train_loss)+1)), train_loss, label='train')
    plt.plot(list(range(1, len(valid_loss)+1)), valid_loss, label='valid')
    plt.title('loss')
    plt.legend()
    plt.show()
    
    plt.plot(list(range(1, len(train_acc)+1)), train_acc, label='train')
    plt.plot(list(range(1, len(valid_acc)+1)), valid_acc, label='valid')
    plt.title('accuracy')
    plt.legend()
    plt.show()
        
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
        

    