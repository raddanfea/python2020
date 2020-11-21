#!/usr/bin/env python3
import itertools
import sys
import numpy


def main():
    if len(sys.argv) != 1:
        print("Expected no argument.")
    else:
        for subset in itertools.combinations(range(1, 46), 6):
            if sum(subset) == 90 and numpy.prod(subset) == 996300:
                print(subset)
                return 0
        print("Not found.")


if __name__ == '__main__':
    main()
