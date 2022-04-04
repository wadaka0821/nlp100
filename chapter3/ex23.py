import re
import json

def load_json(filename:str) -> dict[str, str]:
    with open(filename, 'r') as f:
        data = json.load(f)
        return data

def get_sections(text:str) -> list[dict[str, str|int]]:
    res:list[dict[str, str|int]] = list()
    match = re.findall(r'(={2,})([^=]+)(={2,})', text)
    for section in match:
        res.append({'name':section[1], 'level':len(section[0])-1})
    return res

if __name__ == '__main__':
    filename = 'wiki-uk.json'
    text = load_json(filename)['text']
    sections = get_sections(text)
    print(sections)