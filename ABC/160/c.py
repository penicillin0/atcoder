k, n = map(int, input().split())
A = list(map(int, input().split()))
big = 0

for i in range(n - 1):
    big = max(big, abs(A[i + 1] - A[i]))
b = (k - A[-1]) + A[0]
big = max(big, b)
print(k - big)



