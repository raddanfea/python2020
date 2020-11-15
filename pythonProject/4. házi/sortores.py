#!/usr/bin/env python3
import sys
import random as r

UPTO = 100


def main():
    for i in range(UPTO):
        if i % 10 == 0 and i != 0:
            print('\n', end="")
        print(r.randint(0, 9), end="")
    print()

if __name__ == '__main__':
    main()
