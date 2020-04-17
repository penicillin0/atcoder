N, M = map(int, input().split())
K = [list(map(int, input().split())) for _ in range(M)]
P = list(map(int, input().split()))

num = 2**N
ans = 0
for i in range(num):
    bit = bin(i)[2:].zfill(N)
    on, off = [], []
    ret = 0
    for j, b in enumerate(bit):
        j += 1
        if b == '1':
            on.append(j)
        else:
            off.append(j)
    for k in range(M):
        on = set(on)
        onon = set(K[k][1:])
        if len(on & onon) % 2 == P[k]:
            ret += 1
    if ret == M:
        ans += 1

print(ans)
