N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

p, q = 0, 0
B1 = []
B2 = []
for i in range(N):
    p += A1[i]
    B1.append(p)
    j = (N - 1) - i
    q += A2[j]
    B2.append(q)
B2.reverse()

ans = 0

for i in range(N):
    ans = max(ans, B1[i] + B2[i])
print(ans)
