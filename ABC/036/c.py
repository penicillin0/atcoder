import sys
input = sys.stdin.readline
N = int(input())
A = [[int(input()), _] for _ in range(N)]
A.sort(key=lambda x: x[0])
A[0].append(0)
z = A[0][0]
B = [0] * N

for i in range(1, N):
    if A[i][0] == z:
        A[i].append(A[i - 1][2])
    else:
        A[i].append(A[i - 1][2] + 1)
        z = A[i][0]
A.sort(key=lambda x: x[1])

for a in A:
    print(a[2])