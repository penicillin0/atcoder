A, B = map(int, input().split())

tap = 1
ans = 0
while True:
    if tap >= B:
        print(ans)
        exit()
    tap += (A - 1)
    ans += 1
