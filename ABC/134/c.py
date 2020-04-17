N = int(input())
A = [int(input()) for _ in range(N)]

B = sorted(A, reverse=True)


MAX1 = B[0]
MAX2 = B[1]


if MAX1 == MAX2:
    for a in range(N):
        print(MAX1)
else:
    for a in A:
        if a != MAX1:
            print(MAX1)
        else:
            print(MAX2)
