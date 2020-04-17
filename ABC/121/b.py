N, M, C = map(int, input().split())
B = list(map(int, input().split()))
AA = []
for i in range(N):
    AA.append(list(map(int, input().split())))

ans = 0
for A in AA:
    allall = 0
    for i in range(M):
        allall += A[i] * B[i]
    if allall + C > 0:
        ans += 1
print(ans)
