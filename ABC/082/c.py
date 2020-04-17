import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
C = Counter(A)

ans = 0
for c in C:
    if c > C[c]:
        ans += C[c]
    elif c < C[c]:
        ans += C[c] - c
print(ans)