X, Y = map(int, input().split())
ans = 1
while X <= Y:
    X *= 2
    ans += 1
print(ans - 1)
