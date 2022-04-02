import re

def get_n_gram(text:str, n:int, word:bool) -> list[str]:
    ngram:list[str] = list()
    if word:
        word_list = re.split(r'[,\.]*\s|\.', text)
        if text[-1] == '.':
            word_list = word_list[:-1]
        for i in range(0, len(word_list)-n+1):
            ngram.append(' '.join(word_list[i:i+n]))
    else:
        for i in range(0, len(text)-n+1):
            ngram.append(text[i:i+n])
    return ngram

if __name__ == '__main__':
    text = 'I am a NLPer'
    print(get_n_gram(text, 2, False))
    print(get_n_gram(text, 2, True))
    print(get_n_gram(text, 4, False))