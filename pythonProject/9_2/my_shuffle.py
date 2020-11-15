#!/usr/bin/env python3
from copy import copy
import random


def my_shuffled(listIn):
    listOut = copy(listIn)
    random.shuffle(listOut)
    return listOut


def main():
    list1 = [1, 2, 3, 4, 5]
    print("Original:")
    print(list1)
    print("Shuffled [-1]:")
    print(my_shuffled(list1)[-1])
    print("Original Unchanged:")
    print(list1)


####################################


if __name__ == '__main__':
    main()
