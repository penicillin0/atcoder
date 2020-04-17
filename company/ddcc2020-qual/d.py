h, w, k = map(int, input().split())
SS = [list(input()) for _ in range(h)]
num = 1
ans = [[0] * w for _ in range(h)]

flag = False
for i in range(h):
    S = SS[i]
    for j in range(w):
        if ans[i][j] != 0:
            continue

        s = [i, j]
        




for i, a in enumerate(ans):
    a = list(map(str, a))
    if i % 2 == 1:
        a = a[::-1]
    print(' '.join(a))
