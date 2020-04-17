n = int(input())
B = list(map(int, input().split()))


A0 = B[0]
An = B[-1]
A = []
A.append(A0)
for i in range(n - 2):
    a = min(B[i], B[i + 1])
    A.append(a)
A.append(An)

print(sum(A))
