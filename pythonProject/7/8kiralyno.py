SIDES = "+-----------------+"


def getTable(list):
    print(SIDES)
    for row in range(7, -1, -1):
        print('|', end='')
        for x in list:
            print(' ', end='')
            if x == row:
                print('Q', end='')
            else:
                print('.', end='')
        print(' |')
    print(SIDES)


def main():
    list1 = [7,3,0,2,5,1,6,4]
    list2 = [0,4,7,5,2,6,1,3]

    getTable(list1)
    print(list1)


if __name__ == '__main__':
    main()
