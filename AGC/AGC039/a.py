S = list(input())
K = int(input())
n = len(S)
SS = S[:] + S[:]
m = len(SS)

if len(set(S)) == 1:
    print(n * K // 2)
    exit()

ans0 = 0
ans1 = 0

c = 0
cnt = 1
for i in range(1, n):
    if S[i - 1] == S[i]:
        cnt += 1
        if i == n-1:
            c += cnt // 2
    else:
        if cnt >= 2:
            c += cnt // 2
        cnt = 1
ans0 = c
c = 0
cnt = 1
m = len(SS)
for i in range(1, m):
    if SS[i - 1] == SS[i]:
        cnt += 1
        if i == m - 1:
            c += cnt // 2
    else:
        if cnt >= 2:
            c += cnt // 2
        cnt = 1
ans1 = c

num = ans1 - ans0
print(ans0 + (K-1) * num)
