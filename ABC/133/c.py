L, R = map(int, input().split())

if (R - L) >= 2019:
    print(0)
    exit()

L, R = L % 2019, R % 2019

if L >= R:
    R += 2019

ans = float('inf')

for i in range(L, R + 1):
    for j in range(i + 1, R + 1):
        ans = min(ans, (i * j) % 2019)
print(ans)