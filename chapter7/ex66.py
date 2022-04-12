from ex60 import load_from_pickle
import csv
import numpy as np

if __name__ == '__main__':
    filename = './dic/word2vec.pickle'
    word2vec = load_from_pickle(filename)
    man, model = list(), list()
    with open('combined.csv', 'r', encoding='utf-8') as f:
        f.readline()
        reader = csv.reader(f)
        for line in reader:
            man.append(float(line[2]))
            model.append(word2vec.similarity(line[0], line[1]))
    N = len(man)
    man, model = np.array(man), np.array(model)
    print(1 - (6 * sum((man - model)**2) / (N*(N**2 - 1))))