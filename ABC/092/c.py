N = int(input())
A = [0] + list(map(int, input().split())) + [0]

s = 0
for i in range(N + 1):
    s += abs(A[i] - A[i + 1])

for i in range(N):
    a, b, c = A[i], A[i + 1], A[i + 2]
    print(s + abs(c-a) - (abs(a-b)+abs(b-c)))
