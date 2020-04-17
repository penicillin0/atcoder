import sys
input = sys.stdin.readline
N, M = map(int, input().split())
par = [-1] * N  # 親だった場合は-(その集合のサイズ)


# xがどのグループに属しているか調べる
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return find(par[x])


# 自分のいるグループの数
def size(x):
    return -par[find(x)]


# xとyの属する集合を併合
def unite(x, y):
    # 根を探す
    x, y = find(x), find(y)

    # 根が一緒
    if x == y:
        return

    # 大きい方に小さい方をくっつける
    if size(x) < size(y):
        x, y = y, x
    # xのサイズを更新
    par[x] = par[x] + par[y]
    # yの親をxにする
    par[y] = x


# 同じ集合に属するか判定
def same(x, y):
    return find(x) == find(y)


ABY = [list(map(int, input().split())) for _ in range(M)]
Q = int(input())
VW = [list(map(int, input().split())) + [_] for _ in range(Q)]

ABY.sort(key=lambda x: x[2], reverse=True)
VW.sort(key=lambda x: x[1], reverse=True)

i = 0
ans = []
for v, w, idx in VW:
    v -= 1
    while True:
        if i == M:
            ans.append([idx, size(v)])
            break
        a, b, yer = ABY[i]
        a, b = a - 1, b - 1
        if w >= yer:
            ans.append([idx, size(v)])
            break
        else:
            if same(a, b):
                i += 1
            else:
                i += 1
                unite(a, b)

ans.sort(key=lambda x: x[0])

for answer in ans:
    print(answer[1])