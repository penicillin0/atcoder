N, K = map(int, input().split())
TD = [list(map(int, input().split())) for _ in range(N)]

TD.sort(key=lambda x: x[1])

F, S = [], []
TD.sort(key=lambda x: (x[0], -x[1]))

k = TD[0][0]
F.append(TD[0])

for i in range(1, N):
    t, d = TD[i]
    if k == t:
        S.append([t, d])
    else:
        F.append([t, d])
        k = t


F.sort(key=lambda x: x[1])
S.sort(key=lambda x: x[1])

cnt = 0
for i in range(0, len(F)):
    F[i][0] +=
