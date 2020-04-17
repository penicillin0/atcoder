from fractions import gcd
N = int(input())
A = list(map(int, input().split()))
B, C = [A[0]], [A[N - 1]]

for i in range(1, N):
    B.append(gcd(B[i - 1], A[i]))

AA = list(reversed(A))
for i in range(1, N):
    C.append(gcd(C[i - 1], AA[i]))
C.reverse()
ans = 0
for i in range(1, N - 1):
    ans = max(ans, gcd(B[i - 1], C[i + 1]))
ans = max(ans, B[N - 2], C[1])
print(ans)