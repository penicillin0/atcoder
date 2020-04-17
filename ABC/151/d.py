h, w = map(int, input().split())

def cl(sx, sy, m):
    Z = -1
    dist = [[Z for i in range(w)] for j in range(h)]
    for i in range(h):
        for j in range(w):
            if m[i][j] == '#':
                dist[i][j] = -1

    def bfs():
        q = []
        q.insert(0, (sx, sy))
        dist[sy][sx] = 0
        while len(q):
            x, y = q.pop()
            for i in range(0, 4):
                nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]
                if (0 <= nx < w and 0 <= ny < h and m[ny][nx] != '#' and dist[ny][nx] == Z):
                    q.insert(0, (nx, ny))
                    dist[ny][nx] = dist[y][x] + 1
        return dist
    return bfs()

S = [list(input()) for _ in range(h)]
ans = 0
for y in range(h):
    for x in range(w):
        e = S[y][x]
        if e != '#':
            num = cl(x, y, S)
            for k in range(h):
                ans = max(ans, max(num[k]))
print(ans)
