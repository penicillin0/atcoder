S = input()

cnt = 0
amr = 1
htn = 0
for s in S[::-1]:
    if s != '?':
        s = int(s)
        cnt += s * amr
        cnt %= 13
    else:
        htn += 1
    amr = (10 * amr) % 13
print(cnt)
print(len(S))
print(htn)
print(len(S) - htn)


num = 10 ** (htn) + (5 - cnt)
print((num // 13) % (10**9+7))
