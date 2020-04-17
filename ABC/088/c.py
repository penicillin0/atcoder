import sys
input = sys.stdin.readline
N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

s, e = set(), set()
for ab in AB:
    a, b = ab
    if a == 1:
        s.add(b)
    elif b == N:
        e.add(a)
if len(s & e) >= 1:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
