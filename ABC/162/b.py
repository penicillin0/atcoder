N = int(input())
ans = 0
for i in range(1, N + 1):
    if not (i % 5 == 0 or i % 3 == 0):
        ans += i
print(ans)

