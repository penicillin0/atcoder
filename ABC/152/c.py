n = int(input())
P = list(map(int, input().split()))

ans = 0

mini = float('inf')

for p in P:
    mini = min(mini, p)
    if mini >= p:
        ans += 1
print(ans)