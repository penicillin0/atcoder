h, n = map(int, input().split())
A = list(map(int, input().split()))

p = sum(A)
if p >= h:
    print('Yes')
else:
    print('No')