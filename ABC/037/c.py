import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(reversed(A))
if N % 2 == 0:
    n1, n2 = N // 2, N // 2
else:
    n1 = N // 2 + 1
    n2 = N // 2
ans = 0
for i in range(n1):
    num = i + 1
    if num <= K:
        ans += A[i] * min(num, (N - K + 1))
    else:
        ans += A[i] * min(K, (N - K + 1))
for i in range(n2):
    num = i + 1
    if num <= K:
        ans += B[i] * min(num, (N - K + 1))
    else:
        ans += B[i] * min(K, (N - K + 1))

print(ans)
