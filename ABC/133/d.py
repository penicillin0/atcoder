N = int(input())
A = list(map(int, input().split()))
B = [0] * N

A.reverse()
num = A[0]
for i in range(1, N):
    if i % 2 == 0:
        num -= A[i]
    else:
        num += A[i]

B[0] = num

for i in range(1, N):
    B[i] = 2 * (A[i] - (B[i - 1] // 2))
B.reverse()
B = list(map(str, B))
print(' '.join(B))