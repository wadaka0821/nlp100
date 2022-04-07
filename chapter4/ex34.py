from ex30 import load_mecab

if __name__ == '__main__':
    filename = 'neko.txt.mecab'
    tokens = load_mecab(filename)
    norms:list[str] = list()
    for token in tokens:
        if token['pos'] == '名詞':
            norms.append(token['surface'])
        else:
            if len(norms) > 1:
                print(''.join(norms))
                norms = list()