from collections import Counter

n = int(input())
S = [list(sorted(input())) for _ in range(n)]

ans_key = []
ans_key = Counter(S[0]).keys()

for s in S:
    ans_key = list(set(ans_key) & set(Counter(s).keys()))

ans_dict = {}
for key in ans_key:
    ans_dict[key] = float('inf')

for s in S:
    for string in ans_key:
        ans_dict[string] = min(ans_dict[string], list(s).count(string))

ans = ''
for key in ans_dict:
    for i in range(ans_dict[key]):
        ans += key
ans = list(ans)
ans.sort()

print(''.join(ans))
