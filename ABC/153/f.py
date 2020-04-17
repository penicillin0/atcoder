h, n = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]
INF = 10 ** 6
dp = [[INF] * (h + 10 ** 4 + 100) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    a, b = AB[i]
    for j in range(h + 10 ** 4 + 100):
        dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])
        if j >= a:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i + 1][j - a] + b)
# for d in dp:
#     print(*d)

ans = INF
for j in range(h, h + 10 ** 4 + 100):
    ans = min(ans, dp[n][j])
print(ans)
