import copy
n = int(input())
S = list(input())

table = [{}]
cnt = {'R': 0, 'G': 0, 'B': 0}
for s in S:
    cnt[s] += 1
    table.append([s, copy.deepcopy(cnt)])

RGB = set(['R', 'G', 'B'])
ans = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if table[i][0] != table[j][0]:
            kigou_set = RGB ^ set([table[i][0], table[j][0]])
            kigou = list(kigou_set)[0]
            sa = table[-1][1][kigou] - table[j][1][kigou]
            ans += sa
            l = j + (j - i)
            # print(i, j, l)
            if l <= n:
                if table[l][0] == kigou:
                    # print(table[l][1],kigou)
                    ans -= 1
                
print(ans)
