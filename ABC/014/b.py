n, X = map(int, input().split())
A = list(map(int, input().split()))
X_bin = bin(X)[2:].zfill(n)

ans = 0
for idx, isUse in enumerate(reversed(X_bin)):
    if isUse == '1':
        ans += A[idx]
print(ans)
