import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
ans = 0
sm = 0
for i in range(n):
    if i % 2 == 0:
        if sm + A[i] > 0:
            sm += A[i]
        elif sm + A[i] <= 0:
            num = -(sm + A[i]) + 1
            sm += A[i] + num
            ans += num
    else:
        if sm + A[i] < 0:
            sm += A[i]
        elif sm + A[i] >= 0:
            num = -(sm + A[i]) - 1
            sm += A[i] + num
            ans += -num
ans1 = ans
ans, sm = 0, 0
for i in range(n):
    if i % 2 != 0:
        if sm + A[i] > 0:
            sm += A[i]
        elif sm + A[i] <= 0:
            num = -(sm + A[i]) + 1
            sm += A[i] + num
            ans += num
    else:
        if sm + A[i] < 0:
            sm += A[i]
        elif sm + A[i] >= 0:
            num = -(sm + A[i]) - 1
            sm += A[i] + num
            ans += -num
print(min(ans, ans1))
