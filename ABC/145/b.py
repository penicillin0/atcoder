N = int(input())
S = list(input())

if N % 2 == 1:
    print('No')
    exit()
else:
    num = N // 2

T = S[:num]
# print(T)
if T + T == S:
    print('Yes')
else:
    print('No')