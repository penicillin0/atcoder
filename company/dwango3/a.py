T = list(input())
n = len(T)

count, ans = 0, 0
flag = False

for t in T:
    if flag is False:
        if t == '2' or t == '?':
            flag = True
        else:
            count = 0
    else:
        if t == '5' or t == '?':
            count += 2
            ans = max(ans, count)
            flag = False
        else:
            flag = False
            count = 0
print(ans)
