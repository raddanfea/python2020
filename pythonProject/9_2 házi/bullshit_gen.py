#!/usr/bin/env python3
import sys

import bullshit


def main():
    if len(sys.argv) == 1:
        print(bullshit.get_bullshit())
    else:
        print("Expected no argument.")


if __name__ == '__main__':
    main()
