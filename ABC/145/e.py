N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)
AB.sort(key=lambda x: x[0])
dp[AB[0]] = []

