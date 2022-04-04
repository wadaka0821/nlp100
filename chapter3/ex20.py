import json

if __name__ == '__main__':
    filename = 'jawiki-country.json'
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            if data['title'] == 'イギリス':
                with open('wiki-uk.json', 'w') as f:
                    json.dump(data, f)
                break