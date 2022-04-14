import numpy as np
import torch
from torch.nn import RNN, Module
import pickle

from ex80 import vectorize

class MyRNN(Module):
    def __init__(self, embedding_dim=300, hidden_dim=10) -> None:
        super(MyRNN, self).__init__()
        self.embedding_dim = embedding_dim
        self.hidden_dim = hidden_dim
        
        self.rnn = RNN(embedding_dim, hidden_dim)
        
    def forward(self, X):
        batch_size = X.shape[1]
        h0 = torch.zeros(1, batch_size, self.hidden_dim)
        output, hn = self.rnn(X, h0)
        return output
    
if __name__ == '__main__':
    vocab = None
    with open('vocab.pickle', 'rb') as f:
        vocab = pickle.load(f)
        
    text = 'hello, good moring.'
    vec = vectorize(text, vocab)
    vec = torch.from_numpy(vec.reshape((vec.shape[0], 1, vec.shape[1]))).float()
    
    rnn = MyRNN()
    output = rnn(vec)
    print(output)
    print(output.shape)
    