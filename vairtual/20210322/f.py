N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]

A = [-1] * N
B = [-1] * N

min_value = float('inf')

for i in range(N):
    for j in range(N):
        if min_value > C[j][i]:
            # print(i, j, C[i][j])
            min_i_j = (i, j)
            min_value = C[j][i]

A[min_i_j[0]] = min_value

flag = True
for j in range(N):
    B[j] = C[j][min_i_j[0]] - min_value

for i in range(N):
    b = B[min_i_j[1]]
    A[i] = C[min_i_j[1]][i] - b
    if A[i] < 0:
        flag = False

for i in range(N):
    for j in range(N):
        if C[j][i] != A[i] + B[j]:
            flag = False

if flag is False:
    print('No')
else:

    print('Yes')
    print(' '.join(list(map(str, B))))
    print(' '.join(list(map(str, A))))
