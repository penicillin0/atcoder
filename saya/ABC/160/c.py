k, n = map(int, input().split())
A = list(map(int, input().split()))

kyori = []
for i in range(n - 1):
    kyori.append(abs(A[i] - A[i + 1]))

kyori.append(A[0] + (k-A[-1]))

ans = k - max(kyori)
print(ans)