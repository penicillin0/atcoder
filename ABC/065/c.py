N, M = map(int, input().split())

if N <= M:
    N, M = M, N

if N - M > 1:
    print(0)
    exit()

num = 10**9 + 7


def bikkuri(n):
    rt = 1
    for i in range(n, 0, -1):
        rt *= i
        rt = rt % num
    return rt


ans = (bikkuri(M)**2) % num

if N == M:
    ans *= 2
else:
    ans *= (M + 1)

ans %= num
print(ans)
