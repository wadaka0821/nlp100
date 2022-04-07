from ex30 import load_mecab

if __name__ == '__main__':
    filename = 'neko.txt.mecab'
    tokens = load_mecab(filename)
    norm = ''
    connection = False
    for token in tokens:
        if connection:
            if token['pos'] == '名詞':
                print('{}と{}\n'.format(norm, token['surface']))
            norm = ''
            connection = False
        else:
            if token['pos'] == '名詞':
                norm = token['surface']
            elif norm and token['surface'] == 'と':
                connection = True
            elif norm:
                norm = ''