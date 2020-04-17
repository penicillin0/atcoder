import math
import itertools

n = int(input())
C = [int(input()) for _ in range(n)]


def cluc_cnt(row):
    coins = [1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if row[j] // row[i] == row[j] / row[i]:
                coins[j] *= -1
    return coins.count(1)


ans = 0

for l in itertools.permutations(C):
    ans += cluc_cnt(l)

print(ans/math.factorial(n))
