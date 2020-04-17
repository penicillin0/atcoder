from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = deque()

ans = 0

s = 0
left, right = 0, 0
for a in A:
    B.append(a)
    right += 1
    s += a
    if s < K:
        continue
    else:
        while s >= K:
            ans += (N + 1) - right
            s -= B[0]
            B.popleft()
            left += 1
print(ans)
