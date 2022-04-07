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
    hist_data = [value for _, value in Counter(tokens).items()]
    plt.hist(hist_data, 20, (0, 150))
    plt.show()