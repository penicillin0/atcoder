S = list(input())
K = int(input())

komoji = list('abcdefghijklmnopqrstuvwxyz')
komoji2 = komoji + komoji
index = {}

num = 1
for k in komoji:
    index[k] = num
    num += 1

cost = []
for s in S:
    c = 27 - index[s]
    if c == 26:
        c = 0
    cost.append(c)

ans = []

for num, c in enumerate(cost):
    if c <= K:
        K -= c
        ans.append('a')
    else:
        ans.append(S[num])
        continue
if K != 0:
    K %= 26
    last = ans[-1]
    last = komoji2[komoji.index(last) + K]
    ans[-1] = last
print(''.join(ans))