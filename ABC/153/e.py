h, n = map(int, input().split())
INF = 10 ** 5
AB = [list(map(int, input().split())) for _ in range(n)]
dp = [[float('inf')] * (h + 10 ** 4 + 100) for _ in range(n + 1)]

# i までの魔法 n
# j HP h
# dp[i][j]

for i in range(n + 1):
    dp[i][0] = 0

# i + 1種類までの魔法を使える
for i in range(n):
    # HPぴったj
    for j in range(1, h + 10 ** 4 + 100):
        if j <= AB[i][0]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i + 1][j - AB[i][0]] + AB[i][1])

ans = float('inf')
for j in range(h, h + 10 ** 4 + 100):
    ans = min(ans, dp[n][j])
print(ans)











