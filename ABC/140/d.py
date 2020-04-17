n, k = map(int, input().split())
S = list(input())

cnt = 0

if len(S) == 1:
    print(0)
    exit()

if S[0] == 'R' and S[1] == 'R':
    cnt += 1

if S[-1] == 'L' and S[-2] == 'L':
    cnt += 1


for i in range(1, n - 1):
    lft = S[i - 1]
    rgt = S[i + 1]
    me = S[i]
    if lft == me == 'L':
        cnt += 1

    if rgt == me == 'R':
        cnt += 1

ans = min(cnt + 2 * k, n - 1)

print(ans)
