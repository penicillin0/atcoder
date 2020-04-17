import copy
field = [list(input()) for _ in range(10)]
field0 = copy.deepcopy(field)
fieldcomp = [['x'] * 10] * 10
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(x, y):
    field[y][x] = 'x'
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 10 and 0 <= ny < 10:
            if field[ny][nx] == 'o':
                dfs(nx, ny)


for i in range(10):
    for j in range(10):
        if field[j][i] == 'x':
            dfs(i, j)
            if field == fieldcomp:
                print('YES')
                exit()
            field = copy.deepcopy(field0)

print('NO')
