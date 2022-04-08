from ex41 import Chunk, get_chunks
from ex42 import search

def chunk_to_str(chunk:Chunk) -> str:
    return ''.join([morph.get_surface() for morph in chunk.get_morphs()])

def get_path(chunk:Chunk, chunks:list[Chunk]) -> list[str]:
    path = [chunk_to_str(chunk)]
    head = chunk
    while head.get_dst() != -1:
        dst_idx = search(head.get_dst(), chunks)
        if dst_idx == -1:
            path.append('error')
        head = chunks[dst_idx]
        path.append(chunk_to_str(head))
    return path

if __name__ == '__main__':
    filename = 'ai.ja.txt.parsed'
    all_chunks = get_chunks(filename)
    
    for chunks in all_chunks:
        for chunk in chunks:
            if '名詞' in set([morph.get_pos() for morph in chunk.get_morphs()]):
                path = get_path(chunk, chunks)
                print(' -> '.join(path))