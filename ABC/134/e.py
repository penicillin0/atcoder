N = int(input())
A = [int(input()) for _ in range(N)]

ans = 0

B = [A[0]]

M = A[0]
for i in range(1, N):
    if A[i] < M:
        B.append(A[i])

    else:
        for i in range(len(B)):
            if
    B.sort()
    M = B[0]
print(B)
