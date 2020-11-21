#!/usr/bin/env python3

n = 1000
inp = [n for n in range(1, n) if n % 3 == 0 or n % 5 == 0]
print(sum(inp))

