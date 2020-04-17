S = list(input())
N = len(S)

info = []
rcnt, lcnt = 0, 0
key = 'R'
for i in range(N):
    if key == 'R':
        if S[i] == 'R':
            rcnt += 1
        else:
            key = 'L'
            lcnt = 1
            idx = i - 1
    else:
        if S[i] == 'R':
            info.append([idx, rcnt, lcnt])
            key = 'R'
            rcnt = 1
            lcnt = 0
        else:
            lcnt += 1
    if i == N - 1:
        info.append([idx, rcnt, lcnt])

A = [0] * N
for inf in info:
    a, b, c, = inf
    if (b + c) % 2 == 0:
        A[a], A[a + 1] = int((b + c) / 2), int((b + c) / 2)
    else:
        v = int((b + c) // 2)
        d = (max(b, c) - 1)
        if b > c:
            b, c = v + 1, v
        else:
            b, c = v, v + 1
        if d % 2 == 0:
            A[a], A[a + 1] = b, c
        else:
            A[a], A[a + 1] = c, b

A = list(map(str, A))
print(' '.join(A))
