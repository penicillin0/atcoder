S = list(input())
n = len(S)

for i in range(n):
    for j in range(i, n):
        if S[:i] + S[j:] == list('keyence'):
            print('YES')
            exit()
print('NO')
