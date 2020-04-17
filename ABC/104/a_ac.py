D, G = map(int, input().split())
src = [tuple(map(int, input().split())) for i in range(D)]
ans = 10**9
for b in range(2**D):
    score = 0
    ac = 0
    for k in range(D):
        if b & (1 << k):
            p, c = src[k]
            score += c
            ac += p
            score += p * (k + 1) * 100
    if score >= G:
        ans = min(ans, ac)
        continue
    for k in range(D - 1, -1, -1):
        print(k)
        if b & (1 << k) == 0:
            p, c = src[k]
            if score + p * (k + 1) * 100 < G:
                score += p * (k + 1) * 100 + c
                ac += p
            else:
                rem = G - score
                ac += -(-rem // (k + 1) // 100)
                ans = min(ans, ac)
                break
print(ans)
