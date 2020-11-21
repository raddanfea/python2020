#!/usr/bin/env python3


def main():



    words = input("Szó:")

    print(words, '->',hangrend(words))


def hangrend(x):
        MELY = 'aáoóuú'
        MAGAS = 'eéiíöőüű'

        magas = False
        mely = False

        for c in x:
            if c.lower() in list(MELY):
                mely = True
            if c.lower() in list(MAGAS):
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
