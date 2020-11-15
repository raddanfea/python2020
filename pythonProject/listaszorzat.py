#!/usr/bin/env python3
def main():
    html = """
<html>
<body>
<h1>Hello</h1>
</body>
</html>
""".strip()

    print(html)

    li = [9, 8, 1, 4, 8, 2, 3, 2]
    print(product(li))


def product(n):
    value = 1
    for i in n:
        value = i * value
    return value


if __name__ == '__main__':
    main()
