n, k, m = map(int, input().split())

A = list(map(int, input().split()))

point = sum(A)
souwa = n * m

if point >= souwa:
    print(0)
elif k >= souwa - point:
    print(souwa - point)
else:
    print(-1)