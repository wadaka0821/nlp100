from ex60 import load_from_pickle

def analogy(model, base, pos, neg):
    top = model.most_similar(model[base] - model[neg] + model[pos], topn=1)[0]
    return top

def experiment(model, filename='questions-words.txt', filename_out='questions-words-out.txt'):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.replace('\n', '').split()
            if len(words) != 4:
                with open(filename_out, 'a') as f:
                    f.write(line)
                continue
            top = analogy(model, words[1], words[2], words[0])
            with open(filename_out, 'a') as f:
                f.write(' '.join(words + [top[0], str(top[1])]) + '\n')
            

if __name__ == '__main__':
    filename = './dic/word2vec.pickle'
    word2vec = load_from_pickle(filename)
    experiment(word2vec)