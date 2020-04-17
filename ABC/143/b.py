n = int(input())
D = list(map(int, input().split()))

ans = 0

for i in range(n):
    a = D[i]
    for j in range(i + 1, n):
        b = D[j]
        ans += a * b
print(ans)
