N = int(input())
UVW = [list(map(int, input().split())) for _ in range(N - 1)]
for i in range(N - 1):
    UVW[i].append(i)

UVW.sort(key=lambda x: (x[0], x[1]))
ans = [0] * (N + 1)
for uvw in UVW:
    u, v, w, z = uvw
    if w % 2 == 1:
        if ans[u] == ans[v]:
            if ans[v] == 1:
                ans[v] = 0
            else:
                ans[v] = 1

for i in range(1, N + 1):
    print(ans[i])
