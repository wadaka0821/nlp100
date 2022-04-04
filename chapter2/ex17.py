from fileinput import filename
from ex12 import extract_cols
from ex10 import load

if __name__ == '__main__':
    filename = 'popular-names.txt'
    text = load(filename)
    col1 = extract_cols(text, [0])
    print(set(col1[0]))