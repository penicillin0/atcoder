import sys
input = sys.stdin.readline
N, M = map(int, input().split())
X, Y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A, B = 0, 0
cnt = 0
time = 0

while True:
    if A > N - 1 or B > M - 1:
        break
    if cnt % 2 == 0:  # Aにいる
        if time > a[-1]:
            break
        if time <= a[A]:
            cnt += 1
            time = a[A] + X
        else:
            A += 1
    else:
        if time > b[-1]:
            break
        if time <= b[B]:
            cnt += 1
            time = b[B] + Y
        else:
            B += 1

print(cnt // 2)
