import re
from copy import deepcopy
from ex21 import load_json
from ex25 import get_templete
from ex26 import remove_enphasis

def remove_inner_link(templates:dict[str,str]) -> dict[str,str]:
    removed_templates = deepcopy(templates)
    for field, value in removed_templates.items():
        value = re.sub(r'\[\[([^\[\]]+)(#.+)?\|(.+)\]\]', '\\3', value)
        value = re.sub(r'\[\[([^\[\]]+)\]\]', '\\1', value)
        removed_templates[field] = value
    return removed_templates

if __name__ == '__main__':
    filename = 'wiki-uk.json'
    text = load_json(filename)['text']
    templates = get_templete('基礎情報 国', text)
    removed_templates = remove_enphasis(templates)
    removed_templates = remove_inner_link(removed_templates)
    for i, j in removed_templates.items():
        print(i, j)