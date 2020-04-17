N, K = map(int, input().split())
S = list(input())
flag = False
zero = 0
for s in S:
    if flag is False:
        if s == '0':
            zero += 1
            flag = True
        else:
            flag = False
    else:
        if s == '0':
            continue
        else:
            flag = False
if K >= zero:
    print(N)
    exit()
ans1 = 0
ans = 0
k = K
flag = False
for i in range(zero + 1):
    count = 0
    ans1 = 0
    for i in range(N):
        if flag is False:
            if S[i] == '1':
                if count > zero:
                    ans1 += 1
            else:
                count += 1
                flag = True
                if k >= 1:
                    k -= 1
                    ans1 += 1
                else:
                    break
        else:
            if S[i] == '1':
                flag = False
                ans1 += 1
            else:
                ans1 += 1
    ans = max(ans, ans1)
print(ans)
