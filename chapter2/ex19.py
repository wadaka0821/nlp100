from collections import Counter
from ex10 import load
from ex12 import extract_cols

if __name__ == '__main__':
    filename = 'popular-names.txt'
    text = load(filename)
    col1 = extract_cols(text, [0])[0]
    count = Counter(col1)
    count_list = [[key, value] for key, value in count.items()]
    sorted_count_list = sorted(count_list, key=lambda x:x[1], reverse=True)
    print(sorted_count_list)