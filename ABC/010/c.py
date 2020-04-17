tx1, ty1, tx2, ty2, T, V = map(int, input().split())
n = int(input())

XY = [list(map(int, input().split())) for _ in range(n)]

for x, y in XY:
    dist = ((tx1 - x) ** 2 + (ty1 - y) ** 2) ** (1/2) + \
        ((tx2 - x) ** 2 + (ty2 - y) ** 2) ** (1 / 2)
    if dist <= T * V:
        print('YES')
        exit()
print('NO')

