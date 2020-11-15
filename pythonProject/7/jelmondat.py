def main():
    INPUT = "jelmondatok"

    valid = 0
    with open(INPUT, 'r') as fro:
        for line in fro:
            if line == line.lower():
                if occurs(line):
                    valid += 1
    print(valid)


def occurs(words):
    d = {}

    for word in words.split():
        if word not in d:
            d[word] = 1
        else:
            return False

    return True


if __name__ == '__main__':
    main()
