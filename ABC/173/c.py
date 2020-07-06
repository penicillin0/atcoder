from itertools import combinations
h, w, k = map(int, input().split())

C = [list(input()) for _ in range(h)]

ans = 0

for p in range(h):
    h_combs = list(combinations(list(range(h)), p))
    for q in range(w):
        w_combs = list(combinations(list(range(w)), q))
        for h_comb in h_combs:
            for w_comb in w_combs:
                cnt = 0
                for i in range(h):
                    for j in range(w):
                        if i not in h_comb and j not in w_comb and C[i][j] == '#':
                            cnt += 1
                if cnt == k:
                    ans += 1
print(ans)
