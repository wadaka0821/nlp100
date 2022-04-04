from ex10 import load
from ex12 import save

def text_to_table(text:str) -> list[list[str]]:
    table:list[list[str]] = list()
    texts = [line.split('\t') for line in text.split('\n')]
    num_cols = len(texts[0])
    for line in texts:
        if len(line) < num_cols:
            continue
        table.append(line)
    return table

if __name__ == '__main__':
    filename = 'popular-names.txt'
    text = load(filename)
    table = text_to_table(text)
    sorted_table = sorted(table, key=lambda x:x[2], reverse=True)
    sorted_texts = ['\t'.join(line)+'\n' for line in sorted_table]
    save('sorted-popular-names.txt', sorted_texts)