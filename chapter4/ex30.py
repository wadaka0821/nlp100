
def load_mecab(filename:str) -> list[dict[str, str]]:
    res:list[dict[str, str]] = list()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            token = line.split('\t')
            if len(token) != 2:
                continue
            t  = {'surface':token[0]}
            info = token[1].split(',')
            t['base'] = info[6]
            t['pos'] = info[0]
            t['pos1'] = info[1]
            res.append(t)
    return res

if __name__ == '__main__':
    filename = 'neko.txt.mecab'
    tokens = load_mecab(filename)
    print(tokens[:4])