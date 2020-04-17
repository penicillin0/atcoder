from math import ceil
from fractions import gcd


def lcm(x, y):
    return (x * y) // gcd(x, y)


a, b, c, d = map(int, input().split())

A = max(b // c - ceil(a / c) + 1, 0)
B = max(b // d - ceil(a / d) + 1, 0)
C = max(b // lcm(c, d) - ceil(a / lcm(c, d)) + 1, 0)
print(max(b-a+1-(A+B-C), 0))
