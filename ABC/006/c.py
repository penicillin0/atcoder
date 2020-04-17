N, M = map(int, input().split())
a, b, c = 0, 0, 0

for b in range(N + 1):
    c = (M - 2 * N - b) / 2
    a = N - (b + c)
    if 0 <= a and 0 <= c and a == a // 1 and c == c // 1:
        print(int(a), int(b), int(c))
        exit()
print('-1 -1 -1')