N = int(input())

a, b = 0, 0

M = N ** (1 / 2) + 1
M = int(M)

for i in range(1, M + 1):
    if N % i == 0:
        a, b = i, N // i


print(a + b - 2)
