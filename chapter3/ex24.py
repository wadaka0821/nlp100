import re
from ex21 import load_json

def get_files(text:str) -> list[str]:
    match = re.findall(r'\[\[(ファイル|File):([^|]+).*\]\]', text)
    files = [i[1] for i in match]
    return files

if __name__ == '__main__':
    filename = 'wiki-uk.json'
    text = load_json(filename)['text']
    print(get_files(text))