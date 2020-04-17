n, k = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

F.sort(reverse=True)
A.sort()

print(F, A)

if sum(A) <= k:
    print(0)
    exit()

big = A[0] * F[0]
j = 0
for i in range(1, n):
    num = big // F[i]
    if num >= A[i]:
        continue
    else:
        j += A[i] - num
        A[i] = num
print(A, j)


ans = []
for i in range(n):
    ans.append((A[i] * F[i], A[i], F[i], i, big - ))

print(ans)

if j >= k:
    for i in range(j):
        ans.sort(key=lambda x: x[0])
