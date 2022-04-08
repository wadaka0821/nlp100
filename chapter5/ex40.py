
class Morph():
    def __init__(self, morph_text:str) -> None:
        self.surface:str = ''
        self.base:str = ''
        self.pos:str = ''
        self.pos1:str = ''
        
        self.parse(morph_text)
    
    def parse(self, morph_text:str) -> None:
        self.surface, info = morph_text.split('\t')
        info = info.split(',')
        self.base = info[6]
        self.pos = info[0]
        self.pos1 = info[1]
        
    def get_surface(self) -> str:
        return self.surface
    
    def get_pos(self) -> str:
        return self.pos
    
    def get_base(self) -> str:
        return self.base
    
    def get_pos1(self) -> str:
        return self.pos1
        
    def __str__(self):
        return '表層系:{} 基本形:{} 品詞:{} 品詞細分類1:{}'.format(self.surface, self.base, self.pos, self.pos1)
        
if __name__ == '__main__':
    filename = 'ai.ja.txt.parsed'
    text:list[Morph] = list()
    with open(filename, 'r', encoding='utf-8') as f:
        for _ in range(4):
            f.readline()
        for line in f:
            if line == 'EOS\n':
                break
            elif line[0] != '*':
                text.append(Morph(line))
    for i in text:
        print(i)