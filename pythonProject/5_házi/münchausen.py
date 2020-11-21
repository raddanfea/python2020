

def main():
    # 0-tól nig kiszámolja a Münchausen számokat.
    n = 10000

    for i in range(0, n):
        l = list(str(i))
        munch = [int(n) ** int(n) for n in l]
        if i == sum(munch) or i == 0:
            print(i)




if __name__ == '__main__':
    main()
