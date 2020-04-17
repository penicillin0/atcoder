N, K = map(int, input().split())
X = list(map(int, input().split()))

lft, rgt = 0, K - 1
ans = float('inf')

while True:
    if rgt == N:
        break
    ans = min(ans, min(abs(X[lft]) + abs(X[lft] - X[rgt]),
                       abs(X[rgt]) + abs(X[rgt] - X[lft])))
    lft += 1
    rgt += 1
print(ans)
