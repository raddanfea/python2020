import sys


def main():
    # A meghívási kódot olvasva eldönti hogy a-z fájlnévről futtatjuk-e.
    output = ''.join([chr(n) for n in range(ord('a'), ord('z') + 1)])
    print(sys.argv[0])
    if sys.argv[0].endswith("a-z.py"):
        print(output)
    else:
        print(output[::-1])


if __name__ == '__main__':
    main()
