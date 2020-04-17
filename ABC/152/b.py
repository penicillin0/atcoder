a, b = map(str, input().split())


A, B = '', ''
for i in range(int(b)):
    A += a
for j in range(int(a)):
    B += b
C = [A, B]
C.sort()
print(C[0])