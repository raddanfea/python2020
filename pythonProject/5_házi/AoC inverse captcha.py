

def ic(s):
    # checks if next chars are the same, if true adds it to sum.
    # checks last and first char equalency as well.
    # returns cumulative sum of fulfilled conditions
    sum = 0
    length = int(len(s)/2)
    #print(length)
    for i in range(0, len(s)-length):
        if s[i] == s[i+length]:
            sum = sum + int(s[i])
            #print("added",int(s[i]))
    for i in range(len(s)-length, len(s)):
        if s[i] == s[i-length]:
            sum = sum + int(s[i])
            #print("addedv",int(s[i]))
    return sum


def main():
    while True:
        i = input("Numbering:")
        print(ic(i))


if __name__ == '__main__':
    main()
