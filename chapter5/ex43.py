from ex41 import get_chunks
from ex42 import search

if __name__ == '__main__':
    filename = 'ai.ja.txt.parsed'
    all_chunks = get_chunks(filename)
    for chunks in all_chunks:
        for chunk in chunks:
            dst = chunk.get_dst()
            dst_phrase_idx = search(dst, chunks)
            if dst_phrase_idx == -1:
                continue
            if '名詞' not in set([i.get_pos() for i in chunk.get_morphs()]):
                continue
            if '動詞' not in set([i.get_pos() for i in chunks[dst_phrase_idx].get_morphs()]):
                continue
            src = ''.join([i.get_surface() for i in chunk.get_morphs() if i.get_pos() != '記号'])
            dst = ''.join([i.get_surface() for i in chunks[dst_phrase_idx].get_morphs() if i.get_pos() != '記号'])
            print('{}\t{}'.format(src, dst))