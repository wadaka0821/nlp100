import numpy as np
import torch
from torch.nn import Linear, RNN, Module, Softmax
import pickle

from ex80 import vectorize

class MyRNN(Module):
    def __init__(self, embedding_dim=300, hidden_dim=10, batch_size=10) -> None:
        super(MyRNN, self).__init__()
        self.embedding_dim = embedding_dim
        self.hidden_dim = hidden_dim
        self.batch_size = batch_size
        
        self.rnn = RNN(embedding_dim, hidden_dim)
        self.linear = Linear(hidden_dim, 4)
        self.softmax = Softmax(dim=1)
        
    def forward(self, X):
        h0 = torch.zeros(1, self.batch_size, self.hidden_dim)
        _, hn = self.rnn(X, h0)
        output = self.linear(hn.reshape(hn.shape[1], -1))
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
    