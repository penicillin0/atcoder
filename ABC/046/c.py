from math import ceil
from fractions import Fraction
n = int(input())
TA = [list(map(int, input().split())) for _ in range(n)]
tka, aok = 1, 1

for ta in TA:
    t, a = ta
    time = int(ceil(max((Fraction(tka, t), Fraction(aok, a)))))
    tka, aok = time * t, time * a
print(tka+aok)
