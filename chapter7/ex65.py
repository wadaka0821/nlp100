if __name__ == '__main__':
    filename = 'questions-words-out.txt'
    sem, syn = list(), list()
    with open(filename, 'r', encoding='utf-8') as f:
        l = None
        for line in f:
            words = line.replace('\n', '').split()
            if ':' == line[0]:
                if 'gram' in line:
                    l = syn
                else:
                    l = sem
                continue
            if words[-2] == words[-3]:
                l.append(1)
            else:
                l.append(0)
    print('意味的アナロジー正解率 :', sum(sem) / len(sem))
    print('文法的アナロジー正解率 :', sum(syn) / len(syn))