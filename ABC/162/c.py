from math import gcd
K = int(input())
ans = 0

for i in range(1, K + 1):
    for j in range(1, K + 1):
        a = gcd(i, j)
        if a == 1:
            ans += K
            continue
        for k in range(1, K + 1):
            ans += gcd(a, k)
print(ans)