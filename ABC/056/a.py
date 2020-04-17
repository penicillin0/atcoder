import math
X = int(input())

N = (-1 + (1 + 8 + X)**(1 / 2)) / 4
if N / 1 == N // 1:
    print(N)
else:
    print(math.ceil(N) - 1)
