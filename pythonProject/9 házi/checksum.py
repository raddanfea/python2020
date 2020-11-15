#!/usr/bin/env python3


def main():
    INPUT = "checksum"

    cul = 0;

    with open(INPUT, 'r') as f1:

        for line in f1:
            intList = [int(i) for i in line.split()]
            high = max(intList)
            low = min(intList)
            cul = cul + high - low
    print(cul)

####################################


if __name__ == '__main__':
    main()
