text1 = "パトカー"
text2 = "タクシー"
text_concat = ''.join([text1[i] + text2[i] for i in range(len(text1))])
print(text_concat)