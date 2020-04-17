N = int(input())
a, b, c = int(input()), int(input()), int(input())
A = [a, b, c]
a = max(A)
c = min(A)
b = sum(A) - a - c
A = [a, b, c]

if (c <= N <= a and a - c == 2) or (N in A):
    print('NO')
    exit()

for i in range(100):
    if N <= 0:
        print('YES')
        exit()
    if N - 3 not in A:
        N -= 3
    elif N - 2 not in A:
        N -= 2
    elif N - 1 not in A:
        N -= 1
    else:
        print('NO')
        exit()
if N <= 0:
    print('YES')
else:
    print('NO')
