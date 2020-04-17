N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0
for a in range(K + 1):  # a回まで行う
    for i in range(a + 1):
        get = a - i
        rel = i
        if rel >= get:
            continue
        for j in range(get + 1):  # 右からj個とる
            point = 0
            right = j
            left = get - right
            if right + left > N:
                continue
            l = V[:left]
            r = V[N - right:]
            al = r + l
            al.sort()
            point = sum(al[rel:])
            ans = max(ans, point)
print(ans)
