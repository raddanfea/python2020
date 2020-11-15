#!/usr/bin/env python3

def main():
    x = input('Páros szám:')
    print(str(diamond(x)))


def diamond(x):
    if int(x) % 2 == 0:
        return 'Csak páratlan számok!'
    else:
        n = ''
        for i in range(1, int(x)+1, 2):
            subs = '*' * i
            n = n + subs.center(int(x)+1) + '\n'
        for i in reversed(range(1, int(x),2)):
            subs = '*' * i
            n = n + subs.center(int(x)+1) + '\n'
        n.strip()
        return n


if __name__ == '__main__':
    main()
