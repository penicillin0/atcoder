N = int(input())
par = [-1] * N  # 親だった場合は-(その集合のサイズ)

if N == 1:
    print(0)


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
    par[x] += par[y]
    # yの親をxにする
    par[y] = x


# 同じ集合に属するか判定
def same(x, y):
    return find(x) == find(y)


AB = [list(map(int, input().split())) for _ in range(N - 1)]
C = list(map(int, input().split()))

for ab in AB:
    a, b = ab
    a, b = a - 1, b - 1
    if same(a, b):
        continue
    else:
        unite(a, b)

n = find(0)
# print(n)
ret = sum(C) - max(C)
print(ret)
m = C.index(max(C))
if n != m:
    C[n], C[m] = C[m], C[n]
C = list(map(str, C))
print(' '.join(C))
