h, w = map(int, input().split())

S = [list(input()) for _ in range(h)]

ans = 0

for sy in range(h):
    for sx in range(w):
        if S[sy][sx] != '#':
            continue
        for gy in range(h):
            for gx in range(w):
                if S[gy][gx] != '#':
                    continue
                else:
                    ans = max(ans)

        

