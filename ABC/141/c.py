n, k, q = map(int, input().split())

A = [0] * n

for i in range(q):
    a = int(input())
    A[a - 1] += 1


for a in A:
    if k - q + a > 0:
        print('Yes')
    else:
        print('No')