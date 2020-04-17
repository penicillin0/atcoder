N = int(input())

dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = float('inf')
    p = 1
    while i - p >= 0:
        dp[i] = min(dp[i], dp[i - p] + 1)
        p *= 6
    q = 9
    while i - q >= 0:
        dp[i] = min(dp[i], dp[i - q] + 1)
        q *= 9
print(dp[N])