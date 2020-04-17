N = int(input())
A = list(map(int, input().split()))
A = [0] + A

# 答え dp[N]
dp = [0] * (N + 1)
dp[0] = float('inf')  # 0本目はないので無限コスト
dp[1] = 0

for i in range(2, N + 1):
    cost1 = abs(A[i] - A[i - 1])
    cost2 = abs(A[i] - A[i - 2])
    dp[i] = min(dp[i - 1] + cost1, dp[i - 2] + cost2)
print(dp[N])
