from math import ceil

N = int(input())
A = list(map(int, input().split()))

A.sort()

if N % 2 == 1:
    num = (N - 1) // 2
    if A[0] != 0:
        print(0)
        exit()
    for i in range(1, N):
        if A[i] == ceil(i / 2) * 2:
            continue
        else:
            print(0)
            exit()
else:
    num = N // 2
    for i in range(N - 1):
        if A[i] == (i // 2) * 2 + 1:
            continue
        else:
            print(0)
            exit()

print((2**num) % (10**9 + 7))
