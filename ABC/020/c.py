import sys
sys.setrecursionlimit(10**9)
H, W, T = map(int, input().split())
field = [list(input()) for _ in range(H)]

for x in range(W):
    for y in range(H):
        if field[y][x] == 'S':
            sx, sy = x, y

dirc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
road = ['#', '.', 'G']


def dfs(black, white, x, y):
    if field[y][x] == 'G':
        print((T - white) // black)
        print(black, white)

    field[y][x] = 'x'
    for dx, dy in dirc:
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H and field[ny][nx] in road:
            print(nx, ny, field[ny][nx])
            if field[ny][nx] == '#':
                dfs(black + 1, white, nx, ny)
            else:
                dfs(black, white + 1, nx, ny)


print(dfs(0, 0, sx, sy))
