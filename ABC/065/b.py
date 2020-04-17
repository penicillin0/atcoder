import sys
input = sys.stdin.readline
N = int(input())
a = [int(input()) for _ in range(N)]
b = [-1] * N
botan = a[0]

cnt = 0

for i in range(N):
    if botan == 2:
        print(cnt + 1)
        exit()
    cnt += 1
    botan = a[botan - 1]

print(-1)
