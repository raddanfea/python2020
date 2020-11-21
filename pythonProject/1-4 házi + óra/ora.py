
def ciklus(start, end, debug=False):
    if debug:
        print('#ciklus kezdete')
    inp = [str(n ) +',' for n in range(start, end + 1)]
    print(''.join(inp)[:-1])
    if debug:
        print('#ciklus vége')

def main():
    ciklus(1, 10)
    ciklus(1, 10, True)

if __name__ == '__main__':
    main()
