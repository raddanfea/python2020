#!/usr/bin/env python3
import sys


def main():

    if len(sys.argv) != 2:
        print("1 argument expected.")
    else:
        c = int(sys.argv[1])
        l = [False] * c

        for i, k in enumerate(l, 1):
            for i2, k2 in enumerate(l, 1):
                if i2 % i == 0:
                    l[i2-1] = not k2

        openCells = []
        for i, val in enumerate(l, 1):
            if val:
                openCells.append(str(i))

        print("Number of cells open:", len(openCells))
        print("".join(openCells))


if __name__ == '__main__':
    main()
