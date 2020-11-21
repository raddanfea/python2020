#!/usr/bin/env python3
def main():
    sztring1 = "python"
    sztring2 = None

    if bool(sztring1) != bool(sztring2):
        print("True")
        return True
    else:
        return False

if __name__ == '__main__':
    main()
