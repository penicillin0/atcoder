N = int(input())
H = list(map(int, input().split()))

ans = 0
cnt = 0
for i in range(0, N-1):
    if H[i] >= H[i + 1]:
        cnt += 1
        ans = max(cnt, ans)
    else:
        cnt = 0
print(ans)
