def isanagram(s1, s2):
    d1 = {}
    for char in s1:
        if char not in d1:
            d1[char] = 1
        else:
            d1[char] = d1[char] + 1

    d2 = {}
    for char in s2:
        if char not in d2:
            d2[char] = 1
        else:
            d2[char] = d2[char] + 1

    # print(d1,"\n" ,d2)
    return d1 == d2


def normalise(s):
    return s.replace(' ', '').lower()


def main():
    n = 1
    while n == 1:
        inp = input("Type words such as: word = word \n")
        values = inp.split('=')
        print(isanagram(normalise(values[0]), normalise(values[-1])))


if __name__ == '__main__':
    main()
