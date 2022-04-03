from ex10 import load
from ex12 import save

def concat(text1:str, text2:str) -> list[str]:
    text1_split = text1.split('\n')
    text2_split = text2.split('\n')
    res:list[str] = list()
    for line1, line2 in zip(text1_split, text2_split):
        res.append(line1 + '\t' + line2 + '\n')
    return res

if __name__ == '__main__':
    text1_name = 'col1.txt'
    text2_name = 'col2.txt'
    text1 = load(text1_name)
    text2 = load(text2_name)
    concat_text = concat(text1, text2)
    save('concat_text.txt', concat_text)