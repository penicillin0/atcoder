N, x = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

if A[0] > x:
    ans += A[0] - x
    A[0] = x

if A[-1] > x:
    ans += A[-1] - x
    A[-1] = x

for i in range(N - 1):
    sa = A[i] + A[i + 1] - x
    if sa > 0:
        ans += sa
        A[i + 1] -= sa

print(ans)
