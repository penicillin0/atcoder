import sys
input = sys.stdin.readline
N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]
seki = 0
if 0 in S:
    print(len(S))
    exit()

lft, rgt = 0, 0
seki = S[0]

if seki <= K:
    ans = 1
else:
    ans = 0

while True:
