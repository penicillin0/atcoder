import itertools


N, M = map(int, input().split())
like = []
for i in range(M):
    _, __ = map(int, input().split())
    like.append((_, __))

ans = 0
for i in range(2**N):
    habatu = []
    for j in range(N):
        if i & (1 << j):
            habatu.append(j + 1)
    flag = True
    for p, q in itertools.combinations(habatu, 2):
        if (p, q) not in like:
            flag = False
            break

    if flag:
        ans = max(ans, len(habatu))
print(ans)
