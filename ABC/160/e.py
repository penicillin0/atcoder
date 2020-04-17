X, Y, A, B, C = map(int, input().split())
P = list(sorted(map(int, input().split()), reverse=True))
Q = list(sorted(map(int, input().split()), reverse=True))
R = list(sorted(map(int, input().split()), reverse=True))

S = P[:X] + Q[:Y]
S.sort(reverse=True)
S_wa = []
wa = 0
for s in S[::-1]:
    wa += s
    S_wa.append(wa)
big = S_wa[-1]
ans = S_wa[-1]

R_wa = []
wa = 0
for r in R:
    wa += r
    R_wa.append(wa)

for i in range(min(X + Y, C)):
    ans = max(ans, big + R_wa[i] - S_wa[i])
print(ans)
