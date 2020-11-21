#!/usr/bin/env python3
from enum import Enum, auto
import sys


def main():
    if len(sys.argv) == 2:
        words = sys.argv[1]

        print(words, '->', hangrend(words))
    else:
        print("Expected one argument: szó")


class MELY(Enum):
    a = auto()
    á = auto()
    o = auto()
    ó = auto()
    u = auto()
    ú = auto()


class MAGAS(Enum):
    e = auto()
    é = auto()
    i = auto()
    í = auto()
    ö = auto()
    ő = auto()
    ü = auto()
    ű = auto()


def hangrend(x):
    magas = False
    mely = False

    for c in x:
        if c.lower() in MELY._member_names_:
            mely = True
        if c.lower() in MAGAS._member_names_:
            magas = True

    if magas and mely:
        return 'vegyes'
    elif magas:
        return 'magas'
    elif mely:
        return 'mély'
    else:
        return 'Nincs magánhangzó!'


if __name__ == '__main__':
    main()
