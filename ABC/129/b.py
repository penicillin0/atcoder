N = int(input())
W = list(map(int, input().split()))
S = sum(W)
ans = 10**8
for i in range(N - 1):
    A = sum(W[:i + 1])
    B = S - A
    ans = min(ans, abs(B - A))
print(ans)