from collections import deque

n = int(input())
A = list(map(int, input().split()))

if n == 2:
    print(max(A))
    exit()

A.sort()
B = A[::-1]
point = deque()
point.append(B[0])
ans = 0
for i in range(1, n):
    ans += point.popleft()
    point.append(B[i])
    point.append(B[i])
print(ans)
