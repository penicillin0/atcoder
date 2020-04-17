def kyori(a, b, x, y):
    if a > b:
        a, b = b, a
    return min(abs(b - a), abs(x - a) + abs(b - y) + 1)


n, x, y = map(int, input().split())
ans = [0] * (n)

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        # print(i, j, kyori(i, j, x, y))
        ans[kyori(i, j, x, y)] += 1
# print(ans)
for i in range(1, n):
    print(ans[i])
