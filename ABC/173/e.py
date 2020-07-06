n, k = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True, key=lambda x: abs(x))
# print(A)
num = 10 ** 9 + 7
minus_len = 0
plus_len = 0
ans = 1
last_minus = -1
last_plus = -1
for i in range(k):
    if A[i] < 0:
        last_minus = A[i]
        minus_len += 1
    else:
        last_plus = A[i]
        plus_len += 1
    ans = (ans * abs(A[i])) % num
print(ans)
next_minus = -1
next_plus = -1
for i in range(k - 1, n):
    if A[i] < 0:
        next_minus = A[i]
    else:
        next_plus = A[i]

minus_len = 0
plus_len = 0

for i in range(n):
    if A[i] < 0:
        minus_len += 1
    else:
        plus_len += 1


ans = 1
last_minus = -1
last_plus = -1
for i in range(k):
    if A[i] < 0:
        last_minus = A[i]
    else:
        last_plus = A[i]
    ans = (ans * abs(A[i])) % num
print(ans)
next_minus = -1
next_plus = -1
for i in range(k - 1, n):
    if A[i] < 0:
        next_minus = A[i]
    else:
        next_plus = A[i]


if k - (minus_len // 2) * 2 <= plus_len:
    if ans < 0:
        ans /= last_minus
        ans *= next_plus
        ans %= num
        print(ans)
    else:
        print(ans)
else:
    if ans > 0:
        ans /= last_plus
        ans *= next_minus
        ans *= - 1
        ans %= num
        print(ans)
    else:
        print(ans)


# print(ans)
