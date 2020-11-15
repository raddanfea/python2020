#!/usr/bin/env python3
# első sor kötelező a hordozhatósághoz

import sys


def hello(name):
    print(sys.argv[0])

    ss = sys.argv[1]


    for i in range(0,len(sys.argv)):
        print(sys.argv[i])

    if s == "Batman" or "Robin":
        print("You will never be Batman!")
    else:
        print("Welcome " + ss)


def main():
    s = input("Nev: ")
    print("Hello " + s + "!")


if __name__ == '__main__':
    main()
