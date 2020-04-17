ssss = list(input())
ans = {}

for s in ssss:
    if s in ans:
        ans[s] += 1
    else:
        ans[s] = 1
for s in ans:
    if ans[s] == 2:
        continue
    else:
        print('No')
        exit()
print('Yes')