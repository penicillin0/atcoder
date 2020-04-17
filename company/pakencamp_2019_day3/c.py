from itertools import combinations
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
index = [i for i in range(M)]
comb = list(combinations(index, 2))

answer = 0

for c in comb:
    a, b = c
    ans = 0
    for i in range(N):
        ans += max(A[i][a], A[i][b])

    answer = max(ans, answer)
print(answer)

