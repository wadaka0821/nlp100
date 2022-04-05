import re
from ex21 import load_json

def get_templete(templete:str, text:str) -> dict[str,str]:
    match = re.search(r'\{\{' + templete + r'(.|\n)+\n\}\}', text)
    if match:
        text = match.group()
        match = re.findall(r'\|([^=\|]+)=(.+)\n',text)
        templetes = {field:value for (field, value) in match}
        return templetes
    return dict()

if __name__ == '__main__':
    filename = 'wiki-uk.json'
    text = load_json(filename)['text']
    templates = get_templete('基礎情報 国', text)
    for i, j in templates.items():
        print(i, j)