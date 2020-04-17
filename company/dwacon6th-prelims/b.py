
from math import factorial
n = int(input())
X = list(map(int, input().split()))

cnt = []

cnt = [1]

for i in range(2, n):
    for j in range(len(cnt)):
        cnt[j] *= i
    cnt.append(cnt[-1] + cnt[0] // i)
# print(cnt)

print(cnt)
ans = 0
for i in range(1, n):
    r = abs(X[i] - X[i - 1])
    ans += r * cnt[i - 1]
    print(r, cnt[i-1])
    ans %= 10 ** 9


print(ans)



