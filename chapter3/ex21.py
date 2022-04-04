from cgitb import text
import json
import re
from typing import Any

if __name__ == '__main__':
    filename = 'wiki-uk.json'
    json_data:dict[Any, Any]
    with open(filename, 'r') as f:
        json_data = json.load(f)
    text = json_data['text']
    
    match = re.findall(r'Category:([^\|\[\]]+)', text)
    print(match)