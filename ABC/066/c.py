import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
ans = deque([])
if n % 2 == 0:
    for i in range(n):
        if i % 2 == 0:
            ans.appendleft(A[i])
        else:
            ans.append(A[i])
else:
    for i in range(n):
        if i % 2 == 0:
            ans.append(A[i])
        else:
            ans.appendleft(A[i])

ans = list(ans)
ans.reverse()
ans = list(map(str, ans))
print(' '.join(ans))
