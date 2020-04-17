N = int(input())
S = list(input())
ans = ''
a = list('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')
for s in S:
    ind = a.index(s) + N
    # print(ind)
    ans = ans + a[ind]
print(''.join(ans))
