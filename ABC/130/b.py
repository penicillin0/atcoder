N, X = map(int, input().split())
L = list(map(int, input().split()))

cnt = 0
now = 0
for i in range(N):
    now += L[i]
    if now <= X:
        cnt += 1
    else:
        break
print(cnt + 1)
