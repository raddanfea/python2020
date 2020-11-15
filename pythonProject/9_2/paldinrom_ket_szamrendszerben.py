#!/usr/bin/env python3

def is_palindrome(s):
    return s == s[::-1]


def decimalToBinary(n):
    return bin(n).replace("0b", "")


def main():
    cum = 0;
    for num in range(0, 1000000):
        if is_palindrome(str(num)):
            if is_palindrome(str(decimalToBinary(num))):
                cum = cum + num

    print(cum)


if __name__ == '__main__':
    main()
