n, m = map(int, input().split())
H = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(m)]

ans = [0] * n
for a, b in AB:
    if H[a-1] < H[b-1]:
        ans[a - 1] += 1
    elif H[a-1] > H[b-1]:
        ans[b - 1] += 1
    else:
        ans[a - 1] += 1
        ans[b - 1] += 1


print(ans.count(0))
