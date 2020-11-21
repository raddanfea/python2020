#!/usr/bin/env python3
import sys


class Verem:
    def __init__(self):
        self.content = []

    def ures(self):
        return not bool(len(self.content))

    def meret(self):
        return len(self.content)

    def betesz(self, ertek):
        return self.content.append(ertek)

    def kivesz(self):
        try:
            return self.content.pop()
        except IndexError:
            return None

    def __str__(self):
        return str(self.content)


def main():

    if len(sys.argv) == 1:

        v = Verem()  # üres verem létrehozása
        print(v)  # [
        print(v.ures())  # True
        v.betesz(1)
        v.betesz(4)
        v.betesz(5)
        print(v)  # [1 4 5
        print(v.meret())  # 3
        print(v.ures())  # False
        x = v.kivesz()
        print(x)  # 5
        print(v)  # [1 4
        v.kivesz()
        v.kivesz()  # most már üres
        x = v.kivesz()
        print(x)  # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)
    else:
        print("Expected no argument.")

if __name__ == '__main__':
    main()
