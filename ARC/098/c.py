import sys
input = sys.stdin.readline
N = int(input())
S = list(input())

e, w = 0, 0
right, left = [], []
for s in S:
    if s == 'E':
        e += 1
    else:
        w += 1
    left.append([e, w])
ss = list(reversed(S))
e, w = 0, 0
for s in ss:
    if s == 'E':
        e += 1
    else:
        w += 1
    right.append([e, w])
right.reverse()
ans = float('inf')

for i in range(N):
    if i == 0:
        ans = min(ans, right[1][0])
    elif i == N - 1:
        ans = min(ans, left[-2][1])
    else:
        ans = min(ans, right[i + 1][0] + left[i - 1][1])
print(ans)
