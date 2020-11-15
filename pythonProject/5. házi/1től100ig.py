# shell: sum(range(100+1))



def szamlyegyosszeg(n):
    # Visszaadja az egész számok számjegyeinek összegét n-ig.
    outp = ""
    inp = [str(n) for n in range(n+1)]
    outp = [int(char) for char in outp.join(inp)]
    return sum(outp)

def main():
    print(szamlyegyosszeg(100))


if __name__ == '__main__':
    main()
