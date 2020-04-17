N = int(input())
A = list(map(int, input().split()))

cnt = 0
ans = 0
absmin = 10**9
for i in range(N):
    ans += abs(A[i])
    if A[i] < 0:
        cnt += 1
    if abs(A[i]) < absmin:
        absmin = abs(A[i])

if cnt % 2 == 0 or 0 in A:
    print(ans)
else:
    print(ans - 2 * absmin)
