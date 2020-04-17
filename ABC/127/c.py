import sys
input = sys.stdin.readline
N, M = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]

A, B = 1, N
for lr in LR:
    L, R = lr
    if R < A or B < L:
        print(0)
        exit()

    if A <= L <= R <= B:
        A, B = L, R
    elif L <= A <= R <= B:
        B = R
    elif A <= L <= B <= R:
        A = L
print(B - A + 1)
