import sys
input = sys.stdin.readline
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
yo = [['@'] * W for _ in range(H)]
ta = [['@'] * W for _ in range(H)]


def yoko(y, x):
    ret1 = 0
    xx = x
    while xx + 1 <= W - 1 and S[y][xx + 1] != '#':
        ret1 += 1
        xx += 1
    xxx = x
    ret2 = 0
    while 0 <= xxx - 1 and S[y][xxx - 1] != '#':
        ret2 += 1
        xxx -= 1
    ret3 = ret1 + ret2
    for i in range(xxx, xx + 1):
        yo[y][i] = ret3
    return ret3


def tate(y, x):
    ret1 = 0
    yy = y
    while 0 <= yy - 1 and S[yy - 1][x] != '#':
        ret1 += 1
        yy -= 1
    yyy = y
    ret2 = 0
    while yyy + 1 <= H - 1 and S[yyy + 1][x] != '#':
        ret2 += 1
        yyy += 1
    ret3 = ret1 + ret2
    for i in range(yy, yyy + 1):
        ta[i][x] = ret3
    return ret3


for y in range(H):
    for x in range(W):
        if S[y][x] == '#':
            continue
        if yo[y][x] == '@':
            yoko(y, x)
        if ta[y][x] == '@':
            tate(y, x)
        else:
            continue

ans = 0
for y in range(H):
    for x in range(W):
        if S[y][x] == '#':
            continue
        else:
            ans = max(ans, ta[y][x] + yo[y][x] + 1)
print(ans)