from ex30 import load_mecab

if __name__ == '__main__':
    filename = 'neko.txt.mecab'
    tokens = load_mecab(filename)
    for token in tokens:
        if token['pos'] == '動詞':
            print(token['base'])