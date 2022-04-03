def wc(text:str) -> int:
    return len(text.split('\n')) - 1

def load(filename:str) -> str:
    with open(filename, 'r') as f:
        return f.read()

if __name__ == '__main__':
    filename = 'popular-names.txt'
    text = load(filename)
    print(wc(text))

# wc popular-names.txt