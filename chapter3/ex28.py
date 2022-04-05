import re
from copy import deepcopy
from ex21 import load_json
from ex25 import get_templete
from ex26 import remove_enphasis
from ex27 import remove_inner_link

def remove_tag(templates:dict[str,str]) -> dict[str,str]:
    removed_templates = deepcopy(templates)
    for field, value in removed_templates.items():
        value = re.sub(r'<[^<>]+/>', '', value)
        value = re.sub(r'<[^<>]+>.+</[^<>]+>', '', value)
        value = re.sub(r'<[^<>]+>.*', '', value)
        removed_templates[field] = value
    return removed_templates

def remove_file(templates:dict[str,str]) -> dict[str,str]:
    removed_templates = deepcopy(templates)
    for field, value in templates.items():
        print(value)
        value = re.sub(r'\[ファイル:(.+)\|.*', '\\1', value)
        print(value)
    return removed_templates

def remove_lang(templates:dict[str,str]) -> dict[str,str]:
    removed_templates = deepcopy(templates)
    return removed_templates

if __name__ == '__main__':
    filename = 'wiki-uk.json'
    text = load_json(filename)['text']
    templates = get_templete('基礎情報 国', text)
    removed_templates = remove_enphasis(templates)
    removed_templates = remove_inner_link(removed_templates)
    removed_templates = remove_tag(removed_templates)
    removed_templates = remove_file(removed_templates)
    print(removed_templates)