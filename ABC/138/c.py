N = int(input())
V = list(map(int, input().split()))
V.sort()

ans = 0
for i in range(N):
    if i == 0:
        ans = V[i]
    else:
        ans = (ans + V[i]) / 2
print(ans)
