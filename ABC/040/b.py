n = int(input())
ans = float('inf')
for i in range(1, n + 1):
    j = n // i
    amari = n - (i * j)

    sa = abs(i - j)
    ans = min(ans, amari + sa)
print(ans)
