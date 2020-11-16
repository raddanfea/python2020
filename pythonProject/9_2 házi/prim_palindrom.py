#!/usr/bin/env python3
import sys


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

    if len(sys.argv) == 2:
        print(sys.argv[1], test(int(sys.argv[1])))
    else:
        print("Expected one argument: int")

if __name__ == '__main__':
    main()
