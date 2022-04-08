from ex40 import Morph
from ex41 import Chunk, get_chunks
from ex42 import search

def search_pos(pos:str, chunk:Chunk, all:bool=False) -> list[Morph]:
    ans:list[Morph] = list()
    morphs = chunk.get_morphs()
    for i in range(len(morphs)):
        if morphs[i].get_pos() == pos:
            ans.append(morphs[i])
        if ans and not all:
            break
    return ans

def save(filename:str, text:str):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    filename = 'ai.ja.txt.parsed'
    all_chunks = get_chunks(filename)
    pattern:dict[str, list[list[str]]] = dict()
    
    for chunks in all_chunks:
        for chunk in chunks:
            verb = search_pos('動詞', chunk)
            if not verb:
                continue
            verb = verb[0].get_base()
            srcs = chunk.get_srcs()
            for src in srcs:
                src_idx = search(src, chunks)
                if src_idx == -1:
                    continue
                src_chunk = chunks[src_idx]
                particles = search_pos('助詞', src_chunk, True)
                if not particles:
                    continue
                phrase = ''.join([morph.get_surface() for morph in src_chunk.get_morphs()])
                particles = [[particle.get_surface(), phrase] for particle in particles]
                if verb in pattern:
                    pattern[verb] += particles
                else:
                    pattern[verb] = particles
    
    for verb, particles in pattern.items():
        particles = sorted(particles, key=lambda x:x[0])
        save('frame.txt', '{}\t{}\t{}\n'.format(verb, ' '.join([particle[0] for particle in particles]), ' '.join([particle[1] for particle in particles])))