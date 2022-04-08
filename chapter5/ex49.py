from ex41 import Chunk, get_chunks
from ex42 import search

def chunk_to_str(chunk:Chunk, mask:str='') -> str:
    if mask:
        return ''.join([mask if morph.get_pos() == '名詞' else morph.get_surface() for morph in chunk.get_morphs()])
    return ''.join([morph.get_surface() for morph in chunk.get_morphs()])

def get_all_path(chunks:list[Chunk], pos:str='名詞') -> list[list[int]]:
    all_path:list[list[int]] = list()
    for chunk in chunks:
        path:list[int] = [chunk.get_idx()]
        if pos not in set([i.get_pos() for i in chunk.get_morphs()]):
            continue
        while chunk.get_dst() != -1:
            dst_idx = search(chunk.get_dst(), chunks)
            if dst_idx == -1:
                break
            chunk = chunks[dst_idx]
            path.append(chunk.get_idx())
        all_path.append(path)
    return all_path

def extract_all_path(all_path:list[list[int]], chunks:list[Chunk]) -> None:
    N = len(all_path)
    for i in range(N):
        for j in range(i+1, N):
            mul = set(all_path[i]).intersection(set(all_path[j]))
            if len(mul) == len(all_path[j]):
                print(chunk_to_str(chunks[0], mask='X') + ' -> ' + ' -> '.join([chunk_to_str(chunks[idx]) if all_path[j][0] != idx else chunk_to_str(chunks[idx], mask='Y') for idx in all_path[i][1:]]))
            elif len(mul) > 0:
                merge_idx = min(mul)
                x_idx = all_path[i].index(merge_idx)
                y_idx = all_path[j].index(merge_idx)
                print(chunk_to_str(chunks[0], mask='X') + ' -> ' + ' -> '.join([chunk_to_str(chunks[idx]) for idx in all_path[i][1:x_idx]]), end=' | ')
                print(chunk_to_str(chunks[0], mask='Y') + ' -> ' + ' -> '.join([chunk_to_str(chunks[idx]) for idx in all_path[j][1:y_idx]]), end=' | ')
                print(' -> '.join([chunk_to_str(chunks[idx]) for idx in all_path[i][x_idx:]]))

if __name__ == '__main__':
    filename = 'ai.ja.txt.parsed'
    all_chunks = get_chunks(filename)
    
    for chunks in all_chunks:
        all_path = get_all_path(chunks)
        print(extract_all_path(all_path, chunks))
        