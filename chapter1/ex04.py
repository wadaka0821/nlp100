import re

text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
uni = {1, 5, 6, 7, 8, 9, 15, 16, 19}
word_list = re.split(r'[,\.]*\s|\.', text)[:-1:]
element_dict:dict[str, int] = dict()
for i, word in enumerate(word_list, 1):
    if i in uni:
        element_dict[word[0]] = i
    else:
        element_dict[word[0:2]] = i
print(element_dict)