#!/usr/bin/env python3

def main():

    '''

    f = open("text.txt", "r")

    for line in f:
        line = line.rstrip('\n')
        if line.endswith('sor'):
            print(line)
    f.close()

    f = open("text.txt", "r")
    sorok = [line.rstrip('\n') for line in f]
    print(sorok)
    f.close()

    f = open("text.txt", "r")
    tartalom = f.read().splitlines()
    print(tartalom)
    f.close()

    f = open("text.txt", "r")

    for line in f:
        line = line.rstrip('\n')
        if line.endswith('sor'):
            print(line)
    f.close()

    f = open("out.txt", "w")
    print("world", file=f)
    print("yolo", file=f)
    f.write("aaaa")
    f.write("bbbb")
    f.close()
    '''

    INPUT = "string1.py"
    OUTPUT = "string1_clean.py"

    with open(INPUT, 'r') as f1, open(OUTPUT, 'w') as to:
        for line in f1:
            if not line.lstrip().startswith('#'):
                to.write(line)

####################################


if __name__ == '__main__':
    main()
