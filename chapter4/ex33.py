from ex30 import load_mecab

if __name__ == '__main__':
    filename = 'neko.txt.mecab'
    tokens = load_mecab(filename)
    norm = ''
    connection = False
    for token in tokens:
        if token['pos'] == '名詞':
            if norm and connection:
                print('{}の{}\n'.format(norm, token['surface']))
                norm = ''
            elif not norm and not connection:
                norm = token['surface']
            else:
                norm = ''
            connection = False
        elif norm and not connection:
            if token['surface'] == 'と':
                connection = True
        else:
            norm = ''
            connection = False
                