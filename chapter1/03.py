import re

text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
word_list = re.split(r'[,\.]*\s|\.', text)[:-1:]
word_count = [len(word) for word in word_list]
print(word_count)