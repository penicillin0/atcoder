A, B = map(int, input().split())
ans = max(2 * A - 1, 2 * B - 1)
ans = max(ans, A + B)
print(ans)
