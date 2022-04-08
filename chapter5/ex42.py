from ex41 import Chunk, get_chunks

def search(phrase_idx:int, chunks:list[Chunk]) -> int:
    for i in range(len(chunks)):
        if phrase_idx == chunks[i].get_idx():
            return i
    return -1

if __name__ == '__main__':
    filename = 'ai.ja.txt.parsed'
    all_chunks = get_chunks(filename)
    for chunks in all_chunks:
        for chunk in chunks:
            dst = chunk.get_dst()
            dst_phrase_idx = search(dst, chunks)
            if dst_phrase_idx == -1:
                continue
            src = ''.join([i.get_surface() for i in chunk.get_morphs() if i.get_pos() != '記号'])
            dst = ''.join([i.get_surface() for i in chunks[dst_phrase_idx].get_morphs() if i.get_pos() != '記号'])
            print('{}\t{}'.format(src, dst))