n, k = map(int, input().split())

if n == k:
    print(0)
    exit()

if n < k:
    print(min(abs(n-k), n))
else:
    n = n % k
    print(min(abs(n-k), n))
