N = int(input())
A = list(map(int, input().split()))
B = 1
ans = 0
for i in range(N):
    for j in range(32, 0, -1):
        if A[i] % (2**j) == 0:
            ans += j
            A[i] = A[i] / (2**j)
print(ans)
