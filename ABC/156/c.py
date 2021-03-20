N = int(input())
X = list(map(int, input().split()))

ans = float('inf')
for i in range(1, 100):
    cost = 0
    for x in X:
        cost += (i - x) ** 2
    ans = min(ans, cost)
print(ans)
