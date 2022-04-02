import random

def typoglycemia(text:str) -> str:
    start = text[0]
    shuffled_text = ''
    end = text[-1]
    if (len(text) <= 4) :
        return text
    else:
        letter_list = list(text[1:-1])
        random.shuffle(letter_list)
        shuffled_text = ''.join(letter_list)
        return start + shuffled_text + end

if __name__ == '__main__':
    text = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
    print(typoglycemia(text))