#!/usr/bin/env python3
import sys


def concat(string_input):
    list_output = []
    for each in string_input.strip().split(','):
        midpos = each.find('-')
        if midpos > 0:
            for i in range(int(each[:midpos]), int(each[midpos + 1:]) + 1):
                list_output.append(i)
        else:
            list_output.append(int(each))
    return list_output


def main():

    if len(sys.argv) == 1:
        string1 = "1-4, 7, 9, 11-15"
        print("TEST:")
        print(concat(string1))
        print("TEST SUCCESSFUL")

        while True:
            inpt = input("Írd be a saját teszted:")

            if inpt == 'q':
                return False
            print(concat(inpt))
    else:
        print("Expected no args.")


if __name__ == '__main__':
    main()
