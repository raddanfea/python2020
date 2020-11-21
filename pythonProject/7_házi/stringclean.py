def main():
    INPUT = "string1.py"
    OUTPUT = "string1_clean.py"

    with open(INPUT, 'r') as f1, open(OUTPUT, 'w') as to:
        for line in f1:
            if not line.lstrip().startswith('#'):
                to.write(line)

####################################


if __name__ == '__main__':
    main()
