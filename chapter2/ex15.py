import sys

def tail(n:int, filename:str) -> None:
    data = ['\n' for _ in range(n)]
    with open(filename, 'r') as f:
        for line in f:
            data.append(line)
            del data[0]
    print(''.join(data), end='')

if __name__ == '__main__':
    arg = sys.argv[1]
    if not arg.isdigit():
        print('invalid argument type')
    N = int(arg)
    filename = 'popular-names.txt'
    tail(N, filename)