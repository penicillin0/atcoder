from itertools import combinations
n, m = map(int, input().split())
ab = []
C = []
for _ in range(m):
    ab.append(list(map(int, input().split())))
    C.append((list(map(int, input().split()))))

chk = []
for c in C:
    chk += c
    chk = list(set(chk))

if len(chk) != n:
    print(-1)
    exit()


# dp[i] 1..iまで開ける最小
dp = [-1] * (n + 1)

tool = [[] for _ in range(n+1)]
for j in range(n):
    cst, box = float('inf'), -1
    num = j + 1
    sml = float('inf')
    for k in range(m):
        if num in C[k] and cst >= ab[k][0]:
            box = k + 1
            cst = ab[k][0]
    tool[num].append((cst, box))
    for k in range(m):
        if num in C[k] and cst == ab[k][0] and k + 1 != box:
            tool[num].append((cst, k + 1))


dp[1] = tool[1]
print(dp[1])
for i in range(2, n + 1):
    kouho = []
    for d in dp[i - 1]:
        for t in tool[i]:
            print(d[1], t[1])
