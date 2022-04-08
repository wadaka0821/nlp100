from ex40 import Morph
from ex41 import Chunk, get_chunks
from ex42 import search

def search_pos(pos:str, chunk:Chunk, all:bool=False, index:bool=False) -> list[Morph|int]:
    ans:list[Morph|int] = list()
    morphs = chunk.get_morphs()
    for i in range(len(morphs)):
        if morphs[i].get_pos() == pos:
            if index:
                ans.append(i)
            else:
                ans.append(morphs[i])
        if ans and not all:
            break
    return ans

if __name__ == '__main__':
    filename = 'ai.ja.txt.parsed'
    all_chunks = get_chunks(filename)
    
    for chunks in all_chunks:
        for chunk in chunks:
            verb = search_pos('動詞', chunk)
            if not verb:
                continue
            if isinstance(verb[0], Morph):
                verb = verb[0].get_base()
            srcs = chunk.get_srcs()
            particles_out:list[list[str]] = list()
            for src in srcs:
                src_idx = search(src, chunks)
                if src_idx == -1:
                    continue
                src_chunk = chunks[src_idx]
                particles = search_pos('助詞', src_chunk, True, True)
                if not particles:
                    continue
                
                for particle in particles:
                    if isinstance(particle, int):
                        if not src_chunk.get_morphs()[particle].get_surface() == 'を':
                            continue
                        if src_chunk.get_morphs()[particle-1].get_pos() == '名詞' and src_chunk.get_morphs()[particle-1].get_pos1() == 'サ変接続':
                            phrase = src_chunk.get_morphs()[particle-1].get_surface() + 'を'
                            particles_out.append([src_chunk.get_morphs()[particle].get_surface(), phrase])
            if particles_out:
               print('{}\t{}\t{}'.format(verb, ' '.join([i[0] for i in particles_out]), ' '.join([i[1] for i in particles_out])))
                        
    