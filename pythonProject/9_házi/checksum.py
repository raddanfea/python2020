#!/usr/bin/env python3
import sys


def main(argv):

    if len(argv) == 2:
        INPUT = argv[1]

        cul = 0;

        with open(INPUT, 'r') as f1:

            for line in f1:
                intList = [int(i) for i in line.split()]
                high = max(intList)
                low = min(intList)
                cul = cul + high - low
        print(cul)
    else:
        print("Expected one argument: filename")

####################################


if __name__ == '__main__':
    main(sys.argv)
