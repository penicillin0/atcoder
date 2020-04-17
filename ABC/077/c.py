from bisect import bisect_right, bisect_left
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
C.sort()
s = 0
for j in range(N):
    s += bisect_left(A, B[j]) * (N - bisect_right(C, B[j]))
print(s)
