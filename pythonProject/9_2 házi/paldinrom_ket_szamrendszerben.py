#!/usr/bin/env python3
import sys


def is_palindrome(s):
    return s == s[::-1]


def decimalToBinary(n):
    return bin(n).replace("0b", "")


def main():

    if len(sys.argv) == 1:
        cum = 0;
        for num in range(0, 1000000):
            if is_palindrome(str(num)):
                if is_palindrome(str(decimalToBinary(num))):
                    cum = cum + num

        print(cum)
    else:
        print("Expected no args.")


if __name__ == '__main__':
    main()
