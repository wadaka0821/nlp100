import re
from ex21 import load_json

def get_templete(templete:str, text:str) -> dict[str,str]:
    #print(r'\{\{' + templete + r'(\n)*(\|([^=]+)=(\{\{(.+)\}\}|[^=]+))+\}\}')
    #match = re.search(r'\{\{' + templete + r'(\n)*(\|([^=]+)=(\{\{(.+)\}\}|[^=]+))+\}\}', text)
    match = re.search(r'\{\{' + templete + r'(\n)*(.+)\}\}', text)
    print(match)
    file = {'test':'val'}
    return file

if __name__ == '__main__':
    filename = 'wiki-uk.json'
    text = load_json(filename)['text']
    print(re.findall(r'基礎情報 国(\n)*(\|[^=\|]+=[^=\|]+)+', text))
    print(re.findall(r'\{\{基礎情報 国(\n)*(.+)\}\}', text))
    get_templete('基本情報 国', text)