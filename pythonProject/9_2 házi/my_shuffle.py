#!/usr/bin/env python3
import sys
from copy import copy
import random


def my_shuffled(listIn):
    listOut = copy(listIn)
    random.shuffle(listOut)
    return listOut


def main():
    if len(sys.argv) == 1:
        list1 = [1, 2, 3, 4]
        print("Original:")
        print(list1)
        print("Shuffled:")
        list2 = my_shuffled(list1)
        print(list2)
        print("Shuffled [-1]:")
        print(list2[-1])
        print("Original Unchanged:")
        print(list1)
    else:
        print("Expected no args.")


####################################


if __name__ == '__main__':
    main()
