def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    # vissazdja a textből azokat a karaktereket amik megtalálhatóak a charsban.
    # alapértelmezett a nagy angol abc és arab számjegyek
    inp = [n for n in text if n in chars]
    return ''.join(inp)


def main():
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))


if __name__ == '__main__':
    main()
