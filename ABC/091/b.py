N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

ans = 0

for a in S:
    p = S.count(a)
    q = T.count(a)
    ans = max(ans, p - q)
print(ans)