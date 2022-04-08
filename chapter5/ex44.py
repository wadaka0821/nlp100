from graphviz import Digraph

from ex41 import get_chunks
from ex42 import search

if __name__ == '__main__':
    filename = 'ai.ja.txt.parsed'
    all_chunks = get_chunks(filename)
    
    for i, chunks in enumerate(all_chunks):
        G = Digraph(filename='kakari/kakari-'+str(i), format='png')
        G.attr('node', shape='circle')
        for chunk in chunks:
            dst = chunk.get_dst()
            dst_phrase_idx = search(dst, chunks)
            if dst_phrase_idx == -1:
                continue
            src = ''.join([i.get_surface() for i in chunk.get_morphs() if i.get_pos() != '記号'])
            dst = ''.join([i.get_surface() for i in chunks[dst_phrase_idx].get_morphs() if i.get_pos() != '記号'])
            G.edge(src, dst)
        
        G.render()
