def is_palindrome(s):
    return s == s[::-1]


def test(num):
    lower = num
    max = lower * 10**6

    for num in range(lower, max):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                if is_palindrome(str(num)):
                    return num


def main():
    print(130, test(130))
    print(131, test(131))
    print(1977, test(1977))
    print(31111, test(31111))


if __name__ == '__main__':
    main()
