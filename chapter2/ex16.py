from ex12 import save

def split(filename:str, n:int) -> list[list[str]]:
    splited_text:list[list[str]] = list()
    texts:list[str] = list()
    num_line:int
    with open(filename, 'r') as f:
        for line in f:
            texts.append(line)
        num_line = int(len(texts)/n)
    for i in range(n):
        splited_text.append(texts[num_line*i:num_line*(i+1)])
    splited_text[-1] += texts[num_line*n:]
    return splited_text

if __name__ == '__main__':
    filename = 'popular-names.txt'
    n = 5
    splited_text = split(filename, n)
    for i in range(n):
        save('splited_text_'+str(i)+'.txt', splited_text[i])