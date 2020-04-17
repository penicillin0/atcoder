import sys
input = sys.stdin.readline
import math
N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

cost = float('inf')
for i in range(N + 1):  # 普通な食事
    hara = H + i * B - E * (N - i)
    if hara > 0:
        j = 0
    else:
        tarinai = -hara
        if tarinai % (D + E) == 0:
            j = math.ceil(tarinai / (D + E)) + 1
        else:
            j = math.ceil(tarinai / (D + E))
    cost = min(cost, i * A + C * j)
print(cost)
