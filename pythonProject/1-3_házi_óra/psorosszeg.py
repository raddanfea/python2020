#!/usr/bin/env python3
# első sor kötelező a hordozhatósághoz

import sys


def main():

    s = 0
    for i in range(1,len(sys.argv)):
        s = s + int(sys.argv[i])

    print(s)

if __name__ == '__main__':
    main()
