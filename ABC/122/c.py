N, Q = map(int, input().split())
S = input()
S = S.replace('AC', 'ac')
ans = [0] * N
LR = [list(map(int, input().split())) for _ in range(Q)]

flag = False
count = 0
for num, s in enumerate(S):
    if flag is False:
        if s == 'a':
            flag = True
            ans[num] = count
            continue
        else:
            ans[num] = count
    else:
        if s == 'c':
            count += 2
            ans[num] = count
            flag = False
            continue
        else:
            ans[num] = count
            flag = False

for lr in LR:
    l, s = lr[0], lr[1]
    print((ans[s - 1] - ans[l - 1]) // 2)
