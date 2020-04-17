import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

big = max(A)
sml = min(A)

ans = float('inf')

for i in range(sml, big + 1):
    cnt = 0
    for a in A:
        cnt += (abs(i - a))**2
    ans = min(ans, cnt)
print(ans)
