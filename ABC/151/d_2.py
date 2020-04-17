from collections import deque
h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]
INF = 10010001001
way = [[0, 1], [0, -1], [1, 0], [-1, 0]]

ans = 0
for sy in range(h):
    for sx in range(w):
        dist = [[INF] * w for _ in range(h)]
        dist[sy][sx] = 0
        if S[sy][sx] == '#':
            continue
        q = deque()
        q.append((sy, sx))
        while q:
            y, x = q.popleft()
            for dy, dx in way:
                ny, nx = y + dy, x + dx
                if 0 <= ny <= h - 1 and 0 <= nx <= w - 1 and S[ny][nx] == '.' and dist[ny][nx] == INF:
                    dist[ny][nx] = dist[y][x] + 1
                    ans = max(ans, dist[y][x] + 1)
                    q.append((ny, nx))
print(ans)