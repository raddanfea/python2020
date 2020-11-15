#!/usr/bin/env python3
# első sor kötelező a hordozhatósághoz

import sys


def hello(name, color, what):
    print("{0},{1},{2}".format(name, color, what))


def hello2(name, color, what):
    print("{},{},{}".format(name, color, what))


def hello3(name, color, what):
    print("{name} {szin},{obj}".format(name=name.capitalize(),
                                       szin=color,
                                       obj=what))


def hello4(name, color, what):
    print(f"{name}, {color} az {what}")


def is_palindrom(s):
    return s == s[::-1]


def main():
    hello("a", "b", "c")
    hello2("a", "b", "c")
    hello3("a", "b", "c")
    hello4("a", "b", "c")

    hello3("Julcsi", "piros", "autó")

    print("-" * 30)
    print("Palindrom?")
    print("tet", is_palindrom("tet"))
    print("tett", is_palindrom("tett"))



if __name__ == '__main__':
    main()
