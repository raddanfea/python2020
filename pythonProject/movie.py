#!/usr/bin/env python3

def get_movie_info():
    # f t h adatbázis
    # rekord lekérdezés
    return ("Total Recall", 1990, 7.5)


def main():
    (cim, ev, pontszam) = get_movie_info()
    print(cim, ev, pontszam)


if __name__ == '__main__':
    main()
