from collections import Counter

n = int(input())
A = list(map(int, input().split()))
S = Counter(A)

all_ans = 0
for key in S:
    value = S[key]
    if value >= 2:
        all_ans += (value * (value - 1)) // 2

for a in A:
    if S[a] <= 1:
        print(all_ans)
    else:
        print(all_ans - (S[a] - 1))
