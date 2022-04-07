import requests

from ex21 import load_json
from ex25 import get_templete
from ex26 import remove_enphasis
from ex27 import remove_inner_link
from ex28 import remove_tag, remove_file

if __name__ == '__main__':
    filename = 'wiki-uk.json'
    text = load_json(filename)['text']
    templates = get_templete('基礎情報 国', text)
    removed_templates = remove_enphasis(templates)
    removed_templates = remove_inner_link(removed_templates)
    removed_templates = remove_tag(removed_templates)
    removed_templates = remove_file(removed_templates)
    if '国旗画像 ' in removed_templates:
        img = removed_templates['国旗画像 ']
        print(img)
        
        session = requests.Session()
        
        URL = 'https://ja.wikipedia.org/w/api.php'
        
        PARAMS = {
            'action':'query',
            'format':'json',
            'prop':'imageinfo',
            'titles':'File:'+img
        }
        
        res = session.get(url=URL, params=PARAMS)
        data = res.json()
        
        print(data)