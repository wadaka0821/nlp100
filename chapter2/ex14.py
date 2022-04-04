import sys

def head(n:int, filename:str) -> None:
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            print(line, end='')

if __name__ == '__main__':
    arg = sys.argv[1]
    filename = 'popular-names.txt'
    if not arg.isdigit():
        print('invalid argument type')
        sys.exit(1)
    
    N = int(arg)
    head(N, filename)