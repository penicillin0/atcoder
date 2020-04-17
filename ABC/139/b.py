A, B = map(int, input().split())

tap = 1
ans = 0
for i in range(B+1):
   if tap >= B:
        print(ans)
        exit()
    tap += (A - 1)
    ans += 1
