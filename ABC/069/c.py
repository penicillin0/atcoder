N, M = map(int, input().split())
if 2 * N >= M:
    print(M // 2)
    exit()
else:
    print(N + (M - 2 * N) // 4)
