import sys
input = sys.stdin.readline
N = int(input())
TXY = [list(map(int, input().split())) for _ in range(N)]
t, x, y = 0, 0, 0
for i in range(N):
    T, X, Y = TXY[i]
    z = (T - t) - ((X - x) + (Y - y))
    if z >= 0 and z % 2 == 0:
        t, x, y = T, X, Y
    else:
        print('No')
        exit()
print('Yes')
