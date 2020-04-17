from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

f = [list(input()) for _ in range(R)]
dirc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

f[sy - 1][sx - 1] = 0
que = deque([[sy - 1, sx - 1]])

while que:
    py, px = que.popleft()
    if (py, px) == (gy - 1, gx - 1):
        break
    for dy, dx in dirc:
        ny, nx = py + dy, px + dx
        if f[ny][nx] == '.':
            que.append([ny, nx])
            f[ny][nx] = f[py][px] + 1

print(f[gy - 1][gx - 1])
