n = int(input())
A = list(set([int(input()) for _ in range(n)]))
A.sort()
print(A[-2])
