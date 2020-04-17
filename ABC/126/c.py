from math import log2
from math import ceil
N, K = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    if i >= K:
        ans += 1 / N
    else:
        n = ceil(log2(K / i))
        ans += 1 / N * pow(1 / 2, n)
print(ans)