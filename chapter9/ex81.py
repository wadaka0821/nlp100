import numpy as np
import torch
from torch.nn import Linear, RNN, Module, Softmax
import pickle

from ex80 import vectorize

class MyRNN(Module):
    def __init__(self, embedding_dim=300, hidden_dim=10, bidirectional=False, num_layers=1) -> None:
        super(MyRNN, self).__init__()
        self.embedding_dim = embedding_dim
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        self.D = 2 if bidirectional else 1
        
        self.rnn = RNN(embedding_dim, hidden_dim, nonlinearity='relu', bidirectional=bidirectional, num_layers=num_layers)
        self.linear = Linear(self.D*self.num_layers*hidden_dim, 4)
        self.softmax = Softmax(dim=1)
        
    def forward(self, X):
        batch_size = X.shape[1]
        h0 = torch.zeros(self.D * self.num_layers, batch_size, self.hidden_dim)
        _, hn = self.rnn(X, h0)
        hn = torch.flatten(torch.swapaxes(hn, 0, 1))
        output = self.linear(torch.reshape(hn, (batch_size, -1)))
        output = self.softmax(output)
        return output
    
if __name__ == '__main__':
    vocab = None
    with open('vocab.pickle', 'rb') as f:
        vocab = pickle.load(f)
        
    text = 'hello, good moring.'
    vec = vectorize(text, vocab)
    vec = torch.from_numpy(vec.reshape((vec.shape[0], 1, vec.shape[1]))).float()
    vec = torch.concat([vec, torch.zeros(vec.shape[0], 9, vec.shape[2])], dim=1)
    
    rnn = MyRNN()
    output = rnn(vec)
    print(output)
    print(output.shape)
    