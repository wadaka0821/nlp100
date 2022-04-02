def make_text(hour:int, topic:str, contents:str|int|float) -> str:
    return '{}時の{}は{}'.format(hour, topic,contents)

if __name__ == '__main__':
    print(make_text(12, '天気', 22.4))