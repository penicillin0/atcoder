import sys
from collections import deque
input = sys.stdin.readline


def ansans(ans):
    for a in ans:
        a, b = a
        print(a, b)
    exit()


ans = []
N = int(input())
A = list(map(int, input().split()))
cnt = 0
z = 0
PL = []
ML = []
for a in A:
    if a > 0:
        PL.append(a)
    elif a < 0:
        ML.append(a)
    else:
        z += 1
PL.sort()
ML.sort()
print(PL, ML)

PL = deque(PL)
ML = deque(ML)

if z != 0:
    if len(PL) == 0:
        a = PL[0]
        PL.popleft()
        b = PL[0]
        PL
        ans.append(PL[0])
        
else:


