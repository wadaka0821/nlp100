from fileinput import filename
import re

from ex40 import Morph

class Chunk():
    def __init__(self, text:list[str]) -> None:
        self.morphs:list[Morph] = list()
        self.idx:int = -1
        self.dst:int = -1
        self.srcs:list[int] = list()
        self.parse(text)
        
    def parse(self, text:list[str]) -> None:
        match = re.findall(r'-?\d+', text[0].split('D')[0])
        self.idx = int(match[0])
        self.dst = int(match[1])
        for line in text[1:]:
            self.morphs.append(Morph(line))
        
    def set_srcs(self, srcs:list[int]) -> None:
        self.srcs = srcs
        
    def get_srcs(self) -> list[int]:
        return self.srcs
        
    def get_idx(self) -> int:
        return self.idx
    
    def get_dst(self) -> int:
        return self.dst
    
    def get_morphs(self) -> list[Morph]:
        return self.morphs
        
    def get_rev_src(self) -> tuple[int, int]:
        return (self.dst, self.idx)
    
    def __str__(self) -> str:
        return '文節id:{} 係り先id:{} 係り元id:{}\n形態素\n{}'.format(self.idx,
                                                                      self.dst,
                                                                      self.srcs,
                                                                      '\n'.join([str(i) for i in self.morphs]))
        
def get_chunks(filename:str) -> list[list[Chunk]]:
    all_chunks:list[list[Chunk]] = list()
    srcs:dict[int, list[int]] = dict()
    with open(filename, 'r', encoding='utf-8') as f:
        chunks:list[Chunk] = list()
        chunk:list[str] = list()
        for line in f:
            if line == 'EOS\n':
                if chunk:
                    chunks.append(Chunk(chunk))
                    for c in chunks:
                        if c.get_idx() in srcs:
                            c.set_srcs(srcs[c.get_idx()])
                    srcs = dict()
                    all_chunks.append(chunks)
                    chunks = list()
                    chunk = list()
                continue
            elif line[0] == '*':
                if chunk:
                    new_chunk = Chunk(chunk)
                    chunks.append(new_chunk)
                    chunk = [line]
                    src = new_chunk.get_rev_src()
                    if src[0] == -1 or src[1] == -1:
                        continue
                    if src[0] in srcs:
                        srcs[src[0]].append(src[1])
                    else:
                        srcs[src[0]] = [src[1]]
                else:
                    chunk.append(line)
            else:
                chunk.append(line)
    
    return all_chunks
        
if __name__ == '__main__':
    filename = 'ai.ja.txt.parsed'
    all_chunks = get_chunks(filename)
    for chunks in all_chunks:
        for chunk in chunks:
            print('-'*60)
            print(chunk)
        print()