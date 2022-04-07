from ex30 import load_mecab

from collections import Counter

if __name__ == '__main__':
    filename = 'neko.txt.mecab'
    tokens = load_mecab(filename)
    tokens = [token['surface'] for token in tokens]
    count = [[key, value] for key, value in Counter(tokens).items()]
    count = sorted(count, key=lambda x:x[1], reverse=True)
    print('the number of vocabrary :', len(count))
    print(count[:10])