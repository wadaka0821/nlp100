from fileinput import filename


from ex10 import load

def tab_to_space(text:str) -> str:
    return text.replace('\t', ' ')

if __name__ == '__main__':
    filename = 'popular-names.txt'
    text = load(filename)
    print(tab_to_space(text))

# cat popular-names.txt | tr '\t' ' '