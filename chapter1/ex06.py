from ex05 import get_n_gram

if __name__ == '__main__':
    text1 = 'paraparaparadise'
    text2 = 'paragraph'
    
    text1_set = set(get_n_gram(text1, 2, False))
    text2_set = set(get_n_gram(text2, 2, False))
    
    print('X or Y = {}'.format(text1_set.union(text2_set)))
    print('X and Y = {}'.format(text1_set.intersection(text2_set)))
    print('X - Y = {}'.format(text1_set - text2_set))
    print('\'se\' in X = {}'.format('se' in text1_set))
    print('\'se\' in Y = {}'.format('se' in text2_set))