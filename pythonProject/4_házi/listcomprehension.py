#!/usr/bin/env python3


def main():
    inp = ['auto', 'villamos', 'metro']
    result = [s.upper() + '!' for s in inp]
    print(result)

    inp = ['aladar', 'bela', 'cecil']
    result = [s.capitalize() for s in inp]
    print(result)

    result = [0 for n in range(1, 10 + 1)]
    print(result)

    inp = list(range(1, 10 + 1))
    result = [i + i for i in inp]
    print(result)

    inp = [str(n) for n in range(1, 10 + 1)]
    result = [int(i) for i in inp]
    print(result)

    inp = [n for n in "1234567"]
    result = [int(i) for i in inp]
    print(result)

    inp = [len(n) for n in "The quick brown fox jumps over the lazy dog".split()]
    print(inp)

    inp = [n[0] for n in "python is an awesome language".split()]
    print(inp)

    inp = [(n, len(n)) for n in 'The quick brown fox jumps over the lazy dog'.split()]
    print(inp)

    inp = [n for n in range(0, 10, 2)]
    print(inp)

    inp = [n * n for n in range(0, 20) if (n * n) % 2 == 0]
    print(inp)

    inp = [n * n for n in range(0, 20) if str(n * n)[-1] == '4']
    print(inp)

    outp = ""
    inp = [chr(n) for n in range(ord('A'), ord('Z')+1)]
    print(outp.join(inp))

    inp = [n.strip() for n in [' apple ', ' banana ', ' kiwi']]
    print(inp)

    outp = ""
    inp = [str(n) for n in [1, 0, 1, 1, 0, 1, 0, 0]]
    print(outp.join(inp))


if __name__ == '__main__':
    main()
