#!/usr/bin/env python3

import math


def distance(p1, p2):
    a = abs(p2[0] - p1[0])
    b = abs(p2[1] - p1[1])

    return math.sqrt(a * a + b * b)


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', distance(p1, p2))


#############################################################################

if __name__ == "__main__":
    main()
