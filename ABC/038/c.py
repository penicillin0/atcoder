N = int(input())
A = list(map(int, input().split()))

ans = 0
cnt = 1
for i in range(1, N):
    if A[i] > A[i - 1]:
        cnt += 1
    else:
        ans += cnt * (cnt + 1) / 2
        cnt = 1
ans += cnt * (cnt + 1) / 2
print(int(ans))
