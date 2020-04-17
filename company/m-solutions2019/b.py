S = list(input())
n = len(S)
num = S.count('o')
if (15 - n) + num >= 8:
    print('YES')
else:
    print('NO')