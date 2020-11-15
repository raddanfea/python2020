def main():
    chars = "abcdefghijklmnopqrstuvwxyz"
    codes = range(ord('a'), ord('z')+1)

    for t in zip(chars, codes):
        print(t)


if __name__ == '__main__':
    main()
