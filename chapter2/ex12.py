from ex10 import load

def save(filename:str, texts:list[str]) -> None:
    with open(filename, 'w') as f:
        f.writelines(texts)

def extract_cols(text:str, cols:list[int]) -> dict[int, list[str]]:
    texts = [line.split('\t') for line in text.split('\n')]
    num_cols = len(texts[0])
    res:dict[int, list[str]] = {i:list() for i in cols if 0 <= i < num_cols}
    for line in texts:
        if len(line) < num_cols:
            continue
        for col in res.keys():
            res[col].append(line[col]+'\n')
    return res

if __name__ == '__main__':
    filename = 'popular-names.txt'
    text = load(filename)
    texts_dict = extract_cols(text, cols=[0, 1])
    save('col1.txt', texts_dict[0])
    save('col2.txt', texts_dict[1])