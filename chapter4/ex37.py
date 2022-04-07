from ex30 import load_mecab

import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

def get_co_occurance(target:str, source:list[str], window:int=1) -> dict[str,int]:
    co_occurance:dict[str, int] = dict()
    for i in range(len(source)):
        if source[i] == target:
            for j in range(1, min(window, i)+1):
                if source[i-j] in co_occurance:
                    co_occurance[source[i-j]] += 1
                else:
                    co_occurance[source[i-j]] = 1
            for j in range(1, min(window+1, len(source)-i)):
                if source[i+j] in co_occurance:
                    co_occurance[source[i+j]] += 1
                else:
                    co_occurance[source[i+j]] = 1
    return co_occurance

if __name__ == '__main__':
    filename = 'neko.txt.mecab'
    tokens = load_mecab(filename)
    tokens = [token['surface'] for token in tokens]
    co_occurance = get_co_occurance('猫', tokens, window=2)
    top10_co_occurance = sorted([[key, value] for key, value in co_occurance.items()], key=lambda x:x[1], reverse=True)[:10]
    x = [i[0] for i in top10_co_occurance]
    y = [i[1] for i in top10_co_occurance]
    plt.bar(x, y)
    plt.show()