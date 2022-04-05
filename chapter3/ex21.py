from fileinput import filename
import re
from ex23 import load_json

def get_category_rows(text:str) -> list[str]:
    res:list[str] = list()
    for line in text.split('\n'):
        match = re.search(r'Category:([^\|\[\]]+)', line)
        if match:
            res.append(line)
    return res

if __name__ == '__main__':
    filename = 'wiki-uk.json'
    text = load_json(filename)['text']
    print(get_category_rows(text))