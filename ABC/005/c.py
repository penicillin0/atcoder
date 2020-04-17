T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

if N < M:
    print('no')
    exit()

a, b = 0, 0

a, b = 0, 0

while True:
    if A[a] + T >= B[b] >= A[a]:
        a += 1
        b += 1
    else:
        a += 1

    if b == M and a == N:
        print('yes')
        exit()

    if b == M:
        print('yes')
        exit()
    if a == N:
        print('no')
        exit()