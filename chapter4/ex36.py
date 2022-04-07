from ex30 import load_mecab

from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

if __name__ == '__main__':
    filename = 'neko.txt.mecab'
    tokens = load_mecab(filename)
    tokens = [token['surface'] for token in tokens]
    count = [[key, value] for key, value in Counter(tokens).items()]
    count = sorted(count, key=lambda x:x[1], reverse=True)[:10]
    x = [i[0] for i in count]
    y = [i[1] for i in count]
    plt.bar(x, y)
    plt.show()