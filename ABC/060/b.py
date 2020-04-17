A, B, C = map(int, input().split())

for i in range(1, B + 2):
    NA = i * A
    if NA % B == C:
        print('YES')
        exit()
print('NO')