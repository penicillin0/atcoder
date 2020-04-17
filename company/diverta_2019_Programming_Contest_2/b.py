N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
if N == 1:
    print(1)
    exit()

XY.sort(key=lambda x: x[0])

PQ = {}

for i in range(N):
    x0, y0 = XY[i]
    for j in range(N):
        if i == j:
            continue
        x1, y1 = XY[j]
        p, q = x0 - x1, y0 - y1
        key = str(p) + ',' + str(q)
        if key in PQ:
            PQ[key] += 1
        else:
            PQ[key] = 1
ansL = PQ.values()
print(N - max(list(ansL)))
