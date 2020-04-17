N, M = map(int, input().split())
time = 1900 * M + 100 * (N - M)
a = 1 - (1 / 2)**M
ans = ((1 / 2)**M) * (1 / (1 - a)**2) * time

print(int(ans))