import sys
input = sys.stdin.readline


def binary_search(l, value):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == value:
            return True
        elif l[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return False


N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]

A.append(10**6)
A.append(10**6)
B = [0] * (N + 1)
B[0] = 1
if binary_search(A, 1) is True:
    B[1] = 0
else:
    B[1] = 1
mod = 10**9 + 7

for i in range(2, N + 1):
    if i != 2 and binary_search(A, i - 1) is True and binary_search(
            A, i - 2) is True:
        print(0)
        exit()
    elif binary_search(A, i - 2) is True:
        B[i] = B[i - 1]
    elif binary_search(A, i - 1) is True:
        B[i] = B[i - 2]
    else:
        B[i] = B[i - 1] + B[i - 2]
    B[i] %= mod
print(B[N] % mod)
