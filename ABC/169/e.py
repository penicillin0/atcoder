n = int(input())

A = []
B = []

for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

m = int(((n * 2) - 2) / 2)

A.sort()
p1 = A[m - 1]
p2 = A[m]
B.sort(reverse=True)
q1 = B[m-1]
q2 = B[m]

if p2 == q2:
    

if n % 2 == 1:
    print(q - p + 1)
else:
    print((q - p) * 2 - 1)