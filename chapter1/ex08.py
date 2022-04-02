def to_cipher(text:str) -> str:
    code = ''
    for letter in text:
        if letter.isascii() and 96 < ord(letter) < 123:
            code += str(219 - ord(letter))
        else:
            code += letter
    return code

def from_cipher(code:str) -> str:
    text = ''
    num = ''
    for letter in code:
        if letter.isdigit():
            num += letter
            if len(num) >= 2:
                ascii = int(num)
                if 96 < ascii < 123:
                    text += chr(219-ascii)
                    num = ''
        else:
            text += letter
    return text

if __name__ == '__main__':
    text = 'Hello, today is a nice day, right?'
    encoded_text = to_cipher(text)
    decoded_text = from_cipher(encoded_text)
    print(encoded_text)
    print(decoded_text)