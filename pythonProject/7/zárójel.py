def main():

    test("((5+3)*2+1)")
    test("{[(3+1)+2]+}")
    test("(3+{1-1)}")
    test("[1+1]+(2*2)-{3/3}")
    test("(({[(((1)-2)+3)-3]/3}-3)")


def test(s):
    # remove nonimportant characters
    charlist = ['(', ')', '[', ']', '{', '}']
    getS = list([val for val in s if val in charlist])
    s = "".join(getS)
    # remove brackets from inside out
    brackets = ['()', '{}', '[]']
    while any(x in s for x in brackets):
        for br in brackets:
            s = s.replace(br, '')
    print(not s)


if __name__ == '__main__':
    main()

