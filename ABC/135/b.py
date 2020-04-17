import copy
N = int(input())
P = list(map(int, input().split()))

Q = sorted(P)

if Q == P:
    print('YES')
    exit()

for i in range(N):
    for j in range(i + 1, N):
        R = copy.deepcopy(P)
        R[i], R[j] = R[j], R[i]
        if R == Q:
            print('YES')
            exit()
print('NO')
