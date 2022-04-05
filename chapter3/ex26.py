import re
from copy import deepcopy
from ex21 import load_json
from ex25 import get_templete

def remove_enphasis(templates:dict[str, str]) -> dict[str, str]:
    removed_templates = deepcopy(templates)
    for field, value in removed_templates.items():
        value = re.sub(r'\'{5,5}(.+)\'{5,5}', '\\1', value)
        value = re.sub(r'\'{3,3}(.+)\'{3,3}', '\\1', value)
        value = re.sub(r'\'{2,2}(.+)\'{2,2}', '\\1', value)
        removed_templates[field] = value
    return removed_templates

if __name__ == '__main__':
    filename = 'wiki-uk.json'
    text = load_json(filename)['text']
    templates = get_templete('基礎情報 国', text)
    removed_templates = remove_enphasis(templates)
    print(removed_templates)